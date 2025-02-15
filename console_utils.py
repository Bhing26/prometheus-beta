import os
import platform

def clear_console_and_log(message):
    """
    Clear the console screen and then log a message.
    
    Args:
        message (str): The message to log after clearing the console.
    
    This function works across different platforms:
    - On Windows, it uses 'cls'
    - On Unix-like systems (Linux, macOS), it uses 'clear'
    """
    # Determine the operating system and use appropriate clear command
    system = platform.system().lower()
    
    try:
        # Clear the console based on the operating system
        if system == 'windows':
            os.system('cls')
        else:
            # For Unix-like systems (Linux, macOS)
            os.system('clear')
    except Exception as e:
        # Fallback if console clearing fails
        print(f"Warning: Could not clear console - {e}")
    
    # Log the message after clearing
    print(message)