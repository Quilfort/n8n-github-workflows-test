def spell_name(name):
    """
    Function to spell out a name with a visual representation for each letter
    """
    print(f"Spelling out the name: {name}\n")
    
    for letter in name:
        print(f"* {letter.upper()} *")
        
        # Create a simple ASCII art for each letter
        if letter.lower() == 'q':
            print("  ####  ")
            print(" #    # ")
            print(" #    # ")
            print(" #  # # ")
            print("  #### #")
            print("        ")
        elif letter.lower() == 'u':
            print(" #    # ")
            print(" #    # ")
            print(" #    # ")
            print(" #    # ")
            print("  ####  ")
            print("        ")
        elif letter.lower() == 'i':
            print("  ####  ")
            print("   ##   ")
            print("   ##   ")
            print("   ##   ")
            print("  ####  ")
            print("        ")
        elif letter.lower() == 'l':
            print(" #      ")
            print(" #      ")
            print(" #      ")
            print(" #      ")
            print(" ###### ")
            print("        ")
        elif letter.lower() == 'f':
            print(" ###### ")
            print(" #      ")
            print(" #####  ")
            print(" #      ")
            print(" #      ")
            print("        ")
        elif letter.lower() == 'o':
            print("  ####  ")
            print(" #    # ")
            print(" #    # ")
            print(" #    # ")
            print("  ####  ")
            print("        ")
        elif letter.lower() == 'r':
            print(" #####  ")
            print(" #    # ")
            print(" #####  ")
            print(" #   #  ")
            print(" #    # ")
            print("        ")
        elif letter.lower() == 't':
            print(" ###### ")
            print("   ##   ")
            print("   ##   ")
            print("   ##   ")
            print("   ##   ")
            print("        ")
        else:
            print(" ?????  ")
            print(" ?????  ")
            print(" ?????  ")
            print(" ?????  ")
            print(" ?????  ")
            print("        ")
        
        print("\n")


if __name__ == "__main__":
    spell_name("Quilfort")