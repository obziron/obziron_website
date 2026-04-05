from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# 🔐 Secret key (safe for now, can move to env later)
app.secret_key = os.environ.get("SECRET_KEY", "defaultsecret")

# 💬 Store comments (temporary storage)
comments = []

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html", comments=comments)

# ================= ADD COMMENT =================
@app.route("/comment", methods=["POST"])
def comment():
    name = request.form.get("name")
    text = request.form.get("comment")

    if name and text:
        comments.append((name, text))

    return redirect("/")
    
@app.route("/.well-known/discord")
def discord_verification():
    return "dh=4118046e803b45e48f76fd838fe6b8bb8c9162ec"
