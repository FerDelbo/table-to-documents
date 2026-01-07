from generate_documents.generator import Generator
import pandas as pd

if __name__ == "__main__":
    source = "./answer.csv"
    llm = "gemini-2.5-flash"
    # llm = "gemini-3-pro-preview"
    destination = "./documents/"

    generator = Generator(source, llm, destination)

    questions = pd.read_csv(source)["question"].tolist()

    # Mudar para 307
    for pos in range(179, len(questions) + 1):
        generator.generate_document_md(questions[pos])
        print(f"Generated document number {pos}")