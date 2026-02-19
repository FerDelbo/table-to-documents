from src.generate_documents.custom_agent import agent_LLM
from src.generate_documents.generator import Generator
from src.table_representation import TableRepresentation
import argparse
from pathlib import Path
import pyexcel as p

def register_par_table_document(table_name, document_path):
    book = p.get_book(file_name='./ground_truth.csv')
    sheet = book[0]
    sheet.row += [table_name, document_path]
    book.save_as('./ground_truth.csv')

def save_persona(table_name, persona, k=0):
    if k == 0:
        title = persona.splitlines()[0]
        with open(f'./personas/{title}_{table_name}.md', 'w', encoding='utf-8') as f:
            f.write(persona)
    else:
        title = persona.splitlines()[0]
        with open(f'./personas/{title}_{table_name}.md', 'w', encoding='utf-8') as f:
            f.write(persona)
            k = k - 1

def get_persona(name):
    with open(f'./personas/{name}', 'r', encoding='utf-8') as f:
        return f.read()

#argumnets
parser = argparse.ArgumentParser(description="Generate documents from a CSV source using a specified LLM.")
# parser.add_argument("--source", default="./answer.csv", help="Path to the CSV source file")
parser.add_argument("--llm_model", default="gemini-3-flash-preview", help="Name of the LLM to use")
parser.add_argument("--llm_name", default="gemini", help="Name of the LLM provider")
parser.add_argument("--destination", default="./pseudodocuments/", help="Path to the destination directory")
parser.add_argument("--prompt_path", default="./prompt/prompt_pseudodocument_not_question.yaml", help="Path to the prompt YAML file")
parser.add_argument("--question", action="store_true", help="Generate a question-based document")
parser.add_argument("--table", help="Path to the CSV table for persona definition")
parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature for the LLM (0.0-1.0)")
# parser.add_argument("--k", default=0, help="K generate documents the table")

args = parser.parse_args()
# source = args.source
llm = args.llm_model
name_llm = args.llm_name
destination = args.destination
prompt_path = args.prompt_path
question = args.question
table = args.table
# top_k = args.k
temperature = args.temperature

table_name = Path(table).stem

#table representation
table_representation = TableRepresentation(csv_path=table)
table_repr_str = table_representation.to_markdown()

# # define persona
my_agent = agent_LLM()
persona = my_agent.define_person(table=table)
# save_persona(table_name=table_name, persona=persona)
# persona = get_persona(name="Alright, persona loaded. It's great to meet you. I'm Alex._basketball_match.md")

#generated document
generator = Generator(
table_representation=table_repr_str,
llm=llm,
destination=destination,
prompt_path=prompt_path,
temperature=temperature
)

response = generator.generate_document_md(persona=persona, questions=question, name_table=table_name)
# response = open(f'/home/fernando/Documentos/TCC/table-to-documents/pseudodocuments/# The Power of the Road: Analyzing Elite Performance in the ACC Standings.md', 'r', encoding='utf-8').read()
register_par_table_document(table_name=table_name, document_path=response)

# validate = my_agent.validate_document(document=response, table=table)
# print("Validation result:", validate)

# register_par_table_document(table_name=table_name, document_path=response, validate=validate)