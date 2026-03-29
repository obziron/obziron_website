from flask import Flask, render_template, request, redirect

app = Flask(__name__)

comments = []

@app.route("/")
def home():
    return render_template("index.html", comments=comments)

@app.route("/comment", methods=["POST"])
def comment():
    name = request.form.get("name")
    text = request.form.get("comment")

    if name and text:
        comments.append((name, text))

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

    