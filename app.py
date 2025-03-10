from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  """View for the Home page of the website."""
  return render_template("home.html")

@app.route("/about")
def about():
  """View for the About page of the website."""
  return render_template("about.html")


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=3000)