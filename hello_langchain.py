from langchain_ollama import ChatOllama

# init Ollama model
llm=ChatOllama(model="qwen2.5-coder")

# asking a question
questions = [
    "What is python?",
    "what is 1 + 1?",
    "How do you feel today?"
]

# print the result
for question in questions:
    response = llm.invoke(question)
    print(f":Q:{question}\n")
    print(f"A:{response.content}\n")