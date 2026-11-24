"""Reviewer agent: reviews a draft study guide."""
import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

reviewer_agent = Agent(
    name="reviewer_agent",
    model=LiteLlm(model=os.getenv("MODEL_NAME", "ollama_chat/llama3.2:1b")),
    description="Reviews a draft study guide and comments on it.",
    instruction=(
        "You are a reviewer agent. You receive a draft study guide. Review "
        "it for clarity, completeness and usefulness. Do not rewrite the "
        "guide and do not use Markdown headings. Return a short, specific "
        "review with these bold labels, each followed by its text: Missing "
        "information, Unclear parts, Suggestions, Recommendation (Approve "
        "or Revise, with one sentence of reason)."
    ),
)
