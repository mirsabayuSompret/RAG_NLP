from config import Config
import google.genai as genai
import json


class Evaluation:
    def __init__(self):
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        pass
    
    def Evaluate(self, answer, question, expected_answer, context ):
        prompt=f"""
                You are an expert AI system auditor. Analyze the provided RAG system components and grade them across three metrics. Give the reason in bahasa indonesia
                
                INPUT DATA TO EVALUATE:
                1. User Query: {question}
                2. Fact Context: {context}
                3. Generated Answer: {answer}
                4. Expected Answer (Gold Standard): {expected_answer}
                
                GRADING INSTRUCTIONS:
                
                - HALLUCINATION PERCENTAGE (0% to 100%):
                1. Extract all discrete factual statements/claims made in the Generated Answer.
                2. Cross-check every statement against the Fact Context. 
                3. Calculate: (Number of claims NOT supported by the context / Total claims extracted) * 100.
                *Note: 0% means perfect alignment (No hallucinations). 100% means pure fabrication.*
                
                - COMPLETENESS PERCENTAGE (0% to 100%):
                1. Extract all required core facts from the Expected Answer (Gold Standard).
                2. Check how many of those core facts are successfully addressed inside the Generated Answer.
                3. Calculate: (Core facts successfully addressed / Total core facts in Expected Answer) * 100.
                
                - ACCURACY PERCENTAGE (0% to 100%):
                1. Rate the overall factual and semantic correctness of the Generated Answer compared directly to the Expected Answer.
                2. Heavily penalize direct contradictions or wrong details.
                
                CRITICAL: You must return your response ONLY as a valid JSON object matching this schema exactly:
                {{
                "hallucination_pct": float,
                "hallucination_reason": "string explaining the breakdown",
                "completeness_pct": float,
                "completeness_reason": "string explaining missed or covered points",
                "accuracy_pct": float,
                "accuracy_reason": "string explaining semantic alignments or errors"
                }}
                """
        try:
            response = self.client.models.generate_content(
                    model=Config.LLM_MODEL,
                    contents=prompt,
                    config={"response_mime_type": "application/json"}
                )

            return json.loads(response.text)
        except Exception as e:
                print(e)

