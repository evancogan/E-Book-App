"""
navigation.py

NavigationController manages chapter navigation for the E‑Book Reader.

Responsibilities:
- Track current chapter index.
- Provide next/prev/home/last/go_to_chapter.
- Notify UI via update callback.

Constraints:
- Must not render text.
- Must not contain Tkinter widgets.
- Must not parse EPUBs.
"""

class NavigationController:
    def __init__(self, book, update_callback=None):
        self.book = book
        self.update_callback = update_callback
        self.index = 0  # current chapter index

    def set_update_callback(self, fn):
        self.update_callback = fn

    def _update(self):
        if self.update_callback:
            self.update_callback()

    def next(self):
        if self.index < len(self.book.chapters) - 1:
            self.index += 1
        self._update()

    def prev(self):
        if self.index > 0:
            self.index -= 1
        self._update()

    def home(self):
        self.index = 0
        self._update()

    def last(self):
        self.index = len(self.book.chapters) - 1
        self._update()

    def go_to_chapter(self, i):
        if 0 <= i < len(self.book.chapters):
            self.index = i
        self._update()
