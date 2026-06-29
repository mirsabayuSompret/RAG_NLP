from config import Config
import google.genai as genai

class LLM:
    def __init__(self):
        print('LLM generated')
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        pass

    def response_RAG(self, chunk_retrieved, question):
        try:
            prompt = f"""Context:{chunk_retrieved} Question: {question} Answer concisely using the context only."""
            response = self.client.models.generate_content(model=Config.LLM_MODEL, contents=prompt)
            return response.text
        except Exception as e:
            print(e)

    def response_NonRAG(self, question):
        try:
            prompt=f"answer this question : {question}"
            response = self.client.models.generate_content(model=Config.LLM_MODEL, contents=prompt)
            return response.text
        except Exception as e:
            print(e)

    