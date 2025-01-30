from langchain_groq import ChatGroq

class LLMs():
        
    llama70b=ChatGroq(model_name="llama3-70b-8192")
    llama8b=ChatGroq(model_name="llama3-8b-8192")
    gemma2=ChatGroq(model_name="gemma2-9b-it")
    mixtral = ChatGroq(model_name="mixtral-8x7b-32768")