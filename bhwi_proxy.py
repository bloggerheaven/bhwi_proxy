from flask import Flask, request, jsonify, abort
import os
import requests

app = Flask(__name__)
app.debug = os.getenv('DEBUG', '') == 'True'

def build_url(user_id, client_id):
  return 'https://api.instagram.com/v1/users/' + user_id + '/media/recent/?client_id=' + client_id + '&callback=?'

@app.route("/recent_images/<path:user_id>")
def recent_images(user_id):
    if user_id in os.getenv('USER_IDS', ''):
      path = build_url(user_id, os.getenv('CLIENT_ID', ''))
      r = requests.get(path)
      return jsonify(results=r.json(), status=202)
    else:
      abort(403)

@app.route('/healthcheck')
def healthcheck():
    return 'WORKING'

if __name__ == "__main__":
    app.run()
