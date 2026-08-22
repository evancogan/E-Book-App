"""
epub_loader.py

Loads EPUB files and constructs Book + Chapter objects.

Responsibilities:
- Read EPUB file structure.
- Extract chapter contents.
- Build Book and Chapter instances.

Constraints:
- Must not render text.
- Must not handle navigation.
- Must not contain UI code.
"""


from book import Book
from chapter import Chapter
class EPUBLoader:
    def load(self, path):
        return Book("Untitled", [Chapter("Example content")])
