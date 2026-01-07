from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
from dotenv import load_dotenv
import os
import time

load_dotenv()

class Generator:
    def __init__(self, source, llm, destination):
        self.name_llm = llm
        self.source = pd.read_csv(source)
        self.destination = destination
        self.api_key = os.getenv("GOOGLE_API_KEY")
    
    def generate_document_md(self, question):
        # self.llm = gemini-3-pro-previewnit_chat_model(self.name_llm)
        self.llm = GoogleGenerativeAI(model=self.name_llm, google_api_key=self.api_key)
        prompt = ChatPromptTemplate.from_template("""
            You are an expert agent in generating technical documentation in Markdown format\n.
            Your main function is to receive a specific question as input and generate a complete and structured Markdown (.md)
            document that answers that question exhaustively and accurately.\n
            The generated document must be formatted exclusively in Markdown, including headings, subheadings, lists,
            and code blocks (when appropriate) to ensure clarity and readability, addressing all relevant aspects of the raised question.\n
            Use the following data to answer the question: Here is the document: {table}.\n
            Here is the question: {question}\n
        """)
        chain = prompt | self.llm
        
        max_retries = 3
        result = None
        for attempt in range(max_retries):
            try:
                result = chain.invoke({"table": self.source.to_string(), "question": question})
                break  # Success
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
        time.sleep(60)