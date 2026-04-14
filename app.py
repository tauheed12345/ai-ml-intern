import os
from google import genai
from dotenv import load_dotenv

# Loading API key from .env file for security
load_dotenv()

def get_gemini_response(user_query):
    """
    Function to connect with Gemini API and fetch the response.
    """
    # Initialize the client with the API key
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    try:
        # Requesting response from the model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_query
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def run_app():
    print("--- Simple AI Query Script ---")
    
    # Requirement 1: Accept user input
    user_input = input("Enter your question: ")

    if user_input.strip():
        print("\nFetching response...")
        
        # Requirement 2 & 3: Send query and get clear response
        answer = get_gemini_response(user_input)
        
        print("\nAI Response:")
        print(answer)
    else:
        print("Input cannot be empty.")

if __name__ == "__main__":
    run_app()