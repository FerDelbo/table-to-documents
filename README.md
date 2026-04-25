# 📄 Table-to-Documents

> Geração de pseudo-documentos a partir de tabelas relacionais com LLM e recuperação semântica esparsa via SPLADE.

Este projeto foi desenvolvido como parte de um Trabalho de Conclusão de Curso (TCC) e investiga a tarefa de **table augmentation**: dado uma tabela estruturada, o sistema gera documentos em linguagem natural que descrevem semanticamente seu conteúdo, e em seguida recupera os documentos mais relevantes para ela usando recuperação esparsa.

O pipeline é avaliado sobre tabelas extraídas do [Spider 1](https://yale-lily.github.io/spider), um benchmark amplamente utilizado para tarefas de *text-to-SQL*.

---

<!-- ## 🎯 Motivação Acadêmica

Tabelas relacionais são fontes ricas de informação, mas sua estrutura bidimensional dificulta o uso direto em sistemas de recuperação baseados em linguagem natural. Este trabalho propõe um pipeline que:

1. **Representa** a tabela em diferentes formatos textuais (9 estratégias implementadas)
2. **Gera** pseudo-documentos usando um LLM (Gemini), condicionado a uma persona definida automaticamente
3. **Recupera** os documentos mais relevantes para uma tabela de consulta usando SPLADE (*Sparse Lexical and Expansion Model*)
4. **Avalia** a qualidade da recuperação com Precision@K e Recall@K

A combinação de geração por LLM com recuperação esparsa permite explorar como diferentes representações de tabela afetam a qualidade do retrieval — questão central investigada neste trabalho.

--- -->

## 🔁 Pipeline

```
Tabela CSV
     │
     ▼
Representação Textual (9 estratégias)
     │
     ├──► Definição de Persona (LLM)
     │
     ▼
Geração de Pseudo-documento (.md) via Gemini
     │
     ▼
Corpus de Pseudo-documentos
     │
     ▼
Retrieval com SPLADE
     │
     ▼
Top-K Documentos + Precision@K / Recall@K
```

---

## 📁 Estrutura do Projeto

```
table-to-documents/
├── src/
│   ├── table_representation.py     # 9 estratégias de representação tabular
│   ├── generation/
│   │   ├── generator.py            # Geração de documentos com LLM
│   │   └── agent.py                # Agente LLM (persona e validação)
│   └── retrieval/
│       └── splade.py               # Retrieval esparso + métricas
│
├── prompts/                        # Templates de prompt em YAML
├── data/
│   ├── spider.zip                  # Dataset Spider 1 (extrair antes de usar)
│   ├── ground_truth.csv            # Pares tabela ↔ documento gerado
│   ├── answer.csv                  # Pares tabela ↔ questão (Spider)
│   └── results.csv                 # Resultado sobre o retorno de documentos

│
├── pseudodocuments/                # Documentos gerados
│
├── generate.py                     # Entrypoint: geração de documentos
├── retrieve.py                     # Entrypoint: retrieval e avaliação
├── runner.py                       # Orquestrador batch
├── config.yaml                     # Configuração do runner
└── .env.example                    # Template de variáveis de ambiente
```

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.10+
- Conta Google com acesso à [Gemini API](https://aistudio.google.com/)
- GPU recomendada para inferência com SPLADE (funciona em CPU, porém mais lento)

### 1. Clone o repositório

```bash
git clone https://github.com/FerDelbo/table-to-documents.git
cd table-to-documents
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais:

```env
GOOGLE_API_KEY=sua_chave_aqui
API_URL=https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}
API_KEY=sua_chave_aqui
MODEL_NAME=gemini-3.0-flash
PROVIDER=gemini
```

### 5. Extraia o dataset Spider

```bash
cd data/
unzip spider.zip
cd ..
```

---

## 🚀 Uso

### Gerar um pseudo-documento a partir de uma tabela

```bash
python generate.py \
  --table data/spider/database/schema_escolhido/data_csv/sua_tabela.csv \
  --prompt_path prompts/prompt_pseudodocument_not_question.yaml \
  --destination pseudodocuments/ \
  --temperature 0.7
```

Para usar as questões em linguagem natural do Spider como contexto adicional:

```bash
python generate.py \
  --table data/spider/database/schema_escolhido/data_csv/sua_tabela.csv \
  --question \
  --prompt_path prompts/prompt_pseudodocument_llm.yaml \
  --destination pseudodocuments/
```

### Recuperar documentos relevantes para uma tabela

```bash
python retrieve.py \
  --table data/tables/sua_tabela.csv \
  --representation 3 \
  --output outputs/results.csv
```

### Executar em lote com o runner

```bash
# Gerar documentos para todas as tabelas configuradas
python runner.py --document --config config.yaml

# Executar retrieval
python runner.py --retrieval --config config.yaml

# Ambos em sequência
python runner.py --document --retrieval --config config.yaml
```

Exemplo de `config.yaml`:

```yaml
tables:
  - data/tables/basketball_match.csv
  - data/tables/artists.csv

document:
  temperatures: [0.5, 0.7, 1.0]
  prompt_path: prompts/prompt_pseudodocument_not_question.yaml
  destination: pseudodocuments/

retrieval:
  representation: 3
```

---

## 🗂️ Estratégias de Representação Tabular

A classe `TableRepresentation` implementa 9 formas de converter uma tabela CSV em texto, usadas tanto na geração quanto no retrieval:

| # | Estratégia | Descrição |
|---|---|---|
| 0 | `linearized_column_wise` | Valores listados por coluna |
| 1 | `linearized_row_wise` | Cada linha como pares chave-valor |
| 2 | `template_based` | Sentenças em linguagem natural por linha |
| 3 | `markdown` | Tabela no formato Markdown padrão |
| 4 | `html_like` | Estrutura HTML textual |
| 5 | `column_header_value_triples` | Triplas inspiradas em RDF `(col_idx, header, value)` |
| 6 | `serialized_flat` | Sequência plana com tokens `[COL]` e `[ROW]` |
| 7 | `schema_description` | Metadados do schema (tipos, cardinalidade, valores faltantes) |
| 8 | `contextualized` | Schema + resumo estatístico (média, desvio, min/max) |

---

## 📊 Avaliação

Após o retrieval, as seguintes métricas são calculadas automaticamente por tabela:

- **Precision@K** — proporção de documentos recuperados que são relevantes

Os resultados são salvos na planilha `data/results.csv` com o nome da tabela, estratégia de representação utilizada, métricas, IDs recuperados e a similiradidade de cosseno. 

---

## 📦 Principais Dependências

| Biblioteca | Uso |
|---|---|
| `sentence-transformers` | Retrieval esparso com SPLADE |
| `langchain` + `langchain-google-genai` | Orquestração do LLM |
| `google-genai` | Acesso à API Gemini |
| `pandas` | Leitura e manipulação das tabelas |
| `PyYAML` | Carregamento dos templates de prompt |
| `python-dotenv` | Gerenciamento de variáveis de ambiente |
| `torch` + `transformers` | Backend de inferência dos modelos |

---

## 📄 Dataset

Este projeto utiliza o **Spider 1** — um benchmark de larga escala para tarefas de *text-to-SQL*, com tabelas de múltiplos domínios.

- Dataset original: [https://yale-lily.github.io/spider](https://yale-lily.github.io/spider)
- Yu, T. et al. *Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task*. EMNLP, 2018.

---

## 📝 Sobre

Projeto desenvolvido como Trabalho de Conclusão de Curso (TCC).

Dúvidas ou sugestões, abra uma [issue](https://github.com/FerDelbo/table-to-documents/issues).