"""
widgets.py

Reusable Tkinter widgets for the E‑Book Reader.

Responsibilities:
- Provide custom UI components (if needed).

Constraints:
- Must not contain business logic.
- Must not parse EPUBs.
- Must not handle navigation.
"""

import tkinter as tk

def create_nav_buttons(frame):
    return (
        tk.Button(frame, text="Prev"),
        tk.Button(frame, text="Home"),
        tk.Button(frame, text="Next"),
        tk.Button(frame, text="Last"),
    )

def create_text_area(root):
    return tk.Text(root)

def create_chapter_buttons(frame, book, callback):
    buttons = []
    for i in range(len(book.chapters)):
        btn = tk.Button(frame, text=f"{i+1}", command=lambda i=i: callback(i))
        buttons.append(btn)
    return buttons
