from flask import Flask, request
import threading
from downloader.download import download

app = Flask(__name__)

base_threads = len(threading.enumerate())

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route("/")
def hello_world():
    return "Welcome!"

@app.route("/download")
def download_yt():
    url = request.args.get("url")
    download(url)
    
    return {"status":"downloading"}