from flask import Flask
import os

app = Flask(__name__)
app.debug = os.getenv('DEBUG', '') == 'True'

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
