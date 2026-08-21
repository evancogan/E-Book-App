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
