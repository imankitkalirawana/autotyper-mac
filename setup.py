from setuptools import setup

APP = ['autotyper.py']  # Replace 'your_script.py' with the name of your Python script
DATA_FILES = []
OPTIONS = {
    'packages': ['tkinter', 'pyautogui'],  # Add 'rubicon.objc' to the list
    'includes': ['tkinter'],
    'excludes': ['rubicon'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
