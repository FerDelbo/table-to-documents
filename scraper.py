from src.scraping.scrape_wiki import WikiScraper
import argparse

parser = argparse.ArgumentParser("Scraping Wikipedia page")
parser.add_argument("--url", help="URL of the Wikipedia page to scrape")
parser.add_argument("--path_article", default="./data/wiki/wiki_doc/", help="Path to the configuration file for scraping")
parser.add_argument("--path_table", default="./data/wiki/wiki_table/", help="Path to the configuration file for scraping")
parser.add_argument("--threshold", default=0.1, help="value for percent the information the table mentioned in the document for validate augmentation")
args = parser.parse_args()

path_table = args.path_table
url = args.url
path_doc = args.path_article
threshold = args.threshold

print("Iniciando o processo de scraping...")
soup = WikiScraper(url=url, path_save=path_doc, path_table=path_table, threshold=threshold)
# soup.run()
soup.run_scrape()
# print(soup.extract_content())
