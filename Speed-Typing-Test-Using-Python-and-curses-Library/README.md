# Speed-Typing-Test-Using-Python-and-curses-Library

This is a command-line program that tests a user's typing speed by asking them to type out a random line of text. It uses the curses library to create a user interface in the terminal.

# How to Use
1. Clone the repository onto your computer.
2. Make sure you have Python 3 and the curses library installed.
3. Run the main.py file in your terminal by navigating to the cloned repository and typing python3 main.py.
4. The program will display a welcome screen. Press any key to begin.
5. A random line of text will be displayed on the screen. Type out the text as quickly and accurately as you can.
6. Once you have typed out the entire line, the program will display your words per minute (WPM).
7. Press any key to continue to the next line of text.
8. You can exit the program at any time by pressing the escape key.

# How it Works

The program uses the curses library to create a terminal-based user interface. When the program is run, it first displays a welcome screen that prompts the user to press any key to begin.

Once the user presses a key, the program selects a random line of text from a text file and displays it on the screen. The user is then prompted to type out the text as quickly and accurately as they can.

As the user types, the program displays the text they have entered so far in green, and any incorrect characters in red. It also displays the current words per minute (WPM) based on the user's typing speed.

Once the user has typed out the entire line of text, the program displays their final WPM and prompts them to press any key to continue to the next line of text.

If the user wants to exit the program at any time, they can press the escape key.

# The Concept Is Used-

1. File I/O: The program reads in a text file to select a random line of text for the user to type.

2. Libraries: The program uses the curses library to create a user interface in the terminal.

3. Randomness: The program selects a random line of text from the text file for the user to type.

4. Time and Timing: The program measures the user's typing speed by calculating their words per minute (WPM) based on the time it takes them to type the line of text.

5. User Input: The program captures the user's keystrokes as they type out the line of text.

6. Control Flow: The program uses loops and conditionals to control the flow of the program and determine when to exit.
