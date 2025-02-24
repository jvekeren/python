import tkinter as tk

def clear_text():
    text_widget.delete(1.0, tk.END)

def change_background_color(color):
    text_widget.configure(bg=color)

def change_font_size(size):
    text_widget.configure(font=("Arial", size))

def change_font_to_bold():
    # Create a font with the "bold" style
    bold_font = font.nametofont("TkDefaultFont")
    bold_font.configure(weight="bold")
    text_widget.configure(font=bold_font)

# Create a root window
root = tk.Tk()
root.title("Text Window")

# Create a text widget
text_widget = tk.Text(root)
text_widget.pack()

# Add text to the text widget
text_widget.insert("1.0", "Hello, this is a text window!")
change_background_color('red')
change_font_size(20)
change_font_to_bold()

#clear_text()

# clear_button = tk.Button(root, text="Clear Text", command=clear_text)
# clear_button.pack()

# text_widget.delete(1.0, tk.END)

# Start the main event loop
root.mainloop()
