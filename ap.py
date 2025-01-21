from flask import Flask, request, make_response, redirect, render_template_string
import base64

app = Flask(__name__)

# Hardcoded credentials for simplicity
USERNAME = "admin"
PASSWORD = "admin"
FLAG = "CTF{c00k13_m0n5t3r_ftw}"

@app.route("/")
def home():
    return """
    <h1>Welcome to the Cookie Monster Challenge!</h1>
    <p><a href="/login">Login</a></p>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            # Set a Base64-encoded cookie to indicate the user is logged in (but not admin)
            resp = make_response(redirect("/dashboard"))
            resp.set_cookie("is_admin", base64.b64encode(b"0").decode())  # Encode "0" as Base64
            return resp
        else:
            return "Invalid credentials. <a href='/login'>Try again</a>"
    return """
    <h1>Login</h1>
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    """

@app.route("/dashboard")
def dashboard():
    # Check if the user is an admin by decoding the Base64 cookie
    is_admin_encoded = request.cookies.get("is_admin", "")
    try:
        is_admin = base64.b64decode(is_admin_encoded).decode()  # Decode the cookie
    except:
        is_admin = "0"  # Default to non-admin if decoding fails

    if is_admin == "1":
        return """
        <h1>Admin Dashboard</h1>
        <p>Here are the pictures:</p>
        <img src="/static/image1.jpg" alt="Image 1">
        <img src="/static/image2.jpg" alt="Image 2">
        <img src="/static/image3.jpg" alt="Image 3">
        <p>One of these images contains the flag in its metadata. Use a tool like ExifTool to extract it.</p>
        """
    else:
        return "<h1>Dashboard</h1><p>You are not an admin. <a href='/login'>Login</a></p>"

if __name__ == "__main__":
    app.run(debug=True)