import pandas as pd
import numpy as np
from typing import List, Dict, Any
import csv

class TableRepresentation:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    def to_linearized_column_wise(self) -> str:
        """
        Representação linearizada orientada a colunas.
        Formato usado em muitos trabalhos de table-to-text.
        
        Esta é a representação mais comum em trabalhos de ML sobre tabelas,
        onde cada coluna é tratada como uma sequência de valores.
        
        Returns:
            String com representação linearizada por coluna
        """
        result = []
        for col in self.df.columns:
            values = self.df[col].astype(str).tolist()
            col_repr = f"Column '{col}': {', '.join(values)}"
            result.append(col_repr)
        
        return "\n".join(result)
    
    def to_linearized_row_wise(self) -> str:
        """
        Representação linearizada orientada a linhas.
        Cada linha é representada como um conjunto de pares chave-valor.
        
        Este formato é mencionado no contexto de table comprehension
        e é útil para modelos que processam tabelas linha por linha.
        
        Returns:
            String com representação linearizada por linha
        """
        result = []
        for idx, row in self.df.iterrows():
            row_items = [f"{col}: {row[col]}" for col in self.df.columns]
            row_repr = f"Row {idx + 1}: " + " | ".join(row_items)
            result.append(row_repr)
        
        return "\n".join(result)
    
    def to_template_based(self) -> str:
        """
        Representação baseada em templates (sentences naturais).
        
        Converte cada linha em uma sentença natural em linguagem próxima
        ao português/inglês, útil para tasks de table-to-text generation.
        
        Returns:
            String com sentenças naturais
        """
        result = []
        for _, row in self.df.iterrows():
            # Cria uma sentença natural
            parts = [f"the {col} is {row[col]}" for col in self.df.columns]
            sentence = "This entry has " + ", ".join(parts[:-1])
            if len(parts) > 1:
                sentence += f", and {parts[-1]}"
            else:
                sentence += parts[0] if parts else ""
            sentence += "."
            result.append(sentence)
        
        return " ".join(result)
    
    def to_key_value_pairs(self) -> str:
        """
        Representação em pares chave-valor estruturados.
        
        Formato usado em alguns modelos de table understanding para
        capturar a estrutura relacional de forma explícita.
        
        Returns:
            String com pares chave-valor estruturados
        """
        result = []
        result.append(f"Table with {len(self.df)} rows and {len(self.df.columns)} columns")
        result.append(f"Columns: {', '.join(self.df.columns)}")
        result.append("\nData:")
        
        for idx, row in self.df.iterrows():
            result.append(f"\n[Record {idx + 1}]")
            for col in self.df.columns:
                result.append(f"  {col} = {row[col]}")
        
        return "\n".join(result)
    
    def to_markdown(self) -> str:
        """
        Representação em formato Markdown.
        
        Este formato é amplamente usado para visualização humana
        e também é processável por modelos de linguagem.
        
        Returns:
            String em formato Markdown
        """
        return self.df.to_markdown(index=False)
    
    def to_html_like(self) -> str:
        """
        Representação HTML-like (estruturada).
        
        Similar ao formato HTML mas adaptado para processamento textual.
        Útil para modelos que processam estruturas hierárquicas.
        
        Returns:
            String em formato HTML-like
        """
        result = ["<table>"]
        
        # Header
        header_cells = [f"<th>{col}</th>" for col in self.df.columns]
        result.append(f"  <tr> {' '.join(header_cells)} </tr>")
        
        # Rows
        for _, row in self.df.iterrows():
            row_cells = [f"<td>{row[col]}</td>" for col in self.df.columns]
            result.append(f"  <tr> {' '.join(row_cells)} </tr>")
        
        result.append("</table>")
        return "\n".join(result)
    
    def to_column_header_value_triples(self) -> str:
        """
        Representação em triplas (column, header, value).
        
        Formato inspirado em triplas RDF, mencionado no contexto de
        semantic type detection e table comprehension.
        
        Returns:
            String com triplas estruturadas
        """
        result = []
        for col_idx, col in enumerate(self.df.columns):
            for row_idx, value in enumerate(self.df[col]):
                triple = f"(col_{col_idx}, {col}, {value})"
                result.append(triple)
        
        return "\n".join(result)
    
    def to_serialized_flat(self) -> str:
        """
        Representação serializada plana (flat serialization).
        
        Concatena todos os valores da tabela em uma única sequência,
        separando colunas e linhas com delimitadores especiais.
        Útil para modelos sequence-to-sequence.
        
        Returns:
            String serializada
        """
        result = []
        
        # Header
        result.append("[HEADER]")
        result.append(" [COL] ".join(self.df.columns))
        result.append("[/HEADER]")
        
        # Rows
        result.append("[ROWS]")
        for _, row in self.df.iterrows():
            row_values = [str(row[col]) for col in self.df.columns]
            result.append("[ROW] " + " [COL] ".join(row_values) + " [/ROW]")
        result.append("[/ROWS]")
        
        return " ".join(result)
    
    def to_schema_description(self) -> str:
        """
        Representação focada no schema da tabela.
        
        Descreve a estrutura e metadados da tabela, útil para
        tasks de schema matching e data discovery mencionados na tese.
        
        Returns:
            String com descrição do schema
        """
        result = []
        result.append(f"Table Schema:")
        result.append(f"Number of columns: {len(self.df.columns)}")
        result.append(f"Number of rows: {len(self.df)}")
        result.append(f"\nColumn Metadata:")
        
        for col in self.df.columns:
            dtype = self.df[col].dtype
            n_unique = self.df[col].nunique()
            n_missing = self.df[col].isna().sum()
            
            col_info = [
                f"  Column: {col}",
                f"    Data type: {dtype}",
                f"    Unique values: {n_unique}",
                f"    Missing values: {n_missing}",
                f"    Sample values: {list(self.df[col].dropna().head(3).astype(str))}"
            ]
            result.extend(col_info)
        
        return "\n".join(result)
    
    def to_contextualized_representation(self) -> str:
        """
        Representação contextualizada (com estatísticas).
        
        Inclui contexto estatístico sobre os dados, similar ao que
        é usado em feature extraction para semantic type detection
        (Capítulo 2 - Sherlock).
        
        Returns:
            String com representação contextualizada
        """
        result = []
        result.append("=== Contextualized Table Representation ===\n")
        
        # Global table info
        result.append(f"Dimensions: {len(self.df)} rows × {len(self.df.columns)} columns")
        result.append(f"Columns: {', '.join(self.df.columns)}\n")
        
        # Column-wise contextualized info
        for col in self.df.columns:
            result.append(f"\n[Column: {col}]")
            
            # Basic stats
            result.append(f"  Type: {self.df[col].dtype}")
            result.append(f"  Cardinality: {self.df[col].nunique()}/{len(self.df)}")
            result.append(f"  Missing: {self.df[col].isna().sum()}")
            
            # Sample values
            sample_vals = self.df[col].dropna().head(5).tolist()
            result.append(f"  Sample values: {sample_vals}")
            
            # Numeric stats if applicable
            if pd.api.types.is_numeric_dtype(self.df[col]):
                result.append(f"  Mean: {self.df[col].mean():.2f}")
                result.append(f"  Std: {self.df[col].std():.2f}")
                result.append(f"  Min/Max: {self.df[col].min()}/{self.df[col].max()}")
        
        return "\n".join(result)
    
    def get_all_representations(self) -> Dict[str, str]:
        """
        Retorna todas as representações disponíveis.
        
        Returns:
            Dicionário com nome da representação e seu conteúdo
        """
        return {
            "linearized_column_wise": self.to_linearized_column_wise(),
            "linearized_row_wise": self.to_linearized_row_wise(),
            "template_based": self.to_template_based(),
            "key_value_pairs": self.to_key_value_pairs(),
            "markdown": self.to_markdown(),
            "html_like": self.to_html_like(),
            "column_header_value_triples": self.to_column_header_value_triples(),
            "serialized_flat": self.to_serialized_flat(),
            "schema_description": self.to_schema_description(),
            "contextualized": self.to_contextualized_representation()
        }