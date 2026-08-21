class NavigationController:
    def __init__(self, book, update):
        self.book = book
        self.update = update

    def next(self):
        self.book.next()
        self.update()

    def prev(self):
        self.book.prev()
        self.update()
