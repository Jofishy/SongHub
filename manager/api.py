from flask import Flask, request
import threading
from downloader.download import download

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route("/")
def hello_world():
    return "Welcome!"

@app.route("/downloader/<id>")
def get_downloader(id):
    return id

@app.route("/download")
def download_yt():
    url = request.args.get("url")
    dl_thread = download(url)
    
    body = {
        "status": "downloading",
        "downloader": dl_thread
    }

    return body, 202