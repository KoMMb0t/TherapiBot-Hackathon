# Devpost Pitch: TherapiBot

**Project Name:** TherapiBot: The Cognitive Counter-Speaker

**Elevator Pitch:**
TherapiBot is a voice-driven AI companion that helps you challenge and reframe negative thoughts in real-time. Using evidence-based cognitive-behavioral techniques, it acts as your personal cognitive counter-speaker, turning moments of self-doubt into opportunities for growth. It's not just a tool; it's a mental sparring partner in your pocket.

**The Problem We Solve:**
Negative self-talk is a universal human experience. Thoughts like "I'm not good enough" or "I'll never succeed" can become debilitating, impacting our mental well-being and holding us back from our potential. While therapy is effective, it's not always accessible or available in the moment you need it most. We wanted to create a tool that could provide immediate, accessible, and personalized cognitive support, right when a negative thought strikes.

**How We Built It:**
TherapiBot is built on a powerful, modern AI stack designed for complex, agentic behavior and natural human interaction:

*   **Core Logic & Orchestration (Raindrop MCP):** At the heart of TherapiBot is the Raindrop Multi-Agent Control Platform. We use it to orchestrate a team of specialized AI agents that work in parallel:
    *   **The Analyst:** A content agent that dissects the user's statement to identify the underlying cognitive distortion (e.g., catastrophizing, black-and-white thinking).
    *   **The Empath:** A mood agent that analyzes the emotional tone of the user's voice and text to tailor the response's empathy level.
    *   **The Pacer:** A tempo agent that determines the optimal speaking rate and rhythm for the response, ensuring it feels natural and supportive.
    This multi-agent approach allows for a nuanced and context-aware response that a single monolithic model couldn't achieve.

*   **Voice Interaction (ElevenLabs):** To make the interaction feel truly human and engaging, we use the ElevenLabs Voice API. This allows TherapiBot to respond with a voice that is not only clear but also rich in emotional inflection, matching the empathetic tone determined by the Raindrop agents. It's the difference between a sterile chatbot and a compassionate companion.

*   **Inference & Backend (Python & Cerebras Cloud - Optional):** The backend is a lightweight Python application. For high-speed, low-latency inference, the system is designed to be deployed on the Cerebras Cloud, ensuring that the cognitive counter-arguments are delivered almost instantaneously.

**Challenges We Ran Into:**
One of the biggest challenges was moving beyond simple intent-based responses. We didn't want a bot that just spat out pre-canned affirmations. The goal was to generate a *cognitive counter-argument* that was both logically sound and emotionally resonant. Orchestrating the three agents (Analyst, Empath, Pacer) in Raindrop to produce a single, coherent, and helpful response required significant fine-tuning of the prompts and control logic.

Another challenge was ensuring the "cheeky but friendly" personality. The responses needed to be challenging enough to be effective but not so confrontational that they alienate the user. This was a delicate balance to strike in the prompt engineering for the content agent.

**Accomplishments We're Proud Of:**
We are incredibly proud of creating an application that feels less like a piece of software and more like a genuine interaction. The synergy between Raindrop's agentic orchestration and ElevenLabs' expressive voice synthesis creates a "WOW" factor that has to be experienced. We've successfully built a prototype that demonstrates the core functionality: it listens, it understands the underlying thought pattern, and it talks back with a supportive, intelligent counter-point.

**What We Learned:**
This project reinforced the power of multi-agent systems. By breaking down a complex task (cognitive restructuring) into smaller, specialized sub-tasks, we were able to achieve a level of sophistication that would be difficult with a single AI model. We also learned how critical high-quality voice synthesis is for applications in the mental well-being space. The emotional nuance provided by ElevenLabs is a game-changer.

**What's Next for TherapiBot:**
This is just the beginning. We envision a future where TherapiBot is a platform for a variety of cognitive wellness tools. Future plans include:

*   **Personalization:** Training the agents on a user's specific thought patterns and communication style.
*   **Integration:** Developing integrations for smart home devices (like mirrors with embedded speakers) and wearables for on-the-go support.
*   **Gamification:** Adding features to track progress and reward consistent use, turning mental wellness into an engaging journey.

**Try it Out!**
*   **GitHub Repo:** [https://github.com/KoMMb0t/TherapiBot-Hackathon](https://github.com/KoMMb0t/TherapiBot-Hackathon)
*   **Live Demo:** [Link to be added]
