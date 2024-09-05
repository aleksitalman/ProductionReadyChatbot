import requests
import time

def chat_with_model():
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Send the POST request to the server
        url = "http://127.0.0.1:8000/chat"
        payload = {"input": user_input}

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()

            result = response.json()
            llm_response = result.get("response", "No response")
            time_taken = result.get("time_taken", "N/A")

            print(f"LLM Model: {llm_response}\n")
            print(f"------------Time taken: {time_taken:.2f} seconds---------------\n")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    print("Chatbot started. Type 'exit' or 'quit' to end the chat.")
    chat_with_model()
