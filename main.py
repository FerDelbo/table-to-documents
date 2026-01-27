# from generate_documents.generator import Generator
# import pandas as pd
# import argparse

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Generate documents from a CSV source using a specified LLM.")
#     parser.add_argument("--source", default="./answer.csv", help="Path to the CSV source file")
#     parser.add_argument("--llm", default="gemini-2.5-flash", help="Name of the LLM to use")
#     parser.add_argument("--destination", default="./documents/", help="Path to the destination directory")
#     parser.add_argument("--prompt_path", default="./prompt/prompt_simples.yaml", help="Path to the prompt YAML file")
#     parser.add_argument("--question", help="Specific question to generate a document")

#     args = parser.parse_args()
#     source = args.source
#     llm = args.llm
#     destination = args.destination
#     prompt_path = args.prompt_path
#     question = args.question

#     generator = Generator(source, llm, destination, prompt_path)

#     # questions = pd.read_csv(source)["question"].tolist()

#     generator.generate_document_md(question)
#     # # Mudar para 307
#     # for pos in range(179, len(questions) + 1):
#     #     generator.generate_document_md(questions[pos])
#     #     print(f"Generated document number {pos}")

from generate_documents.custom_agent import agent_LLM
from generate_documents.generator import Generator

# define persona
my_agent = agent_LLM()
persona = my_agent.define_person(table='./data/database/battle-checkpoint.csv', prompt="./prompt/promp_persona.yaml")
open('./personas/persona_battle-checkpoint.md', 'w', encoding='utf-8').write(persona)

#generated document
generator = Generator(
	source='./data/database/battle-checkpoint.csv',
	llm='gemini-2.5-flash',
	destination='./pseudodocuments/',
	prompt_path='./prompt/promp_define_persona.yaml',
)

response = generator.generate_document_md(question="battle-checkpoint-pseudodocument", persona=persona)
print(response)