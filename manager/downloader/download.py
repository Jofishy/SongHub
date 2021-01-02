from pytube import YouTube
from .util import getConfig
from os import path

import threading

class NoStreamError(Exception):
    pass

class DL_thread(threading.Thread):
    def __init__(self, url, location):
        threading.Thread.__init__(self)
        self.url = url
        self.location = location
    
    def run(self):
        vid = YouTube(self.url)

        print(self.url)

        raise NoStreamError

        # get highest quality audio track
        if vid.streams.filter(adaptive=True,only_audio=True).first():
            vid.streams.filter(adaptive=True,only_audio=True).first().download(self.location)
        elif vid.streams.filter(only_audio=True).first():
            vid.streams.filter(only_audio=True).first().download(self.location)
        else:
            raise NoStreamError


def download(url):
    config = getConfig()

    basepath = path.dirname(__file__)
    directory = path.abspath(path.join(basepath, config["dl_location"]))

    DL_thread(url, directory).start()