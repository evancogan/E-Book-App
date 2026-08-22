"""
app.py

Entry point for the E‑Book Reader application.

Responsibilities:
- Initialize loader, renderer, navigation controller, and UI.
- Wire components together and start the Tk mainloop.

Constraints:
- Must not contain UI layout code.
- Must not contain business logic or model classes.
- Must not parse EPUB files directly.
"""


from epub_loader import EPUBLoader
from html_cleaner import HTMLCleaner
from renderer import Renderer
from navigation import NavigationController
from ereader_app import EReaderApp
from chapter import Chapter

loader = EPUBLoader()
book = loader.load("example.epub")
cleaner = HTMLCleaner()
renderer = Renderer(cleaner)

def update():
    app.update_display()

nav = NavigationController(book, update)
app = EReaderApp(book, renderer, nav)
app.run()