from flask import Flask
import os

app = Flask(__name__)
app.debug = os.getenv('DEBUG', '') == 'True'

@app.route("/recent_images/<path:name>")
def recent_images(name):
    return 'Hello ' + name

if __name__ == "__main__":
    app.run()
