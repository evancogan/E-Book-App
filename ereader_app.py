"""
ereader_app.py

Main Tkinter UI layout for the E‑Book Reader.

Responsibilities:
- Build window, frames, navigation bar, chapter sidebar, and text display.
- Connect UI events to NavigationController.
- Use Renderer to display cleaned chapter text.

Constraints:
- Must not parse EPUBs.
- Must not store book/chapter data.
- Must not implement navigation logic.
"""


import tkinter as tk
from tkinter import BOTH, LEFT, RIGHT, X, Y, WORD, END

class EReaderApp:
    def __init__(self, book, renderer, nav_controller):
        self.book = book
        self.renderer = renderer
        self.nav = nav_controller

        # Main window
        self.root = tk.Tk()
        self.root.title("E‑Book Reader")
        self.root.geometry("800x600")

        # ============================
        # TOP NAVIGATION BAR
        # ============================
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(fill=X, padx=20, pady=10)

        tk.Button(nav_frame, text="Prev", command=self.nav.prev).pack(side=LEFT, padx=5)
        tk.Button(nav_frame, text="Next", command=self.nav.next).pack(side=LEFT, padx=5)
        tk.Button(nav_frame, text="Home", command=self.nav.home).pack(side=LEFT, padx=5)
        tk.Button(nav_frame, text="Last", command=self.nav.last).pack(side=LEFT, padx=5)

        # ============================
        # LEFT CHAPTER LIST
        # ============================
        chapter_frame = tk.Frame(self.root)
        chapter_frame.pack(side=LEFT, fill=Y)

        for i, chapter in enumerate(self.book.chapters):
            tk.Button(
                chapter_frame,
                text=f"Chapter {i+1}",
                command=lambda i=i: self.nav.go_to_chapter(i)
            ).pack(fill=X)

        # ============================
        # MAIN TEXT DISPLAY AREA
        # ============================
        self.display = tk.Text(self.root, wrap=WORD)
        self.display.pack(expand=True, fill=BOTH)

        # Give the nav controller access to update the display
        self.nav.set_update_callback(self.update_display)

        # Initial render
        self.update_display()

    # Called by NavigationController
    def update_display(self):
        chapter = self.book.chapters[self.nav.index]
        cleaned = self.renderer.render(chapter)

        self.display.delete("1.0", END)
        self.display.insert(END, cleaned)

    def run(self):
        self.root.mainloop()
