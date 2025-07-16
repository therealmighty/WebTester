# WebTester
A simple command-line tool for basic web security header analysis and website reachability checks.

# About
WebTester is a lightweight Python script designed to help you quickly assess basic security configurations of web applications by checking for the presence of common HTTP security headers. It also includes a simple ping functionality to check website reachability. This tool is primarily for educational purposes and basic reconnaissance.

# Features
Security Header Scan: Checks for X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security, Content-Security-Policy, Referrer-Policy, Permissions-Policy, and Server headers.

Website Ping: Verifies if a given URL is reachable.

Configurable Timeout: Set a custom timeout for HTTP requests.

Interactive CLI: Simple command-line interface for easy interaction.

Clear Console: Command to clear the terminal screen.

# Installation
Clone the repository (or download the script):

git clone https://github.com/therealmighty/WebTester
cd WebTester

(Replace YOUR_USERNAME with your actual GitHub username and WebTester.git with your repository name)

# Install dependencies:
WebTester requires requests and colorama. You can install them using pip:

pip install requests colorama

# Usage
To run WebTester, navigate to the script's directory in your terminal and execute:

python web_tester.py

(Assuming you saved the script as web_tester.py)

You will be greeted with the tool's banner and a command prompt.

# Commands
Once the tool is running, you can use the following commands:

scan <URL>: Scans the specified URL for security headers.

ping <URL>: Checks if the specified URL is reachable.

timeout <seconds>: Sets the request timeout in seconds (default is 10 seconds).

help: Displays a list of all available commands and their descriptions.

about: Shows information and the disclaimer about WebTester.

version: Displays the tool's name and version.

clear: Clears the console screen.

exit: Exits the WebTester tool.

# Disclaimer
for educational purposes only, dont be an idiot and use it on random ones

# Contributing
feel free to fork and make public, but just add credit please

# License
This project is open-source and available under the MIT License.
