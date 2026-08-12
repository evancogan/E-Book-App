import tkinter as tk

HOME_PAGE = -1

def on_prev():
    global current_page
    if current_page == HOME_PAGE:
        return
    if current_page > 0:
        current_page -= 1
    else:
        current_page = HOME_PAGE
    display_page()

def on_next():
    global current_page
    if current_page == HOME_PAGE and paragraphs:
        current_page = 0
    elif current_page < len(paragraphs) - 1:
        current_page += 1
    display_page()

def go_last():
    global current_page
    current_page = len(paragraphs) - 1
    display_page()

def go_home():
    global current_page
    current_page = HOME_PAGE
    display_page()

def go_to_chapter(chapter):
    global current_page
    if chapter >= 0 and chapter < len(paragraphs):
        current_page = chapter
    else:
        current_page = HOME_PAGE
    display_page()

def display_page():
    text_widget.delete(1.0, tk.END)

    if current_page == HOME_PAGE:
        home_frame.pack()
        prev_button.config(state=tk.DISABLED)
        next_button.config(state=tk.NORMAL if paragraphs else tk.DISABLED)
        page_label.config(text="Page: ")
        for i, button in enumerate(chapter_buttons):
            button.config(text=f"Chapter {i+1}", command=lambda i=i: go_to_chapter(i))
    else:
        home_frame.pack_forget()
        page_label.config(text=f"Page: {current_page + 1}/{len(paragraphs)}")
        text_widget.insert(tk.END, paragraphs[current_page])
        prev_button.config(state=tk.NORMAL)
        next_button.config(state=tk.NORMAL if current_page < len(paragraphs) - 1 else tk.DISABLED)

    chapter_buttons[current_page].config(relief='sunken')
# Initialize variables
paragraphs = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
]
current_page = HOME_PAGE

# Create the main window
root = tk.Tk()
root.title("E-Reader App")

# Create a centered control bar for the navigation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons
prev_button = tk.Button(button_frame, text="Prev", command=on_prev)
home_button = tk.Button(button_frame, text="Home", command=go_home)
next_button = tk.Button(button_frame, text="Next", command=on_next)
last_button = tk.Button(button_frame, text="Last", command=go_last)

# Pack the buttons in the correct order
home_button.pack(side=tk.LEFT, padx=10)
prev_button.pack(side=tk.LEFT, padx=10)
next_button.pack(side=tk.LEFT, padx=10)
last_button.pack(side=tk.LEFT, padx=10)

# Add a Text widget to display fake text
text_widget = tk.Text(root, height=20, width=50)
text_widget.pack(pady=20)

# Page label
page_label = tk.Label(root, text="Page: ")
page_label.pack()

# Home page frame
home_frame = tk.Frame(root)
chapter_frame = tk.Frame(root)
chapter_frame.pack(side=tk.TOP, pady=10)

chapter_buttons = []
for i in range(len(paragraphs)):
    btn = tk.Button(chapter_frame, text=f"Chapter {i+1}", command=lambda i=i: go_to_chapter(i))
    btn.config(relief='sunken')
    btn.pack(side=tk.LEFT, padx=5)
    chapter_buttons.append(btn)

display_page()

root.mainloop()