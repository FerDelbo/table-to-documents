from src.generation.agent import agent_LLM
from src.generation.generator import Generator
from src.table_representation import TableRepresentation
import argparse
from pathlib import Path
import pyexcel as p

def register_par_table_document(table_name, document_path):
    book = p.get_book(file_name='./data/ground_truth.csv')
    sheet = book[0]
    sheet.row += [table_name, document_path]
    book.save_as('./data/ground_truth.csv')

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
parser.add_argument("--prompt_path", default="./prompts/prompt_pseudodocument_not_question.yaml", help="Path to the prompt YAML file")
parser.add_argument("--question", action="store_true", help="Generate a question-based document")
parser.add_argument("--table", help="Path to the CSV table for persona definition")
parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature for the LLM (0.0-1.0)")
# parser.add_argument("--k", default=0, help="K generate documents the table")
parser.add_argument("--adversarial", action="store_true", help="Generate an adversarial document")

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
ardversarial = args.adversarial

table_name = Path(table).stem

#table representation
table_representation = TableRepresentation(csv_path=table)
table_repr_str = table_representation.to_markdown()

# # define persona
my_agent = agent_LLM()
persona = my_agent.define_person(table=table)

#generated document
generator = Generator(
table_representation=table_repr_str,
# llm=llm,
destination=destination,
prompt_path=prompt_path,
temperature=temperature
)
generator.setGemini(model_llm=llm)

if ardversarial:
    response_adversarial = generator.generate_document_adversarial(name_table=table_name)
    register_par_table_document(table_name=f"{table_name}_adversarial", document_path=response_adversarial)
else:
    response = generator.generate_document_md(persona=persona, questions=question, name_table=table_name)
    register_par_table_document(table_name=table_name, document_path=response)
