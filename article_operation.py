import os
import json
import re

class cleanup:

    @classmethod
    def cleanup_text(cls, text):
            cleaned = text.replace('\n', ' ')  # Replace with space
            cleaned = text.strip()  # Remove leading/trailing

            # 2. Remove special characters (keep only letters, numbers, spaces)
            cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)

            # 3. Remove extra whitespace
            cleaned = ' '.join(text.split())  # Removes ALL extra spaces/newlines

            # 4. Remove specific symbols
            cleaned = text.replace('!', '').replace('@', '')
            cleaned = cleaned.lower()

            return cleaned

class ArticleOperation:

    def __init__(self):
        self.filename = "articles.json"

    def readAllArticles(self):
        articles = ""
        for i in range(self.GetNumOfArticle()):
            article = self.readAtIndex(i)
            articles += article
        return articles

    def readAtIndex(self, index):
        data = self.__openArticles()
        if data and len(data[0]) > index:
            content = data[0][index]['content']
            text = cleanup.cleanup_text(content)       
            return text
        
    def GetNumOfArticle(self):
        data = self.__openArticles()
        return len(data[0])

    def __openArticles(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data
        except:
            print("error occured")        

   
    
class QueryOperation:
    def __init__(self):
        self.filename = "question.json"

    def readAllQuestion(self):
        questions = []
        for i in range(self.__getNumQuestion()):
            data = self.readQuestionAnswerAtIndex(i)
            questions.append(data['question'])

        return questions
    
    def readAllAnswers(self):
        answers = []
        for i in range(self.__getNumQuestion()):
            data = self.readQuestionAnswerAtIndex(i)
            answers.append(data['answer'])
        
        return answers
    
    def readAllQuestionAndAnswers(self):
        return self.__openQuestion

    def readQuestionAnswerAtIndex(self, index):
        data = self.__openQuestion()
        if data and len(data) > index:
            question = cleanup.cleanup_text(data[index]['question'])
            answer = cleanup.cleanup_text(data[index]['answer'])
            text = {'question':question, 'answer':answer}
            return text
        pass

    def __getNumQuestion(self):
        data = self.__openQuestion()
        return len(data)

    def __openQuestion(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data
        except:
            print("error occured")       
    