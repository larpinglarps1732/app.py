from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "replace_with_random_secret"

# Hardcoded credentials
USERNAME = "rat"
PASSWORD = "tools"

# Templates
login_page = """
<!doctype html>
<title>Login Page Multi Tool</title>
<h2>Login</h2>
{% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
<form method="post">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
"""

menu_page = """
<!doctype html>
<title>Main Menu</title>
<h2>Welcome to The Main Menu Multi Tool</h2>
<ul>
  <li><a href="{{ url_for('tool371') }}">Tool371 (Google Drive)</a></li>
  <li><a href="{{ url_for('notepad') }}">Notepad</a></li>
  <li><a href="{{ url_for('logout') }}">Logout</a></li>
</ul>
"""

tool371_page = """
<!doctype html>
<title>Tool371</title>
<h2>Tool371</h2>
<p>Choose an option:</p>
<ul>
  <li><a href="{{ drive_link }}" target="_blank">Open Google Drive file</a></li>
  <li><a href="{{ url_for('menu') }}">Return to main menu</a></li>
</ul>
"""

notepad_page = """
<!doctype html>
<title>Notepad</title>
<h2>Notepad</h2>
<form method="post">
  <textarea name="content" rows="20" cols="80">{{ content }}</textarea><br><br>
  <input type="submit" value="Save">
</form>
<p><a href="{{ url_for('menu') }}">Return to main menu</a></p>
{% if saved %}<p style="color:green;">Content saved!</p>{% endif %}
"""

# Simple in-memory storage for Notepad content
notepad_content = ""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('menu'))
        else:
            error = "Invalid username or password"
    return render_template_string(login_page, error=error)

@app.route("/menu")
def menu():
    return render_template_string(menu_page)

@app.route("/tool371")
def tool371():
    drive_link = "https://drive.google.com/drive/folders/1U4q-MciRfo9LSxTGEvOp4m6O6MBcH9X9"
    return render_template_string(tool371_page, drive_link=drive_link)

@app.route("/notepad", methods=["GET", "POST"])
def notepad():
    global notepad_content
    saved = False
    if request.method == "POST":
        notepad_content = request.form.get("content")
        saved = True
    return render_template_string(notepad_page, content=notepad_content, saved=saved)

@app.route("/logout")
def logout():
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
