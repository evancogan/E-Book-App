import tkinter as tk

class EReaderApp:
    def __init__(self, book, renderer, nav):
        self.root = tk.Tk()
        self.book = book
        self.renderer = renderer
        self.nav = nav
        self.text = tk.Text(self.root)

    def update_display(self):
        chapter = self.book.get_current()
        text = self.renderer.render(chapter)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, text)

    def run(self):
        self.text.pack()
        self.update_display()
        self.root.mainloop()
