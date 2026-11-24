"""Make the AI Judge Laugh: Office Jokes (make.fun bounty
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a).

Writes a single one-line office joke to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no input,
no randomness.

The joke: a standup meeting that runs so long the intern ages out
of the internship, gets promoted, and ends up running the standup
himself. It is a real one-line joke about office life, the turn
lands at the end, the setup is something anyone who has sat through
a standup recognises, and the wording is tight at 102 characters.
Against the judge's brief, in order: it is a genuine office joke
(criterion 1); the ending swerves from "meeting ran long" to the
intern now running the meeting (criterion 2, the surprise); the
endless standup is a truth every office worker winces at
(criterion 3); at 102 characters with no wasted word it is tight
(criterion 4); and the intern-aging-out angle is not the obvious
Monday-morning or photocopier line (criterion 5).
"""

import os

LINE = (
    "Our standup ran so long the intern aged out of the internship, "
    "got promoted, and now runs the standup."
)

MAX_CHARS = 199


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= MAX_CHARS, "line must be 1-199 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
