from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
from dotenv import load_dotenv
import os
import time
import yaml

load_dotenv()

class Generator:
    def __init__(self, table_representation, llm, destination, prompt_path, temperature=0.7):
        self.name_llm = llm
        self.table_representation = table_representation
        self.destination = destination
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.temperature = temperature

        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_yaml = yaml.safe_load(f)
        self.prompt = (
            f"{prompt_yaml['system']}\n\n"
            f"{prompt_yaml['instructions']}\n\n"
            f"{prompt_yaml['context']}\n\n"
        )

    def generate_document_md(self, persona=None, questions=None, name_table=None):
        if questions:
            # table_questions = pd.read_csv('../../answer.csv')
            table_questions = pd.read_csv('/home/fernando/Documentos/TCC/table-to-documents/answer.csv')
            relevant_questions = table_questions[table_questions['table name'] == name_table]['question'].tolist()
            with open('./prompt/prompt_pseudodocument_llm.yaml', "r", encoding="utf-8") as f:
                prompt_yaml = yaml.safe_load(f)
                questions_str = "\n".join(relevant_questions)
                context_with_questions = prompt_yaml['context'].replace('{questions}', questions_str)
                self.prompt = (
                    f"{prompt_yaml['system']}\n\n"
                    f"{prompt_yaml['instructions']}\n\n"
                    f"{context_with_questions}\n\n"
                )
            print("Using question-based prompt template.")
            
        self.llm = GoogleGenerativeAI(model=self.name_llm, google_api_key=self.api_key, temperature=self.temperature)
        prompt_template = ChatPromptTemplate.from_template(self.prompt)
        chain = prompt_template | self.llm
        
        max_retries = 3
        result = None
        for attempt in range(max_retries):
            try:
                result = chain.invoke({"table": self.table_representation, "persona": persona})
                break  
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    sleep_time = 60 * (attempt + 1)
                    print(f"Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                else:
                    print("Max retries reached. Raising exception.")
                    raise
        name_document = result.splitlines()[0]
        file_path = os.path.join(self.destination, f"{name_document}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result)
        return file_path
        # time.sleep(60) # Pause to avoid rate limits