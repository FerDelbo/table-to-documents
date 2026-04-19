import requests  
from bs4 import BeautifulSoup  
import pandas as pd  
import io
import os
import re
import numpy as np

class WikiScraper:
    def __init__(self, url, path_save="./data/wiki/wiki_doc/", path_table="./data/wiki/wiki_table/", threshold=0.1):
        self.url = url
        self.path_save = path_save
        self.path_table = path_table
        self.augmentation_threshold = float(threshold)

        self.soup = None
        self.title = None
        self.content_text = ""
        self.sections = []
        self.tables = []
        self.selected_table = None

    def connect(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
        }
        
        response = requests.get(self.url, headers=headers)  
        
        if response.status_code == 200:
            self.soup =  BeautifulSoup(response.text, "html.parser")
            return self.soup
        else:
            print(f"Falha ao recuperar a página. Código de status: {response.status_code}")
            return None  

        

    def extract_content(self):
        title_tag = (
            self.soup.find("span", class_="mw-page-title-main")
            or self.soup.find("h1", id="firstHeading")
            or self.soup.find("title")
        )
        text = title_tag.get_text().strip() if title_tag else ""
        if not text:
            text = self.url.split("/")[-1].replace("_", " ")
        self.title = text.replace("\n", "")
        text = self.soup.find("span", class_="mw-page-title-main")
        if not text:
            url = self.url
            text = url.split("/")[-1].replace("_", " ")
        else:
            text = text.get_text().strip()
        self.title = text.replace("\n", "")

        body = (
            self.soup.find("main", class_="mw-body")
            or self.soup.find("div", id="bodyContent")
            or self.soup.find("div", class_="mw-parser-output")
            or self.soup
        )

        sections = []
        current_heading = self.title
        current_paragraphs = []

        content_root = body.find("div", class_="mw-parser-output") if body is not None else None
        if content_root is None:
            content_root = body

        if content_root is None:
            print("Aviso: não foi possível encontrar o corpo do artigo. Salvando apenas o título.")
            self.content_text = f"## {self.title}\n"
            return self.content_text

        for element in content_root.find_all(["div", "p"], recursive=True):

            if element.name == "div" and "mw-heading" in element.get("class", []):
                
                if current_paragraphs:
                    sections.append({
                        "heading": current_heading,
                        "text": "\n".join(current_paragraphs)
                    })
                
                inner = element.find(["h1", "h2", "h3", "h4", "h5", "h6"])
                current_heading = inner.get_text(strip=True) if inner else ""
                current_paragraphs = []

            elif element.name == "p":
                
                if element.find_parent("table"):
                    continue
                text = element.get_text(strip=True)
                if text:
                    current_paragraphs.append(text)

        
        if current_paragraphs:
            sections.append({
                "heading": current_heading,
                "text": "\n".join(current_paragraphs)
            })

        self.content_text = "\n\n".join(
            f"## {s['heading']}\n{s['text']}" for s in sections
        )
        # print("Content:", self.content_text)
        return self.content_text
    
    def extract_table(self):
        tables = []
        no_caption_count = 0

        for table in self.soup.find_all("table", {"class": "wikitable"}):
            caption = table.find("caption")
            
            if caption:
                # print("Caption: ", caption)
                title = caption.get_text()
                title = title.replace("\n", " ")
            else:
                heading = table.find_previous(["h1", "h2", "h3", "h4", "h5", "h6"])
                if heading:
                    # print("Heading: ", heading)
                    title = heading.get_text()
                    title = title.replace("\n", " ")
                else:
                    no_caption_count += 1
                    print("No caption or heading found for this table. Assigning default title.")
                    title = f"{self.title}_table"
             
            prev_p = table.find_previous("p")
            next_p = table.find_next("p")
            context = ""

            if prev_p:
                context += prev_p.get_text(strip=True) + " "
            if next_p:
                context += next_p.get_text(strip=True)
            
            try:
                df = pd.read_html(io.StringIO(str(table)))[0]
                if isinstance(df.columns, pd.MultiIndex):
                  df.columns = [
                        " | ".join(str(c) for c in col).strip()
                        for col in df.columns
                    ]
                tables.append(
                    {
                        "title": title,
                        "df": df,
                        "n_rows": len(df),
                        "n_cols": len(df.columns),
                        "context": context,
                    }
                )
            except Exception as e:
                print(f"Não foi possível parsear tabela '{title}': {e}")
 
        self.tables = tables
        if not self.tables:
            print("Não há tabelas nesse artigo")
            return self

        return self.tables  
    

    def _term_frequency(self, token, sentence):
        return sentence.count(token) / len(sentence) if len(sentence) > 0 else 0.0

    def __inverse_document_frequency(self, word, corpus):
        count_of_documents = len(corpus) + 1
        count_of_documents_with_word = sum([1 for doc in corpus if word in doc]) + 1
        idf = np.log10(count_of_documents/count_of_documents_with_word) + 1
        return idf

    def TF_IDF(self, word, document, corpus):
        return self._term_frequency(word, document) * self.__inverse_document_frequency(word, corpus)
    
    def _tokenize(self, text):
        return re.findall(r"[a-z0-9]+", text.lower())

    def _cell_tfidf_score(self, cell_value, corpus):
        tokens = self._tokenize(cell_value)
        tokens = [t for t in tokens if len(t) > 0]
        if not tokens:
            return 0.0
 
        token_scores = []
        for token in tokens:
            # Score máximo do token entre todas as sentenças do corpus
            best = max(
                (self.TF_IDF(token, sentence, corpus) for sentence in corpus),
                default=0.0,
            )
            token_scores.append(best)
 
        return sum(token_scores) / len(token_scores)

    def score_all_tables(self):
        raw_sentences = re.split(r"(?<=[.!?])\s+", self.content_text)
        corpus = [
            re.findall(r"[a-z0-9]+", s.lower())
            for s in raw_sentences if s.strip()
        ]
 
        for tbl in self.tables:
            df = tbl["df"]
            scores = []
 
            # Nomes de colunas como termos
            for col in df.columns:
                s = self._cell_tfidf_score(str(col), corpus)
                scores.append(s)
 
            # Valores de células como termos
            for col in df.columns:
                for val in df[col].dropna():
                    cell = str(val).strip()
                    if len(cell) < 2:
                        continue
                    s = self._cell_tfidf_score(cell, corpus)
                    scores.append(s)
 
            tbl["aug_score"]        = round(sum(scores) / len(scores), 4) if scores else 0.0
            tbl["aug_n_terms"]      = len(scores)
            tbl["aug_is_candidate"] = tbl["aug_score"] >= self.augmentation_threshold
 
        best = max(self.tables, key=lambda t: t["aug_score"])
        best["aug_is_candidate"] = best["aug_score"] >= self.augmentation_threshold
        self.selected_table = best
 
        print(best["aug_score"])
        print(self.augmentation_threshold)
        
        return self.selected_table

    def save_content(self):
        os.makedirs(self.path_save, exist_ok=True)
        self.file_md = f"{self.path_save}{self.title}.md"
        with open(self.file_md, "w", encoding="utf-8") as file:
            # for item in self.sections:
            file.write(self.content_text)
    
    def save_tables(self):
        os.makedirs(self.path_table, exist_ok=True)
        self.selected_table['title'] = self.selected_table['title'].replace("/", "_")
        # print(self.selected_table['title'])
        # print(self.title)
        self.file_table = f"{self.path_table}{self.selected_table['title']}{self.title}.csv" 
        self.selected_table["df"].to_csv(self.file_table, index=False)

    
    def __parser_ground_truth(self):
        import pyexcel as p
        book = p.get_book(file_name='./data/wiki/ground_truth_wiki.csv')
        sheet = book[0]
        sheet.row += [self.file_table,self.file_md, self.url]
        book.save_as('./data/wiki/ground_truth_wiki.csv')

    def run(self):
        print(f"\n[1/4] Conectando a {self.url}")
        self.connect()
 
        print("[2/4] Extraindo conteudo...")
        self.extract_content()
 
        print("[3/4] Extraindo e pontuando tabelas...")
        self.extract_table()
 
        if not self.tables:
            print("[STOP] Artigo sem tabelas -- scraping interrompido.\n")
            return self
 
        print(f"Total de tabelas encontradas: {len(self.tables)}")
        
        self.score_all_tables()
 
        if self.selected_table and self.selected_table.get("aug_is_candidate"):
            print("[4/4] Salvando par (documento + tabela)...")
            self.save_content()
            self.save_tables()
            self.__parser_ground_truth()
        else:
            print("[4/4] Artigo descartado -- nenhuma tabela atingiu o threshold.")
 
        return self
    
    def run_scrape(self):
        print(f"\n[1/3] Conectando a {self.url}")
        self.connect()
 
        print("[2/3] Extraindo conteudo...")
        self.extract_content()
 
        # print("[3/4] Extraindo e pontuando tabelas...")
        # self.extract_table()
 
        # if not self.tables:
        #     print("[STOP] Artigo sem tabelas -- scraping interrompido.\n")
        #     return self
 
        # print(f"Total de tabelas encontradas: {len(self.tables)}")
        
        # self.score_all_tables()
 
        # if self.selected_table and self.selected_table.get("aug_is_candidate"):
        print("[3/3] Salvando par (documento + tabela)...")
        self.save_content()
        self.file_table = ""
        self.__parser_ground_truth()
 
        return self