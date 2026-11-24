#!/usr/bin/env python3
"""AI Study Guide Generator."""
import asyncio
import json
import os
import sys
import urllib.request

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from tools.file_writer import save_markdown_file
from tools.validation import validate_required_sections

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "study_guide.md")


def check_config():
    """Check the environment variables, Ollama and the model."""
    load_dotenv()
    model = os.getenv("MODEL_NAME")
    if not model:
        raise RuntimeError("Missing environment variable MODEL_NAME. "
                           "Copy .env.example to .env and fill it in.")
    if not model.startswith("ollama"):
        return
    base = os.getenv("OLLAMA_API_BASE")
    if not base:
        raise RuntimeError("Missing environment variable OLLAMA_API_BASE. "
                           "Copy .env.example to .env and fill it in.")
    try:
        with urllib.request.urlopen(base.rstrip("/") + "/api/tags",
                                    timeout=5) as response:
            names = [m["name"] for m in json.load(response)["models"]]
    except OSError:
        raise RuntimeError(f"Ollama is not running at {base}. "
                           "Start it with 'ollama serve'.")
    wanted = model.split("/", 1)[1]
    if wanted not in names and wanted + ":latest" not in names:
        raise RuntimeError(f"Model '{wanted}' is not available. Run "
                           f"'ollama pull {wanted}'.")


def get_topic():
    """Read the topic from the command line or ask for it."""
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    with open(os.path.join(BASE_DIR, "data", "topic_examples.json")) as f:
        print("Example topics:", ", ".join(json.load(f)["topics"]))
    return input("Topic: ")


async def run_agent(agent, message):
    """Run one agent on a message and return its final text answer."""
    service = InMemorySessionService()
    runner = Runner(agent=agent, app_name="ai-agents-intro",
                    session_service=service)
    await service.create_session(app_name="ai-agents-intro",
                                 user_id="student", session_id="run")
    content = types.Content(role="user", parts=[types.Part(text=message)])
    answer = ""
    async for event in runner.run_async(user_id="student",
                                        session_id="run",
                                        new_message=content):
        if event.is_final_response() and event.content:
            answer = "".join(p.text or "" for p in event.content.parts)
    if not answer.strip():
        raise RuntimeError(f"{agent.name} returned an empty answer.")
    return answer.strip()


def assemble_markdown(topic, explanation, practice):
    """Build the draft guide: practice goes before Common Mistakes."""
    before, found, mistakes = explanation.partition("## Common Mistakes")
    parts = [f"# Topic: {topic}", before.strip(),
             "## Practice Exercise\n\n" + practice]
    if found:
        parts.append(found + mistakes.rstrip())
    return "\n\n".join(parts)


def assemble_final_markdown(draft, review, topic):
    """Add the review comments and the final summary to the draft."""
    summary = (f"This guide explained {topic} with key concepts, an "
               "example, a practice exercise and common mistakes, and "
               "it was checked by a reviewer.")
    return (draft + "\n\n## Review Comments\n\n" + review +
            "\n\n## Final Summary\n\n" + summary + "\n")


def main():
    """Run the workflow: explain, practice, review, validate, save."""
    try:
        check_config()
        topic = get_topic()
        if not topic.strip():
            raise ValueError("Topic cannot be empty.")
        from agents.explainer_agent import explainer_agent
        from agents.practice_designer_agent import practice_designer_agent
        from agents.reviewer_agent import reviewer_agent

        print("Running the explainer agent...")
        explanation = asyncio.run(run_agent(explainer_agent,
                                            f"Topic: {topic}"))
        print("Running the practice designer agent...")
        practice = asyncio.run(run_agent(
            practice_designer_agent,
            f"Topic: {topic}\n\nExplanation:\n{explanation}"))
        draft = assemble_markdown(topic, explanation, practice)
        print("Running the reviewer agent...")
        review = asyncio.run(run_agent(reviewer_agent, draft))
        final_markdown = assemble_final_markdown(draft, review, topic)
    except (ValueError, RuntimeError) as error:
        print(f"Error: {error}")
        return 1

    result = validate_required_sections(final_markdown)
    if not result["valid"]:
        print("Validation failed. Missing sections: " +
              ", ".join(result["missing"]))
    else:
        print("Validation passed: all required sections are present.")
    saved = save_markdown_file(OUTPUT_FILE, final_markdown)
    print(saved if saved.startswith("Error") else f"Saved to {saved}")
    return 0 if result["valid"] and not saved.startswith("Error") else 1


if __name__ == "__main__":
    sys.exit(main())
