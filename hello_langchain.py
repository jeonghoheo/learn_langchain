from langchain_ollama import ChatOllama

# init Ollama model
llm=ChatOllama(model="qwen2.5-coder",
    temperature=0.7,     # Controls randomness/creativity (range: 0 to 1)
    num_predict=100)     # Maximum number of tokens to generate

# Set temperature to 0 for deterministic and consistent output
llm_consistent = ChatOllama(model="qwen2.5-coder", temperature=0)

# Set temperature to 0 for deterministic, focused, and creative output
llm_creative = ChatOllama(model="qwen2.5-coder", temperature=1)

question = "AI의 미래를 한 문장으로 예측해줘"

print("Temperature 0:")
print(llm_consistent.invoke(question).content)

print("\nTemperature 1:")
print(llm_creative.invoke(question).content)