"""
renderer.py

Converts Chapter objects into display-ready text.

Responsibilities:
- Apply HTMLCleaner.
- Prepare text for the UI display widget.

Constraints:
- Must not contain Tkinter/UI code.
- Must not handle navigation.
- Must not load EPUBs.
"""

class Renderer:
    def __init__(self, cleaner):
        self.cleaner = cleaner

    def render(self, chapter):
        if chapter.cleaned is None:
            chapter.cleaned = self.cleaner.clean(chapter.raw)
        return chapter.cleaned
