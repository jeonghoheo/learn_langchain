from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# init Ollama model
llm=ChatOllama(model="qwen2.5-coder")

system_prompts = [
    "You are a pirate. Say like a pirate.",
    "You are a Shakespeare. Say it in an old-fashioned way.",
    "You are a 5 years old kid. Say it in a childish way.",]

question = "What is the weather like today?"

for prompt in system_prompts:
    print(f"[{prompt[:20]}...]")
    messages = [SystemMessage(content=prompt), HumanMessage(content=question)]
    response = llm.invoke(messages)
    print(f"{response.content}\n")