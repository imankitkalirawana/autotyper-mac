import tkinter as tk
import pyautogui
import time
from threading import Thread

def start_typing():
    text_to_type = input_text.get("1.0", "end-1c")  # Get the text from the Tkinter Text widget

    # Start a new thread to handle typing on another app
    typing_thread = Thread(target=type_text_on_notepad, args=(text_to_type,))
    typing_thread.start()

def type_text_on_notepad(text):
    # Wait for a moment to give the user time to focus on the desired application
    time.sleep(5)

    # Type the text using pyautogui
    pyautogui.typewrite(text)

# Create the main Tkinter window
root = tk.Tk()
root.title("Auto Typer by Divinely Developer")
# make window to stay on top of all other windows
root.attributes('-topmost', True)
# app icons from /res/icons.ico
root.iconbitmap('res/icons.ico')
# Create a Text widget for user input
input_text = tk.Text(root, height=20, width=80)
input_text.pack(pady=10)

# Create a Start button
start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.pack()

# stop

# Run the Tkinter main loop
root.mainloop()