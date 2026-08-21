class Renderer:
    def __init__(self, cleaner):
        self.cleaner = cleaner

    def render(self, chapter):
        if chapter.cleaned is None:
            chapter.cleaned = self.cleaner.clean(chapter.raw)
        return chapter.cleaned
