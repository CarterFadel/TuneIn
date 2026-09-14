from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template(
      "index.html",
      site_title="Your Tab Name",
      heading="Your Main Title Here",  # <-- Put your title here!
      status="Active",
      description="Your subtitle or description goes here.",
      highlights=["First feature or service", "Second highlight", "Third point"],
  )


if __name__ == "__main__":
  app.run()
