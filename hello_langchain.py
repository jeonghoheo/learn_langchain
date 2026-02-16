from langchain_ollama import ChatOllama

# init Ollama model
llm=ChatOllama(model="qwen2.5-coder")

# asking a question
response = llm.invoke("What is the capital of France?")

# print the result
print(response.content)