import tkinter as tk
import pyautogui
import time
from threading import Thread

# Global variables to control the typing process
stop_typing = False
pause_typing = False

def start_typing():
    global stop_typing, pause_typing
    stop_typing = False
    pause_typing = False
    
    text_to_type = input_text.get("1.0", "end-1c")  # Get the text from the Tkinter Text widget

    # Start a new thread to handle typing on another app
    typing_thread = Thread(target=type_text_on_notepad, args=(text_to_type,))
    typing_thread.start()

def stop_typing():
    global stop_typing
    stop_typing = True

def toggle_pause_resume():
    global pause_typing
    pause_typing = not pause_typing
    button_text.set("Resume Typing" if pause_typing else "Pause Typing")

def type_text_on_notepad(text):
    global stop_typing, pause_typing
    
    # Wait for a moment to give the user time to focus on the desired application
    time.sleep(2)
    
    for char in text:
        # Check if the stop_typing flag is True, break the loop if it is
        if stop_typing:
            break
        
        # Check if the pause_typing flag is True, pause typing
        while pause_typing:
            time.sleep(0.1)  # Adjust the sleep time as needed
        
        pyautogui.typewrite(char)
        time.sleep(0.001)  # Adjust the sleep time as needed

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
start_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a Stop button
stop_button = tk.Button(root, text="Stop Typing", command=stop_typing)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a Pause/Resume button
button_text = tk.StringVar()
pause_resume_button = tk.Button(root, textvariable=button_text, command=toggle_pause_resume)
button_text.set("Pause Typing")
pause_resume_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
