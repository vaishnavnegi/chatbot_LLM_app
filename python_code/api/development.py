from agents import (GuardAgent)
import os

def main():
    pass

if __name__ == "__main__":
    guard_agent = GuardAgent()
    
    messages = []
    while True:
        # Display the chat history
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\nPrint Messages ...............")
        for message in messages:
            print(f"{message['role'].capitalize()}: {message['content']}")
        
        # Get user input
        prompt = input("User: ")
        messages.append({"role": "user", "content": prompt})

        # Get GuardAgent's response
        guard_agent_response = guard_agent.get_response(messages)
        # print("Guard Agent Response: ", guard_agent_response)
        if guard_agent_response["memory"]["guard_decision"] == "not allowed":
             messages.append(guard_agent_response)
             continue
         
        