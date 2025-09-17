"""
Utility module for the Cool Name Speller 3000
Contains color definitions and helper functions
"""

import os
import time
import random

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Extended colors
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.05, color=Colors.OKGREEN):
    """Print text with typewriter effect"""
    for char in text:
        print(color + char + Colors.ENDC, end='', flush=True)
        time.sleep(delay)
    print()

def play_beep():
    """Play a beep sound (cross-platform)"""
    try:
        if os.name == 'nt':  # Windows
            import winsound
            winsound.Beep(800, 200)
        else:  # Unix/Linux/Mac
            print('\a', end='', flush=True)
    except:
        pass  # Silent fail if sound doesn't work

def rainbow_text(text):
    """Return text with rainbow colors"""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char + Colors.ENDC
    return result

def animated_letter_reveal(lines, color):
    """Animate the letter appearing line by line"""
    for line in lines:
        print(color + line + Colors.ENDC)
        time.sleep(0.1)
