import requests
from urllib.parse import urlparse
from colorama import Fore, init
import os # Import the os module for clearing the screen

# --- Tool Information ---
NAME = "WebTester"
VERSION = "0.1"
# ------------------------

# ANSI escape codes for colors (using Colorama)
# No need to define BLUE and RESET explicitly here, Fore.BLUE and Fore.RESET are used directly.

def check_security_headers(url):
    """
    Checks a given URL for the presence of common security headers.

    Args:
        url (str): The URL of the website to check.

    Returns:
        dict: A dictionary containing the status of each security header.
    """
    results = {
        "X-Frame-Options": {"present": False, "value": None, "description": "Prevents clickjacking attacks."},
        "X-Content-Type-Options": {"present": False, "value": None, "description": "Prevents MIME-sniffing attacks."},
        "Strict-Transport-Security": {"present": False, "value": None, "description": "Enforces HTTPS connections."},
        "Content-Security-Policy": {"present": False, "value": None, "description": "Mitigates cross-site scripting (XSS) and data injection attacks."},
        "Referrer-Policy": {"present": False, "value": None, "description": "Controls how much referrer information is sent with requests."},
        "Permissions-Policy": {"present": False, "value": None, "description": "Allows or disallows the use of browser features."},
        "Server": {"present": True, "value": None, "description": "Server software information (can sometimes reveal version for potential exploits)."}
    }

    try:
        # Ensure the URL has a scheme
        if not urlparse(url).scheme:
            url = "http://" + url # Default to http if no scheme is provided

        print(f"Attempting to connect to: {url}")
        response = requests.get(url, timeout=10) # Set a timeout for the request
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        headers = response.headers

        print(f"\n--- Headers for {url} ---")
        for header, value in headers.items():
            print(f"{header}: {value}")
        print("--------------------------\n")

        for header_name in results.keys():
            if header_name in headers:
                results[header_name]["present"] = True
                results[header_name]["value"] = headers[header_name]

        print("--- Security Header Scan Results ---")
        for header, data in results.items():
            status = "Present" if data["present"] else "Missing"
            value_info = f" (Value: {data['value']})" if data["value"] else ""
            print(f"- {header}: {status}{value_info} - {data['description']}")

        # Basic check for server banner (often reveals server software and version)
        if 'Server' in headers:
            results['Server']['value'] = headers['Server']
        else:
            results['Server']['present'] = False

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return results

def display_help():
    """
    Displays a list of available commands and their descriptions.
    """
    print("\n--- Available Commands ---")
    print("  scan <URL>  : Scans the specified URL for security headers.")
    print("  help        : Displays this help message.")
    print("  about       : Shows information and disclaimer about WebTester.")
    print("  version     : Displays the tool's name and version.")
    print("  clear       : Clears the console screen.")
    print("  exit        : Exits the WebTester tool.")
    print("--------------------------\n")

def display_about():
    """
    Displays information and disclaimer about the WebTester tool.
    """
    print("\n--- About WebTester ---")
    print("WebTester is a basic Python tool for educational purposes.")
    print("It checks for the presence of common HTTP security headers on websites.")
    print("\nDisclaimer: This is a very basic script for educational purposes.")
    print("It only checks for the presence of certain HTTP security headers.")
    print("A real vulnerability scanner is far more complex and requires ethical considerations.")
    print("Always ensure you have explicit permission before scanning any website.")
    print("-----------------------\n")

def display_version():
    """
    Displays the tool's name and version.
    """
    # Fixed: Apply Fore.BLUE to the entire line for consistent coloring
    print(f"{Fore.BLUE}+----------+{Fore.RESET}")
    print(f"{Fore.BLUE}| WebTester|{Fore.RESET}")
    print(f"{Fore.BLUE}+----------+{Fore.RESET}")
    print(f"       v{VERSION}\n")

def clear_screen():
    """
    Clears the console screen.
    """
    # For Windows, use 'cls'; for Linux/macOS, use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    init() # Initialize Colorama for cross-platform compatibility

    # Display initial banner
    display_version()
    print("Type 'help' for a list of commands.\n")

    while True:
        command_input = input("Enter Command: ").strip().lower()
        parts = command_input.split(maxsplit=1) # Split into command and argument

        if not parts:
            continue # Empty input

        command = parts[0]

        if command == "scan":
            if len(parts) > 1:
                target_url = parts[1]
                check_security_headers(target_url)
            else:
                print(f"{Fore.RED}Error:{Fore.RESET} Please provide a URL to scan. Usage: scan <URL>")
        elif command == "help":
            display_help()
        elif command == "about":
            display_about()
        elif command == "version":
            display_version()
        elif command == "clear":
            clear_screen()
        elif command == "exit":
            print("Exiting WebTester. Goodbye!")
            break
        else:
            print(f"{Fore.YELLOW}Unknown command: '{command}'. Type 'help' for a list of commands.{Fore.RESET}")