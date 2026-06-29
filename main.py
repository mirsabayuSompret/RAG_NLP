from crawl import crawl;
from article_operation import ArticleOperation, QueryOperation
from chunking import Chunkin, ChunkinWithLangChain
from embedding import Embedding
from retrieval import VectorRetrievalCosineSimilarity, VectorRetrievalUsingFAISS
from llm import LLM
from evaluate import Evaluation

class main :
    def __init__(self):

        

    def __crawlForData(self):
        c = crawl()
        c.get_data()

    def __ReadDownloadedArticles(self):
        c = ArticleOperation()
        content = c.readAllArticles()
        print(content)
        print(c.GetNumOfArticle())

    def __setupTest(self):
        print(f"main for RAG")
        articleOps = ArticleOperation()
        content = articleOps.readAllArticles()
        chunk = ChunkinWithLangChain()
        chunks = chunk.CreateChunk(content)
        embed = Embedding()
        chunk_embed = embed.embed(chunks)
        queryOps = QueryOperation()
        question = queryOps.readAllQuestion()[6]
        expected_answer = queryOps.readAllAnswers()[6]
        print(f"question : {question}")
        question_embed = embed.embed(question)
        retrieval = VectorRetrievalUsingFAISS()
        retrieve_chunk = retrieval.retrieve(question_embed, chunk_embed, chunks,10)
        print(f"retrieve context : {retrieve_chunk}")
        llm = LLM()
        response_rag = llm.response_RAG(retrieve_chunk, question)
        print(f"response RAG : {response_rag}")
        response_nonRAG = llm.response_NonRAG(question)
        print(f"response NON RAG : {response_nonRAG}")
        evaluate = Evaluation()
        eval_rag = evaluate.Evaluate(response_rag, question, expected_answer, content)
        print(f"evaluasi rag : {eval_rag}")
        eval_nonrag = evaluate.Evaluate(response_rag, question, expected_answer, content)
        print(f"evaluasi non rag : {eval_nonrag}")



if __name__ == "__main__":
    main()
        



