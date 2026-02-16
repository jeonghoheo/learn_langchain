from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# init Ollama model
llm=ChatOllama(model="qwen2.5-coder")

# save conversation history
conversation_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

def chat(user_input):
    # add user input to conversation history
    conversation_history.append(HumanMessage(content=user_input))
    
    # get response from Ollama model
    response = llm.invoke(conversation_history)
    
    # add model response to conversation history
    conversation_history.append(response)
    
    return response.content

# testing the chat function
print(chat("Hello! my name is Snow"))
print(chat("What is my name?"))

