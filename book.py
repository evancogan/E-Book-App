class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters
        self.current = 0

    def get_current(self):
        return self.chapters[self.current]

    def next(self):
        if self.current < len(self.chapters) - 1:
            self.current += 1

    def prev(self):
        if self.current > 0:
            self.current -= 1
