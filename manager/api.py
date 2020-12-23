from flask import Flask, request
from downloader.dispatcher import download

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route("/")
def hello_world():
    return "Welcome!"

# Old download request from extension
@app.route("/download")
def download_yt():
    url = request.args.get("url")
    download(url)
    
    return "ok"
