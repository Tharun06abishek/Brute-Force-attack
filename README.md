Brute Force Login Script

This repository contains a simple Python-based brute force login tool designed for educational and ethical penetration testing.
It demonstrates how attackers might attempt to guess passwords using automated login attempts, and how developers can understand these risks.

⚠ Use this script only on systems you own or have explicit permission to test. Unauthorized use is illegal.

🚀 Features

Attempts login on:

Custom web login forms

DVWA (Damn Vulnerable Web Application) login page structure

Supports HTTP POST login brute forcing

Can be used with custom username and password wordlist

Automatically handles sessions via requests.Session()

Includes helper function to fetch CSRF tokens (if needed)

📂 Project Structure
.
├── brute_force.py      # Main brute force script
└── passwords.txt       # Wordlist (provide your own)

🛠️ Requirements

Install dependencies:

pip install requests beautifulsoup4

▶️ How to Use

Run the script:

python3 brute_force.py


You will be prompted for:

Target URL of the login page

Username to brute force

Make sure you have a passwords.txt file in the same directory.

Example:

Enter url to scan: http://localhost/dvwa/login.php
Enter username to brute force: admin

📌 How It Works
1. Loads Password Wordlist

Reads passwords from passwords.txt one by one.

2. Sends Login Attempts

Tries both:

Custom login

DVWA-style login (with CSRF token logic available in code)

3. Checks for Success

Success is detected by responses containing:

"Login Successful"

"Welcome"

"Welcome to the password protected area"

"You have logged in as"