from pytube import YouTube
from util import getConfig
from os import path

def download(url):
    config = getConfig()

    basepath = path.dirname(__file__)
    directory = path.abspath(path.join(basepath, config["dl_location"]))

    vid = YouTube(url)

    # get highest quality audio track
    vid.streams.filter(adaptive=True,only_audio=True).first().download(directory)