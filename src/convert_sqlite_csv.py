import sqlite3
import pandas as pd
import argparse
import os


parser = argparse.ArgumentParser(description='Convert SQLite tables to CSV files.')
parser.add_argument('--database', help='Name to the SQLite database file.')
args = parser.parse_args()

# /home/fernando/Documentos/TCC/ClaimDB/train_dbs/train_dbs/address.sqlite
# conn = sqlite3.connect(f'/home/fernando/Documentos/TCC/ClaimDB/train_dbs/train_dbs/address.sqlite')

conn = sqlite3.connect(f'../ClaimDB/train_dbs/train_dbs/{args.database}.sqlite')
# conn = sqlite3.connect(f'../spider/database/{args.database}/{args.database}.sqlite')

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()
#print(tabelas)

for tabela in tabelas:
    try:
        df = pd.read_sql_query(f"SELECT * FROM {tabela[0]}", conn)
        print(f"Table: {tabela[0]}")
        print(f"Shape: {df.shape}")
        print(df.head())
        print("\n")
        os.makedirs(f'../ClaimDB/train_dbs/train_dbs/{args.database}/data_csv/', exist_ok=True)
        # # os.makedirs(f'../spider/database/{args.database}/data_csv/', exist_ok=True)
        # # df.to_csv(f'../spider/database/{args.database}/data_csv/{tabela[0]}.csv', index=False)
        df.to_csv(f'../ClaimDB/train_dbs/train_dbs/{args.database}/data_csv/{tabela[0]}.csv', index=False)
    except Exception as e:
        print(f"Erro ao ler a tabela {tabela[0]}: {e}")
conn.close()