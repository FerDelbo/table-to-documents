from sentence_transformers import SparseEncoder, util
import pickle
import hashlib
import json
from pathlib import Path

class Retrieval:
    def __init__(self, name='naver/splade-cocondenser-ensembledistil', cache_dir='./data/embeddings_cache'):
        self.name_model=name
        self.corpus = []
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def set_splade(self):
        self.model = SparseEncoder(self.name_model)

    def _get_cache_path(self, documents):
        hash_key = hashlib.md5(json.dumps(sorted(documents)).encode()).hexdigest()
        return self.cache_dir / f"corpus_{hash_key}.pkl"

    def retrieval(self, table, documents, k):
        query_embeddings = self.model.encode_query(table, convert_to_tensor=True)
        
        for doc in documents:
            self.corpus.append(open(doc).read())

        cache_path = self._get_cache_path(documents)
        if cache_path.exists():
            # já temos os embeddings salvos
            with open(cache_path, 'rb') as file:
                corpus_embeddings = pickle.load(file)  
        else:
            corpus_embeddings = self.model.encode_document(self.corpus, convert_to_tensor=True)
            with open(cache_path, 'wb') as f:
                pickle.dump(corpus_embeddings, f)
        
        self.results = util.semantic_search(query_embeddings, corpus_embeddings, top_k=k)
        self.k = k
        return self.results
    
    def evaluation(self, qrels):
        top_k_hits = self.results[0][:self.k]
        top_k_ids = [hit['corpus_id'] for hit in top_k_hits]
        
        
        hit = 0
        for doc_id in top_k_ids:
            if doc_id in qrels:
                hit += 1
        # Calcular Precisão @ K
        # Formula: (Relevantes Recuperados) / K
        precision_at_k = hit / self.k
        
        # Calcular Recall @ K
        # Formula: (Relevantes Recuperados) / (Total de Relevantes Existentes)
        total_relevantes = len(qrels)
        
        if total_relevantes > 0:
            recall_at_k = hit / total_relevantes
        else:
            recall_at_k = 0.0
        
        print("="*20)
        print("|"+ "-"*3 + "Evaluation"+ "-"*3 +"|")
        print(f"Precision@{self.k}: {precision_at_k}")
        print(f"Recall@{self.k}: {recall_at_k}")
        print("="*20)
        return precision_at_k, recall_at_k