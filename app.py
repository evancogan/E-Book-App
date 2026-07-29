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


def display_page():
    text_widget.delete(1.0, tk.END)

    if current_page == HOME_PAGE:
        text_widget.insert(tk.END, "Home Page\n\nWelcome to the Book App.\nClick Next to start reading.")
        prev_button.config(state=tk.DISABLED)
        next_button.config(state=tk.NORMAL if paragraphs else tk.DISABLED)
        page_label.config(text="Page: ")
    else:
        page_label.config(text=f"Page: {current_page + 1}/{len(paragraphs)}")
        text_widget.insert(tk.END, paragraphs[current_page])
        prev_button.config(state=tk.NORMAL)
        next_button.config(state=tk.NORMAL if current_page < len(paragraphs) - 1 else tk.DISABLED)


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

# Create buttons
prev_button = tk.Button(root, text="Prev", command=on_prev)
next_button = tk.Button(root, text="Next", command=on_next)
home_button = tk.Button(root, text="Home", command=go_home)

prev_button.pack(side=tk.LEFT, padx=10)
last_button = tk.Button(root, text="Last", command=go_last)
last_button.pack(side=tk.LEFT, padx=10)
home_button.pack(side=tk.LEFT, padx=10)
next_button.pack(side=tk.RIGHT, padx=10)

# Add a Text widget to display fake text
text_widget = tk.Text(root, height=20, width=50)
text_widget.pack(pady=20)

# Page label
page_label = tk.Label(root, text="Page: ")
page_label.pack()

display_page()

root.mainloop()