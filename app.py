from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template(
      "index.html",
      site_title="TuneIn",
      heading="Welcome to TuneIn",  # <-- Put your title here!
      status="Active",
      description="Tune in is an app that will help you create study playlists",
      highlights=["First feature or service", "Second highlight", "Third point"],
  )


if __name__ == "__main__":
  app.run()
