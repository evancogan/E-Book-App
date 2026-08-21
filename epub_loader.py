
from book import Book
from chapter import Chapter
class EPUBLoader:
    def load(self, path):
        return Book("Untitled", [Chapter("Example content")])
