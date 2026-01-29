from scr.generate_documents.custom_agent import agent_LLM
from scr.generate_documents.generator import Generator
from scr.table_representation import TableRepresentation
import argparse
from pathlib import Path

#argumnets
parser = argparse.ArgumentParser(description="Generate documents from a CSV source using a specified LLM.")
# parser.add_argument("--source", default="./answer.csv", help="Path to the CSV source file")
parser.add_argument("--llm_model", default="gemini-2.5-flash", help="Name of the LLM to use")
parser.add_argument("--llm_name", default="gemini", help="Name of the LLM provider")
parser.add_argument("--destination", default="./pseudodocuments/", help="Path to the destination directory")
parser.add_argument("--prompt_path", default="./prompt/prompt_pseudodocument_not_question.yaml", help="Path to the prompt YAML file")
# parser.add_argument("--question", help="Specific question to generate a document")
parser.add_argument("--table", help="Path to the CSV table for persona definition")
# parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature for the LLM (0.0-1.0)")

args = parser.parse_args()
# source = args.source
llm = args.llm_model
name_llm = args.llm_name
destination = args.destination
prompt_path = args.prompt_path
# question = args.question
table = args.table
# temperature = args.temperature

table_name = Path(table).stem

#table representation
table_representation = TableRepresentation(csv_path=table)
table_repr_str = table_representation.to_linearized_column_wise()

# define persona
# my_agent = agent_LLM()
# persona = my_agent.define_person(table=table)
# open(f'./personas/persona_{table_name}.md', 'w', encoding='utf-8').write(persona)
with open(f'./personas/persona_{table_name}.md', 'r', encoding='utf-8') as f:
    persona = f.read()

#generated document
generator = Generator(
	table_representation=table_repr_str,
	llm=llm,
	destination=destination,
	prompt_path=prompt_path,
)

response = generator.generate_document_md(persona=persona)