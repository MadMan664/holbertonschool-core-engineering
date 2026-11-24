# AI Agents in Python

## Description

An AI Study Guide Generator. It receives a programming topic and builds a Markdown study guide with a simple explanation, key concepts, an example, a practice exercise, common mistakes, review comments and a final summary. Three agents (explainer, practice designer, reviewer) run one after another, and two deterministic tools save and validate the result.

## Requirements

- Python 3.10 or newer
- Ollama with a small local model (default: `llama3.2:1b`)
- The packages in `requirements.txt` (Google ADK, LiteLLM, python-dotenv)

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Install Ollama (https://ollama.com), then pull the model and check that it answers:

    ollama pull llama3.2:1b
    ollama run llama3.2:1b "Say hello"

## Configuration

Copy `.env.example` to `.env`. The real `.env` is ignored by git.

    OLLAMA_API_BASE=http://localhost:11434
    MODEL_NAME=ollama_chat/llama3.2:1b

Model provider: Ollama, connected through LiteLLM (`ollama_chat/` prefix). To use another LiteLLM provider, change `MODEL_NAME` (and set that provider's API key in `.env`, never in git).

## How to Run

    python3 main.py "Python decorators"

Without an argument the program lists example topics and asks for one. The result is saved to `output/study_guide.md`.

## Example Input

    python3 main.py "Python decorators"

## Example Output

The file `output/study_guide.md` in this repository is an example of the format. Short excerpt:

    # Topic: Python decorators

    ## Simple Explanation

    A decorator is a function that takes another function and adds extra behaviour to it without changing its code.

    ## Key Concepts
    ...
    ## Final Summary
    ...

Console output:

    Running the explainer agent...
    Running the practice designer agent...
    Running the reviewer agent...
    Validation passed: all required sections are present.
    Saved to output/study_guide.md

## Project Structure

    ai-agents-intro/
    ├── agents/
    │   ├── explainer_agent.py
    │   ├── practice_designer_agent.py
    │   └── reviewer_agent.py
    ├── tools/
    │   ├── file_writer.py
    │   └── validation.py
    ├── output/
    │   └── study_guide.md
    ├── data/
    │   └── topic_examples.json
    ├── .env.example
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    └── main.py

## Agents

- Explainer Agent: explains the topic with a simple explanation, key concepts, one example and common mistakes.
- Practice Designer Agent: receives the topic and the explanation and writes a small exercise with expected input, expected output and hints.
- Reviewer Agent: reads the draft guide and returns missing information, unclear parts, suggestions and a short recommendation.

The workflow runs in order: topic, explainer, practice designer, draft, reviewer, final Markdown, validation, save.

## Tools

- `save_markdown_file(file_path, content)` in `tools/file_writer.py`: creates the folder if needed, writes the file and returns the saved path, or an error message.
- `validate_required_sections(markdown)` in `tools/validation.py`: checks that the eight required sections exist and returns whether it is valid and which sections are missing.

## Self-Validation Checklist

- [x] Project structure created
- [x] Local model set up and documented
- [x] Explainer Agent
- [x] Markdown saving tool
- [x] Validation tool
- [x] Practice Designer Agent
- [x] Reviewer Agent
- [x] Sequential workflow in `main.py`
- [x] Error handling and troubleshooting notes
- [x] README with reflection and limitations

## Troubleshooting

- `Missing environment variable ...`: copy `.env.example` to `.env`.
- `Ollama is not running at ...`: start it with `ollama serve`.
- `Model '...' is not available`: run `ollama pull <model>` or fix `MODEL_NAME`.
- `Topic cannot be empty.`: give a non-empty topic.
- `Error: could not save ...`: check the permissions of the `output/` folder.
- `Validation failed. Missing sections: ...`: the model did not use the requested headings; run it again or try a larger model.

## Reflection

- A direct LLM call sends one prompt and returns one answer. An AI agent adds a role, instructions and tools, and is placed in a workflow, so its behaviour is easier to control and test.
- The explainer explains the topic, the practice designer creates the exercise from that explanation, and the reviewer checks the draft without rewriting it.
- The file writer saves the Markdown predictably, and the validator checks the required sections. Both always behave the same way, unlike the model.
- The hardest part is making the agent prompts and the validator agree on the same section names.
- A small local model may ignore the requested headings, repeat itself or invent details, so its output can vary between runs.

## Known Limitations

- Output quality depends on the model; small local models can be inconsistent and may hallucinate details.
- The validator only checks that section headings exist, not that the content is correct.
- Generation can be slow on machines without a GPU.
- The agents run one after another, so the whole run takes the sum of the three model calls.
