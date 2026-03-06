from src.scraping.scrape_wiki import Scraper
import argparse

parser = argparse.ArgumentParser("Scraping Wikipedia page")
parser.add_argument("--url", help="URL of the Wikipedia page to scrape")
parser.add_argument("--path_article", default="./data/wiki_doc/", help="Path to the configuration file for scraping")
parser.add_argument("--path_table", default="./data/wiki_table/", help="Path to the configuration file for scraping")
args = parser.parse_args()

path_table = args.path_table
url = args.url
path_doc = args.path_article


print("Iniciando o processo de scraping...")
soup = Scraper(url=url, path_save=path_doc, path_table=path_table)
# soup.run()
soup.connect()
table = soup.extract_table()
print("========",url,"=========")
print(len(table))
print("========================")