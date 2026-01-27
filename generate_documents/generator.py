from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
from dotenv import load_dotenv
import os
import time
import yaml

load_dotenv()

class Generator:
    def __init__(self, source, llm, destination, prompt_path):
        self.name_llm = llm
        self.source = pd.read_csv(source)
        self.destination = destination
        self.api_key = os.getenv("GOOGLE_API_KEY")

        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_yaml = yaml.safe_load(f)
        self.prompt = (
            f"{prompt_yaml['system']}\n\n"
            f"{prompt_yaml['instructions']}\n\n"
            f"{prompt_yaml['context']}\n\n"
        )

    def generate_document_md(self, question=None, persona=None):
        if question is None:
            raise KeyError("A question must be provided to generate a document.")
   
        self.llm = GoogleGenerativeAI(model=self.name_llm, google_api_key=self.api_key)
        prompt_template = ChatPromptTemplate.from_template(self.prompt)
        chain = prompt_template | self.llm
        
        max_retries = 3
        result = None
        for attempt in range(max_retries):
            try:
                result = chain.invoke({"table": self.source.to_string(), "persona": persona})
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
        
        file_path = os.path.join(self.destination, f"{question}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"File {file_path} created successfully!")
        # time.sleep(60) # Pause to avoid rate limits