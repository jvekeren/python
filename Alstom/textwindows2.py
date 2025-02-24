import tkinter as tk
from tkinter import font

def apply_formatting():
    # Create a custom font with the desired size and bold style
    custom_font = font.nametofont("TkDefaultFont")
    custom_font.configure(size=14, weight="bold")

    # Configure a tag to use the custom font and specify the text color
    text_widget.tag_configure("custom_tag", font=custom_font, foreground="blue")

    # Apply the tag to a specific range of text
    text_widget.tag_add("custom_tag", "1.0", "1.11")

def close_window():
    root.destroy()


# Create a root window
root = tk.Tk()
root.title("Text Window")

root.overrideredirect(True)

# Create a Text widget with a specific number of rows and columns
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()


# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack()

# Add text to the Text widget
text_widget.insert("1.0", "Hello, this is a text window!")

# Create a button to apply formatting
formatting_button = tk.Button(root, text="Apply Formatting", command=apply_formatting)
formatting_button.pack()

close_button = tk.Button(root, text="Close Window", command=close_window)
close_button.pack()

# Start the main event loop
root.mainloop()

