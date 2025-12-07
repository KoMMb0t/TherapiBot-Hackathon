'''
TherapiBot: The Cognitive Counter-Speaker

This is the main application file for TherapiBot.
'''

import os
import requests
from elevenlabs import generate, play
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
RAINDROP_API_URL = "https://api.raindrop.io/v1" # This is a placeholder URL

def get_cognitive_restructuring(text):
    '''
    This function sends the user's text to the Raindrop platform and gets a cognitive restructuring response.
    '''
    headers = {
        "Authorization": f"Bearer {os.getenv('RAINDROP_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    response = requests.post(f"{RAINDROP_API_URL}/restructure", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "I'm sorry, I'm having trouble understanding. Please try again."

def main():
    '''
    The main function of the application.
    '''
    print("TherapiBot: Hello! Tell me what's on your mind.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("TherapiBot: Goodbye!")
            break
        
        response_text = get_cognitive_restructuring(user_input)
        print(f"TherapiBot: {response_text}")
        
        audio = generate(
            text=response_text,
            voice="Bella", # You can change the voice here
            api_key=ELEVENLABS_API_KEY
        )
        play(audio)

if __name__ == "__main__":
    main()
