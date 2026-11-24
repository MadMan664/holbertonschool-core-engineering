"""Explainer agent: explains a topic to beginners."""
import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

explainer_agent = Agent(
    name="explainer_agent",
    model=LiteLlm(model=os.getenv("MODEL_NAME", "ollama_chat/llama3.2:1b")),
    description="Explains a programming topic to beginner students.",
    instruction=(
        "You are an explainer agent for beginner programming students. "
        "You receive a programming topic. Reply in Markdown using exactly "
        "these four headings, in this order, and nothing else:\n"
        "## Simple Explanation\n"
        "(two to four short sentences)\n"
        "## Key Concepts\n"
        "(a bullet list of three to five concepts)\n"
        "## Example\n"
        "(one short, simple example in a fenced code block)\n"
        "## Common Mistakes\n"
        "(a bullet list of two or three beginner mistakes)\n"
        "Do not write a practice exercise and do not add other headings."
    ),
)
