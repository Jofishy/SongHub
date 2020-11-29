from flask import Flask, request
from downloader import download

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/download")
def download_yt():
    url = request.args.get("url")
    if download(url):
        return "ok"
    else:
        abort(500)