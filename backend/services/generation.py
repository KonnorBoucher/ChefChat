import ollama

def generate_answer(question:str, context:str) -> str:

    # prompt guides the model on how it should answer and what data it should use
    prompt = f"""You are a helpful cooking assistant named ChefChat. Use the following recipe information to answer the question. 
    Only use information from the provided context. If the context does not contain enough info, say so. 

    Context:
    {context}

    Question: {question}

    Answer:"""

    # Prompts model for an answer
    answer = ollama.chat(model= "llama3.2",
                         messages=[{"role": "user", "content": prompt}] 
                         )
    
    # Return the answer
    return answer["message"]["content"]