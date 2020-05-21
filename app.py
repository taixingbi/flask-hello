import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8442))
    app.run(ssl_context='adhoc', host='0.0.0.0', port=port)

