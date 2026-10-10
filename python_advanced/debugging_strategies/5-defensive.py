#!/usr/bin/env python3
"""
Lab: Defensive debugging and validation.

Goal: compute average score from user-provided text, rejecting invalid
input early with clear error messages.
"""


def parse_scores_csv(scores_text):
    """Parse comma-separated scores (whole numbers 0-100) into a list."""
    if not isinstance(scores_text, str) or not scores_text.strip():
        raise ValueError("scores text must be a non-empty string")

    scores = []
    for position, part in enumerate(scores_text.split(","), start=1):
        token = part.strip()
        try:
            score = int(token)
        except ValueError:
            raise ValueError(
                "score #{} is not a whole number: {!r}".format(position,
                                                               token)
            ) from None
        if not 0 <= score <= 100:
            raise ValueError(
                "score #{} is out of range 0-100: {}".format(position, score)
            )
        scores.append(score)
    return scores


def average_score(scores):
    """Return arithmetic mean of a non-empty score list."""
    if not scores:
        raise ValueError("cannot average an empty list of scores")
    return sum(scores) / len(scores)


def score_band(avg):
    """Classify average score into a textual band."""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


def evaluate_scores(scores_text):
    """Return (average, band) from comma-separated score text."""
    scores = parse_scores_csv(scores_text)
    avg = round(average_score(scores), 2)
    return avg, score_band(avg)


def main():
    samples = [
        "90,85,100",
        "90,85,invalid,100",
        "",
        "90,,100",
        "90,150,80",
    ]
    for scores_text in samples:
        print("Input:", repr(scores_text))
        try:
            avg, band = evaluate_scores(scores_text)
        except ValueError as error:
            print("Error:", error)
        else:
            print("Average:", avg)
            print("Band:", band)


if __name__ == "__main__":
    main()
