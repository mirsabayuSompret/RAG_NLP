
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import faiss

class VectorRetrievalCosineSimilarity:
    def __init__(self):
        pass

    def retrieve(self, query_embed, chunks_embed, chunks_text, top_k = 3):
        query_embed = query_embed.reshape(1,-1)
        similarities = cosine_similarity(query_embed, chunks_embed)[0]

        top_k_index = similarities.argsort()[-top_k:][::-1]

        return [chunks_text[idx] for idx in top_k_index]
    
class VectorRetrievalUsingFAISS:
    def __init__(self):
        pass

    def retrieve(self, query_embed, chunks_embed, chunks_text, top_k = 3):
        chunk_embedding_np = np.array(chunks_embed).astype('float32')

        faiss.normalize_L2(chunk_embedding_np)

        chunk_dim = chunk_embedding_np.shape[1]
        faiss_idx = faiss.IndexFlatIP(chunk_dim)

        faiss_idx.add(chunk_embedding_np)

        query_embed = query_embed.reshape(1,-1)
        query_embedding_np = np.array(query_embed).astype('float32')
        faiss.normalize_L2(query_embedding_np)
        similarities, indices = faiss_idx.search(query_embedding_np, top_k)

        top_k_indices = indices[0]

        return [chunks_text[idx] for idx in top_k_indices if idx != -1]