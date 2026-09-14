from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Write Python logic here!
    greeting = "Hello from Python!"
    status = "Active"
    
    return f"""
    <html>
      <body style="font-family: sans-serif; text-align: center; margin-top: 80px; background: #0f172a; color: white;">
        <h1>{greeting}</h1>
        <p>Backend Status: <strong style="color: #38bdf8;">{status}</strong></p>
        <p>This entire response was generated dynamically using Python.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
