import ollama

def generate_answer(question:str, context:str) -> str:
    prompt = f"""You are a helpful cooking assistant named ChefChat. Use the following recipe information to answer the question. 
    Only use information from the provided context. If the context does not contain enough info, say so. 

    Context:
    {context}

    Question: {question}

    Answer:"""

    answer = ollama.chat(model= "llama3.2",
                         messages=[{"role": "user", "content": prompt}] 
                         )
    
    return answer["message"]["content"]