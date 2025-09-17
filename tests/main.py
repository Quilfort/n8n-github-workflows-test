"""
Cool Name Speller 3000 - Main Module
Interactive ASCII art name spelling program
"""

import sys
import time
import random
from ascii_art import get_ascii_art
from utils import (
    Colors, clear_screen, typewriter_effect, 
    play_beep, rainbow_text, animated_letter_reveal
)

def spell_name_cool(name, style='rainbow'):
    """
    Super cool function to spell out a name with animations, colors, and effects
    """
    clear_screen()
    
    # Cool title with animation
    title = f"✨ SPELLING THE LEGENDARY NAME: {name.upper()} ✨"
    print("\n" + "="*60)
    if style == 'rainbow':
        print(rainbow_text(title.center(60)))
    else:
        print(Colors.BOLD + Colors.HEADER + title.center(60) + Colors.ENDC)
    print("="*60 + "\n")
    
    time.sleep(1)
    
    # Get color sequence
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA, Colors.PURPLE]
    
    for i, letter in enumerate(name):
        if letter == ' ':
            print("\n" + Colors.OKCYAN + "SPACE!" + Colors.ENDC + "\n")
            time.sleep(0.5)
            continue
            
        # Play sound effect
        play_beep()
        
        # Letter announcement with style
        color = colors[i % len(colors)]
        announcement = f"✦ Letter #{i+1}: '{letter.upper()}' ✦"
        
        if style == 'typewriter':
            typewriter_effect(announcement, 0.1, color)
        else:
            print(color + Colors.BOLD + announcement.center(40) + Colors.ENDC)
        
        print()
        
        # Get ASCII art and animate it
        art_lines = get_ascii_art(letter)
        animated_letter_reveal(art_lines, color)
        
        # Cool separator with sparkles
        sparkles = "".join(random.choice("✨⭐🌟💫⚡") for _ in range(10))
        print(Colors.YELLOW + sparkles.center(40) + Colors.ENDC)
        print()
        
        # Pause for dramatic effect
        time.sleep(0.8)
    
    # Grand finale
    print("\n" + "="*60)
    finale_text = f"🎉 COMPLETE! You've spelled: {name.upper()} 🎉"
    print(rainbow_text(finale_text.center(60)))
    print("="*60 + "\n")
    
    # Victory sound sequence
    for _ in range(3):
        play_beep()
        time.sleep(0.2)

def interactive_mode():
    """Interactive mode for user input"""
    clear_screen()
    
    print(Colors.BOLD + Colors.HEADER + """
    ╔══════════════════════════════════════╗
    ║        COOL NAME SPELLER 3000        ║
    ║         ASCII Art Edition            ║
    ╚══════════════════════════════════════╝
    """ + Colors.ENDC)
    
    print(Colors.OKCYAN + "Choose your style:" + Colors.ENDC)
    print("1. Rainbow mode (default)")
    print("2. Typewriter mode")
    print("3. Classic mode")
    
    style_choice = input(Colors.YELLOW + "\nEnter style (1-3): " + Colors.ENDC).strip()
    style_map = {'1': 'rainbow', '2': 'typewriter', '3': 'classic'}
    style = style_map.get(style_choice, 'rainbow')
    
    while True:
        name = input(Colors.GREEN + "\nEnter a name to spell (or 'quit' to exit): " + Colors.ENDC).strip()
        
        if name.lower() in ['quit', 'exit', 'q']:
            print(Colors.PURPLE + "Thanks for using Cool Name Speller 3000! 🚀" + Colors.ENDC)
            break
        
        if name:
            spell_name_cool(name, style)
            input(Colors.CYAN + "\nPress Enter to spell another name..." + Colors.ENDC)
        else:
            print(Colors.FAIL + "Please enter a valid name!" + Colors.ENDC)

if __name__ == "__main__":
    try:
        # Check if name provided as command line argument
        if len(sys.argv) > 1:
            name = " ".join(sys.argv[1:])
            spell_name_cool(name)
        else:
            # Demo with "Quilfort" then interactive mode
            print(Colors.BOLD + "🎬 Demo Mode: Spelling 'Quilfort' 🎬" + Colors.ENDC)
            time.sleep(2)
            spell_name_cool("Quilfort")
            
            input(Colors.CYAN + "\nPress Enter to enter interactive mode..." + Colors.ENDC)
            interactive_mode()
    except KeyboardInterrupt:
        print(Colors.YELLOW + "\n\n👋 Goodbye! Thanks for using Cool Name Speller 3000!" + Colors.ENDC)
    except Exception as e:
        print(Colors.FAIL + f"\n❌ An error occurred: {e}" + Colors.ENDC)