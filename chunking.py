from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunkin:
    def __init__(self):
        pass

    def CreateChunk(self, content,character_limit=150, overlap=20):
        chunk = []

        step = character_limit - overlap;

        for i in range (0, len(content), step):
            chunk_text = content[i:i + character_limit]
            chunk.append(chunk_text)

            if i + character_limit > len(content):
                break

        return chunk
    
class ChunkinWithLangChain:
    def __init__(self):
        pass

    def CreateChunk(self, content, character_limit=150, overlap=20):

        splitter = RecursiveCharacterTextSplitter(chunk_size=character_limit, chunk_overlap=overlap, separators=["\n\n", "\n", " ", ""])
        chunks = splitter.split_text(content)

        return chunks
