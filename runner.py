import subprocess
import argparse
import yaml

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def run_scraping(config):
    url = config['urls']
    for uri in url:
        result = subprocess.run(
            ['python', 'scraper.py', '--url', uri]
        )
        print(result.stdout)
        if result.returncode != 0:
            raise ValueError(f"Erro na execução {uri}:", result.stderr)


def run_retrieval(tables, config):
    representation = config['retrieval']['representation']
    for table in tables:
        comand_line = f"--table {table} --representation {representation}"
        result = subprocess.run(
            ['python', 'retrieve.py'] + comand_line.split() ,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.returncode != 0:
            raise ValueError(f"Erro na execução {table}:", result.stderr)

def generate_psedudocuments(tables, config):
    temperature = config['document']['temperatures']
    prompt_path = config['document']['prompt_path']
    destination = config['document']['destination']
    
    for table in tables:
        for temp in temperature:
            print("Start runner Generator pseudodocuments")
            
            if adversarial:
                print("Adversarial!")
                command = f"--table {table} --prompt_path {prompt_path} --destination {destination} --temperature {temp} --adversarial"
            else:
                command = f"--table {table} --question --prompt_path {prompt_path} --destination {destination} --temperature {temp}"
            
            result = subprocess.run(
                ['python', 'generate.py'] + command.split(),
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
parser.add_argument("--config", type=str, default="./config.yaml", help="Path to the configuration file")
parser.add_argument("--adversarial", action="store_true")
parser.add_argument("--scraping", action="store_true")

args = parser.parse_args()

retrieval = args.retrieval
doc = args.document
conf = args.config
config = load_config(conf)
adversarial = args.adversarial

if args.scraping:
    run_scraping(config)

if doc:
    tables_g = config['tables_generation']
    generate_psedudocuments(tables_g, config)

if retrieval:
    tables_r = config['tables_retrieval']
    run_retrieval(tables_r, config)