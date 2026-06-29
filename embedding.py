from sentence_transformers import SentenceTransformer
from config import Config
from huggingface_hub import login

class Embedding:
    def __init__(self):
        self.model = "BAAI/bge-m3"
        login(token=Config.HF_TOKEN)
        pass

    def embed(self, chunks):
        model = SentenceTransformer(self.model)
        chunks_embed = model.encode(chunks,show_progress_bar=True)
        return chunks_embed
    