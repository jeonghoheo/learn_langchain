from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# init Ollama model
llm=ChatOllama(model="qwen2.5-coder")

# create prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "You are {role}. answer this {style}."),
    ("human", "{question}")])

# apply prompt template
message = template.format_messages(
    role="Python expert",
    style="in a concise way",
    question="What is the difference between a list and a tuple in Python?"
)

print(message)
