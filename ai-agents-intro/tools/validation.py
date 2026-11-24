"""Tool that checks a study guide has every required section."""
import re

REQUIRED_SECTIONS = [
    "Topic",
    "Simple Explanation",
    "Key Concepts",
    "Example",
    "Practice Exercise",
    "Common Mistakes",
    "Review Comments",
    "Final Summary",
]


def validate_required_sections(markdown: str) -> dict:
    """Return the validation status and the list of missing sections."""
    missing = [
        section for section in REQUIRED_SECTIONS
        if not re.search(r"^\s*#*\s*" + re.escape(section), markdown,
                         re.IGNORECASE | re.MULTILINE)
    ]
    return {
        "valid": not missing,
        "is_valid": not missing,
        "missing": missing,
        "missing_sections": missing,
    }
