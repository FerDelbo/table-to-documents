import requests  
from bs4 import BeautifulSoup  
import pandas as pd  
import io
import os

class Scraper:
    def __init__(self, url, path_save="./data/wiki_doc/", path_table="./data/wiki_table/"):
        self.url = url
        self.path_save = path_save
        self.path_table = path_table

    def connect(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
        }
        
        response = requests.get(self.url, headers=headers)  
        
        if response.status_code == 200:
            self.soup =  BeautifulSoup(response.text, "html.parser")  # Analisar e retornar o HTML
            return self.soup
        else:
            print(f"Falha ao recuperar a página. Código de status: {response.status_code}")
            return None  # Retorne None se a solicitação falhar

    def extract_content(self):
        self.title = self.soup.find("h1").get_text()  # tag <h1>
        body = self.soup.find("div", class_="mw-parser-output")
        md_lines = [f"# {self.title}\n"]
        for element in body.children:
        
            if element.name in ["h2", "h3", "h4", "h5", "h6"]:
                 nivel = int(element.name[1])

            elif element.name == "p":
                # self.content.append(element.get_text())
                paragraph = [p.get_text() for p in self.soup.find_all("p")] # tag <p>
        self.title = title
        self.content = paragraph
        return self.content
    
    def extract_table(self):
        tables = []
        no_caption_count = 0
        for table in self.soup.find_all("table", {"class": "wikitable"}):
            caption = table.find("caption")
            if caption:
                print("Caption: ", caption)
                title = caption.get_text()
            else:
                heading = table.find_previous(["h1", "h2", "h3", "h4", "h5", "h6"])
                if heading:
                    print("Heading: ", heading)
                    title = heading.get_text()
                else:
                    no_caption_count += 1
                    print("No caption or heading found for this table. Assigning default title.")
                    title = f"table_without_title_{no_caption_count}"
            
            print("Title: ", title)
            df = pd.read_html(io.StringIO(str(table)))[0]
            tables.append({"title": str(title), "df": df})
        self.tables = tables
        return self.tables
    
    def save_content(self):
        os.makedirs(self.path_save, exist_ok=True)
        with open(f"{self.path_save}{self.title}.md", "w", encoding="utf-8") as file:
            for item in self.content:
                file.write(item + "\n")
    
    def save_tables(self):
        for item in self.tables:
            df = item["df"]
            tbl_title = item.get("title")
            df.to_csv(f"{self.path_table}{tbl_title}{self.title}.csv", index=False)

    def run(self):
        self.connect()
        self.extract_content()
        self.extract_table()
        self.save_content()
        self.save_tables()