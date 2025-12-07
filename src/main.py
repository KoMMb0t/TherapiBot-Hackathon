
import os
import requests
import random
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
RAINDROP_API_KEY = os.getenv("RAINDROP_API_KEY") # Placeholder for actual Raindrop API key
RAINDROP_API_URL = "https://api.raindrop.io/v1"  # Placeholder for actual Raindrop API endpoint

# Set the ElevenLabs API key
if ELEVENLABS_API_KEY:
    set_api_key(ELEVENLABS_API_KEY)
else:
    print("Warning: ELEVENLABS_API_KEY not found. Voice generation will be disabled.")

# --- Mock Raindrop API Interaction ---

def get_cognitive_restructuring_mock(text):
    """
    Mocks the interaction with the Raindrop platform.

    In a real implementation, this function would make an HTTP request to the
    Raindrop MCP, which would orchestrate multiple agents (Analyst, Empath, Pacer)
    to generate a nuanced response.

    For this hackathon prototype, we simulate this process.
    """
    print("\n[Simulating Raindrop MCP]...")
    print(f"[Analyst Agent] Identifying cognitive distortion in: [3m'{text}'[0m")
    
    # Simulate identifying a cognitive distortion
    distortions = {
        "i'm not good enough": "Emotional Reasoning",
        "i always mess up": "Overgeneralization",
        "i'll never succeed": "Catastrophizing",
        "this is all my fault": "Personalization"
    }
    
    identified_distortion = "Unknown"
    for phrase, distortion in distortions.items():
        if phrase in text.lower():
            identified_distortion = distortion
            break
    
    print(f"[Analyst Agent] -> Identified: {identified_distortion}")
    print("[Empath Agent] -> Detected tone: Discouraged")
    print("[Pacer Agent] -> Setting pace: Calm and Reassuring")

    # Simulate generating a response based on the agents' outputs
    responses = {
        "Emotional Reasoning": "Feeling something strongly doesn't make it true. Let's separate the feeling from the facts. What evidence do you have that you aren't 'good enough'?",
        "Overgeneralization": "You're using very strong words like 'always'. Can you think of a time when you didn't mess up? I bet you can. One mistake doesn't define your entire track record.",
        "Catastrophizing": "It sounds like you're jumping to the worst-case scenario. What's a more realistic outcome? Let's walk back from the edge a little.",
        "Personalization": "Are you taking responsibility for something that wasn't entirely in your control? Let's look at the bigger picture and see what other factors were at play.",
        "Unknown": "That's a heavy thought. Let's try to break it down. What makes you say that?"
    }

    response_text = responses.get(identified_distortion, responses["Unknown"])
    print(f"[Raindrop MCP] -> Generated Response: [3m'{response_text}'[0m")
    return response_text

# --- Main Application Logic ---

def main():
    """
    The main function of the application.
    """
    print("\n[1m[36m--- Welcome to TherapiBot ---[0m")
    print("Your cognitive counter-speaker. Ready when you are.")
    print("(Type 'exit' or 'quit' to end the session)\n")

    while True:
        try:
            user_input = input("[1mYou:[0m ")
            if user_input.lower() in ["exit", "quit"]:
                print("\n[36mTherapiBot:[0m Goodbye! Remember to be kind to yourself.")
                break
            
            if not user_input.strip():
                continue

            # Get the cognitive restructuring from the (mocked) Raindrop platform
            response_text = get_cognitive_restructuring_mock(user_input)
            
            print(f"\n[36mTherapiBot:[0m {response_text}")
            
            # Generate and play the audio response using ElevenLabs
            if ELEVENLABS_API_KEY:
                try:
                    print("\n[Generating voice with ElevenLabs]...")
                    audio = generate(
                        text=response_text,
                        voice="Bella",  # A friendly and empathetic voice
                        model="eleven_multilingual_v2"
                    )
                    play(audio)
                    print("[Voice generation complete]")
                except Exception as e:
                    print(f"\n[Error generating voice with ElevenLabs: {e}]")
                    print("[Continuing with text-only response.]")
            else:
                print("\n[Skipping voice generation. Set ELEVENLABS_API_KEY to enable.]")

        except (KeyboardInterrupt, EOFError):
            print("\n\n[36mTherapiBot:[0m Goodbye! Remember to be kind to yourself.")
            break

if __name__ == "__main__":
    main()
