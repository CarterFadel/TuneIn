from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Write your Python variables and logic here!
    return render_template(
        "index.html",
        site_title="TuneIn",
        heading="Welcome to TuneIn",
        status="Backend Online",
        description="This site is running live on Python and Flask, served through GitHub and Render.",
        highlights=[
            "Dynamic data powered by Python",
            "Automatic deployment on every commit",
            "Clean dark-mode interface"
        ]
    )

if __name__ == "__main__":
    app.run()
