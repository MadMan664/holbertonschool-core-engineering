"""Practice designer agent: creates an exercise from an explanation."""
import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

practice_designer_agent = Agent(
    name="practice_designer_agent",
    model=LiteLlm(model=os.getenv("MODEL_NAME", "ollama_chat/llama3.2:1b")),
    description="Designs a short practice exercise for a topic.",
    instruction=(
        "You are a practice designer agent. You receive a topic and the "
        "explanation already written for it. Create a short, "
        "beginner-friendly exercise based on them that takes 10 to 20 "
        "minutes. Do not rewrite the explanation and do not use Markdown "
        "headings. Return only these bold labels, each followed by its "
        "text: Exercise, Expected input, Expected output, Hints (one or "
        "two hints)."
    ),
)
