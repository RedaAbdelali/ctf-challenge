# ctf-challenge : flag_command
### Challenge Description:

"In the depths of the system lies a hidden payload, waiting to be uncovered. Many have tried to find it, but few have succeeded. The key to your success lies in the shadows—look beyond the obvious, for the hidden payload is concealed in plain sight. Only those who can see the unseen and hear the silent whispers shall prevail."

#### Hints

    Hint 1: "Sometimes, the key to unlocking the next step lies in the small, often overlooked details stored in your browser."

    Hint 2: "The treasure is locked away, but the system’s tools can be turned against it."

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
- Build and Run the Docker Container :
``
    docker build -t flag_command .
    docker run -p 5000:5000 flag_command
``
- Run the Flask Application Locally:
``
    python app.py
``
- Access the Challenge:
        Open your browser and navigate to http://127.0.0.1:5000.

#### Challenge Walkthrough:
**Step 1: Log In**

    Use the credentials admin:admin to log in.

**Step 2: Inspect the Session Cookie**

    Use browser developer tools to inspect the session cookie.

    The session cookie is a base64 string of the session data (e.g., {"role": "user"} → eyJyb2xlIjogInVzZXIifQ==).

Step 3: Decode the Session Cookie

Step 4: Forge a Session Cookie

    Encode {"role": "admin"} as a base64 string to generate a valid session cookie.

    Replace the original session cookie with the forged one using browser developer tools.

Step 5: Access the Admin Page

    With the forged session cookie, navigate to the gallery page.

Step 6: Exploit Command Injection

    Use the file upload feature to inject a command and retrieve the flag:
``
    cat flag
``
Step 7: Retrieve the Flag

    The server will return the flag:

    DEFENSYS{c00k13_m4n1pul4t10n_4nd_c0mm4nd_1nj3ct10n}
