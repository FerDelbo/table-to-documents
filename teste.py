import pandas as pd
from src.retrieval.retrieval_splade import Retrieval
from src.table_representation import TableRepresentation
import argparse
from pathlib import Path
import pyexcel as p

def save_results(sheet_path, table, representation, result_retrive, grouth_true, metrics, num_doc=50, k=5):
    ids_retrive = [hit['corpus_id'] for hit in result_retrive[0][:]]
    
    table_name = Path(table).stem
    book = p.get_book(file_name=sheet_path)
    sheet = book[0]
    sheet.row += [
        table_name,#Table
        representation,
        k,
        grouth_true, #result
        ids_retrive, #retrieval
        f"precision: {metrics[0]}\nrecall: {metrics[1]}", #metrics
        result_retrive, #cosine
        num_doc #num documents
    ]
    book.save_as(sheet_path)

parser = argparse.ArgumentParser("Retrieval for documents")
parser.add_argument("--table", help="Path to the CSV table for persona definition")
parser.add_argument("--output", default='./results.csv')
parser.add_argument("--representation", type=int, help="""
                    Selection the representation using for table, only number.\n
                    0-linearized_column_wis\n
                    1-linearized_row_wis\n
                    2-template_based\n
                    3-markdown\n
                    4-html_like\n
                    5-column_header_value_triples\n
                    6-serialized_flat\n
                    7-schema_description\n
                    8-contextualized_representation\n
                    """)
args = parser.parse_args()

table = args.table
output_table=args.output
rep_position = args.representation

df = pd.read_csv('./ground_truth.csv')

corpus = df['Document'].to_list()
# print(corpus)

table_name = Path(table).stem
# table_name = 'artists'

filter = df['Table'] == table_name

ids = df[filter]

# 9 representações
if rep_position < 0 or rep_position > 9:
    raise  ValueError("This representation not avaible.")
else:
    table_repre = TableRepresentation(table)
    rep = table_repre.get_all_representations()
    representation = list(rep.values())
    name_rep = list(rep.keys())
    table_representantion = representation[rep_position]
    print(table_representantion)

model = Retrieval()
model.set_splade()
result = model.retrieval(documents=corpus, table=table_representantion, k=5)
print(result)
metrics = model.evaluation(ids.index)

save_results(output_table, table, name_rep[rep_position], result, ids.index, metrics)