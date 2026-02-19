from sentence_transformers import SparseEncoder, util

class Retrieval:
    def __init__(self, name='naver/splade-cocondenser-ensembledistil'):
        self.name_model=name
        self.corpus = []
    
    def set_splade(self):
        self.model = SparseEncoder(self.name_model)

    def retrieval(self, table, documents, k):
        query_embeddings = self.model.encode_query(table, convert_to_tensor=True)
        
        for doc in documents:
            self.corpus.append(open(doc).read())

        corpus_embeddings = self.model.encode_document(self.corpus, convert_to_tensor=True)
        
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