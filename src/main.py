'''
TherapiBot: The Cognitive Counter-Speaker

This is the main application file for TherapiBot.
'''

import os
import requests
import random
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
RAINDROP_API_KEY = os.getenv("RAINDROP_API_KEY") # Placeholder
RAINDROP_API_URL = "https://api.raindrop.io/v1"  # Placeholder

if ELEVENLABS_API_KEY:
    set_api_key(ELEVENLABS_API_KEY)
else:
    print("Warning: ELEVENLABS_API_KEY not found. Voice generation will be disabled.")

# --- Mock Raindrop API Interaction ---

def get_cognitive_restructuring_mock(text):
    "Mocks the interaction with the Raindrop platform."
    print(f"\n[Simulating Raindrop MCP]...")
    print(f"[Analyst Agent] Identifying cognitive distortion in: \033[3m'{text}'\033[0m")

    # Expanded dictionary of cognitive distortions and keywords
    distortions = {
        "Emotional Reasoning": ["i feel like", "i feel that", "i'm not good enough"],
        "Overgeneralization": ["always", "never", "every time", "everyone"],
        "Catastrophizing": ["it's going to be a disaster", "what if i fail", "i'll never succeed"],
        "Personalization": ["it's all my fault", "this is because of me"],
        "Mind Reading": ["they probably think", "i know she thinks", "he must think i'm"],
        "Fortune Telling": ["i know i'll mess up", "it's going to be terrible", "i'm going to fail"],
        "Labeling": ["i'm a loser", "i'm a failure", "i'm an idiot"],
        "Should Statements": ["i should have", "i must not", "i ought to"]
    }

    identified_distortion = "Unknown"
    for distortion, keywords in distortions.items():
        if any(keyword in text.lower() for keyword in keywords):
            identified_distortion = distortion
            break

    print(f"[Analyst Agent] -> Identified: {identified_distortion}")
    print("[Empath Agent] -> Detected tone: Discouraged, anxious")
    print("[Pacer Agent] -> Setting pace: Calm, thoughtful, and reassuring")

    # Expanded and more nuanced responses
    responses = {
        "Emotional Reasoning": [
            "Ah, the old 'if I feel it, it must be true' trap. Feelings are like the weather, constantly changing, but they aren't facts. Let's look for some solid evidence outside of that feeling.",
            "That's a powerful feeling, but let's not let it write the whole story. What would a neutral observer say about the situation?"
        ],
        "Overgeneralization": [
            "'Always' and 'never' are very strong words, don't you think? It sounds like you're painting with a very broad brush. Can you recall even one exception? That one exception proves it's not 'always'.",
            "You're generalizing from one or two events to your entire life. That's like judging a whole movie by one bad scene. Let's zoom out a bit."
        ],
        "Catastrophizing": [
            "Okay, you're jumping to the worst-possible-disaster-scenario. Let's dial it back. What's a more likely, less dramatic outcome? And even if the worst happened, would you be able to handle it? I bet you would.",
            "You've activated the mental disaster movie projector. Let's turn it off. What's one small, positive step you could take right now, instead of worrying about a future that hasn't happened?"
        ],
        "Personalization": [
            "It sounds like you're carrying the weight of the world on your shoulders. Are you sure this is 100% your fault? Let's look at the other factors at play here.",
            "You're blaming yourself for something that you likely didn't have complete control over. Let's be fair to yourself. What part of this did you *not* control?"
        ],
        "Mind Reading": [
            "You seem to have developed a superpower: mind reading! But are you sure you're getting an accurate reading? The only way to truly know what someone is thinking is to ask them. Everything else is just a story you're telling yourself.",
            "Unless you're secretly a telepath, you can't know for sure what's going on in someone else's head. Let's focus on your actions and intentions, which you *can* control."
        ],
        "Fortune Telling": [
            "So you've got a crystal ball now? Predicting a negative future doesn't make it true. It just makes you anxious right now. What if you predicted a positive outcome instead?",
            "You're acting as if the future is already written, and it's a tragedy. The future is unwritten. Let's focus on what you can do in the present to make a good outcome more likely."
        ],
        "Labeling": [
            "You are not a label. You are a complex person who sometimes makes mistakes. Slapping a negative label on yourself is unfair and inaccurate. Let's describe the action, not the person.",
            "Calling yourself 'a loser' or 'a failure' is a harsh judgment. You are a person who may have failed at something, but that doesn't make your entire being a failure. Let's be more specific and less dramatic."
        ],
        "Should Statements": [
            "'Should' is a tricky word. It often creates a lot of guilt and pressure. What if you replaced 'I should have' with 'I would have preferred to'? It feels a lot different, doesn't it?",
            "You're holding yourself to a rigid set of rules. Says who? Let's challenge that rule. Is it really true that you 'must not' do that, or is that just a high expectation you've set for yourself?"
        ],
        "Unknown": [
            "That's a heavy thought. Let's try to break it down. What makes you say that?",
            "I hear that. It sounds like you're going through a lot right now. Can you tell me more about what's leading you to that conclusion?"
        ]
    }

    response_options = responses.get(identified_distortion, responses["Unknown"])
    response_text = random.choice(response_options)
    print(f"[Raindrop MCP] -> Generated Response: \033[3m'{response_text}'\033[0m")
    return response_text

# --- Main Application Logic ---

def main():
    "The main function of the application."
    print("\n\033[1m\033[36m--- Welcome to TherapiBot ---\033[0m")
    print("Your cognitive counter-speaker. Ready when you are.")
    print("(Type 'exit' or 'quit' to end the session)\n")

    while True:
        try:
            user_input = input("\033[1mYou:\033[0m ")
            if user_input.lower() in ["exit", "quit"]:
                print("\n\033[36mTherapiBot:\033[0m Goodbye! Remember to be kind to yourself.")
                break
            
            if not user_input.strip():
                continue

            response_text = get_cognitive_restructuring_mock(user_input)
            
            print(f"\n\033[36mTherapiBot:\033[0m {response_text}")
            
            if ELEVENLABS_API_KEY:
                try:
                    print("\n[Generating voice with ElevenLabs]...")
                    audio = generate(
                        text=response_text,
                        voice="Bella",
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
            print("\n\n\033[36mTherapiBot:\033[0m Goodbye! Remember to be kind to yourself.")
            break

if __name__ == "__main__":
    main()
