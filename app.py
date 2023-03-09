from flask import Flask
from ytmusicapi import YTMusic

ytmusic = YTMusic()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/search/<query>")
def search(query):
    return   ytmusic.search(query)
