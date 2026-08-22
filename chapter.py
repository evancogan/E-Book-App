"""
chapter.py

Chapter model representing a single chapter's raw content.

Responsibilities:
- Store raw XHTML/text.
- Optionally store cleaned/processed text.

Constraints:
- Must not contain navigation logic.
- Must not contain Tkinter/UI code.
- Must not parse EPUB files.
"""


class Chapter:
    def __init__(self, raw):
        self.raw = raw
        self.cleaned = None
