from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World from Railway! by Pigle Wow~ 한글도 잘 보이려나?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
