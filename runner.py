import subprocess
import argparse

def run_retrieval(tables):
    for table in tables:
        comand_line = f"--table {table} --representation {8}"
        result = subprocess.run(
            ['python', 'teste.py'] + comand_line.split() ,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.returncode != 0:
            raise ValueError(f"Erro na execução {table}:", result.stderr)

def generate_psedudocuments(tables):
    temperature = [0.3, 0.5, 0.7, 0.8, 1.0]

    for table in tables:
        for temp in temperature:
            print("Start runner Generator pseudodocuments")
            command = f"--table {table} --question --prompt_path ./prompt/prompt_pseudodocument_llm.yaml --destination ./data_lake/ --temperature {temp}"
            result = subprocess.run(
                ['python', 'main.py'] + command.split(),
                capture_output=True,
                text=True
                        )
            print(result.stdout)
            if result.returncode != 0:
                raise ValueError(f"Erro na execução {table} e {temp}:", result.stderr)
            print(f"End - {table} in {temp}")

parser = argparse.ArgumentParser()
parser.add_argument("--retrieval", action="store_true")
parser.add_argument("--document", action="store_true")

args = parser.parse_args()

retrieval = args.retrieval
doc = args.document

tables = [
    "/home/fernando/Documentos/TCC/spider/database/store_1/data_csv/artists.csv",
    "/home/fernando/Documentos/TCC/spider/database/store_1/data_csv/playlists.csv",
    "/home/fernando/Documentos/TCC/spider/database/phone_1/data_csv/chip_model.csv",
    "/home/fernando/Documentos/TCC/spider/database/game_1/data_csv/Video_Games.csv",
    "/home/fernando/Documentos/TCC/spider/database/employee_hire_evaluation/data_csv/employee.csv",
    "/home/fernando/Documentos/TCC/spider/database/driving_school/data_csv/Addresses.csv",
    "/home/fernando/Documentos/TCC/spider/database/city_record/data_csv/city.csv",
    "/home/fernando/Documentos/TCC/spider/database/coffee_shop/data_csv/shop.csv",
    "/home/fernando/Documentos/TCC/spider/database/concert_singer/data_csv/stadium.csv",
    "/home/fernando/Documentos/TCC/spider/database/concert_singer/data_csv/singer.csv"
]

if doc:
    generate_psedudocuments(tables)

if retrieval:
    run_retrieval(tables)