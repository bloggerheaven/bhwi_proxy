from flask import Flask, request, jsonify, abort
import os
import requests

app = Flask(__name__)
app.debug = os.getenv('DEBUG', '') == 'True'

def access_token():
  return os.getenv('ACCESS_TOKEN', '')

def check_user_id(user_id):
  if user_id not in os.getenv('USER_IDS', ''):
    return abort(403)

def check_user_name(user_name):
  if user_name not in os.getenv('USER_NAMES', ''):
    return abort(403)

def perform_request(path):
  r = requests.get(path)
  response = jsonify(r.json(), status=202)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

def build_recent_images_url(user_id):
  return 'https://api.instagram.com/v1/users/' + user_id + '/media/recent/?access_token=' + access_token()

def build_user_profile_url(user_id):
  return 'https://api.instagram.com/v1/users/' + user_id + '?access_token=' + access_token()

def build_media_url(user_name):
  return 'https://www.instagram.com/' + user_name + '/media/'

@app.route("/recent_images/<path:user_id>")
def recent_images(user_id):
  check_user_id(user_id)
  return perform_request(build_recent_images_url(user_id))

@app.route("/user_profile/<path:user_id>")
def user_profile(user_id):
  check_user_id(user_id)
  return perform_request(build_user_profile_url(user_id))

@app.route("/media/<path:user_name>")
def media(user_name):
  check_user_name(user_name)
  return perform_request(build_media_url(user_name))

@app.route('/healthcheck')
def healthcheck():
    return 'WORKING'

if __name__ == "__main__":
    app.run()
