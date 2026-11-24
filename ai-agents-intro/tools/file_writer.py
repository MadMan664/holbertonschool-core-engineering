"""Tool that saves Markdown to disk."""
from pathlib import Path


def save_markdown_file(file_path: str, content: str) -> str:
    """Write content to file_path and return the saved path or an error."""
    path = Path(file_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except OSError as error:
        return f"Error: could not save {path}: {error}"
    return str(path)
