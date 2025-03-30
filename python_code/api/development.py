from agents import (GuardAgent,
                    ClassificationAgent
                    )
import os

def main():
    pass

if __name__ == "__main__":
    guard_agent = GuardAgent()
    classification_agent = ClassificationAgent()
    
    messages = []
    while True:
        # Display the chat history
        # os.system('cls' if os.name == 'nt' else 'clear')
        
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
         
         # Get ClassificationAgent's response
        classification_agent_response = classification_agent.get_response(messages)
        chosen_agent=classification_agent_response["memory"]["classification_decision"]
        print("Chosen Agent: ", chosen_agent)

         
        