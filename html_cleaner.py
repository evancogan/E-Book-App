"""
html_cleaner.py

Cleans and converts raw XHTML/HTML into readable text.

Responsibilities:
- Strip tags.
- Normalize whitespace.
- Convert basic formatting.

Constraints:
- Must not contain Tkinter/UI code.
- Must not handle navigation.
- Must not load EPUBs.
"""


class HTMLCleaner:
    def clean(self, html):
        return html  # minimal placeholder behavior
