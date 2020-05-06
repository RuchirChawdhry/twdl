#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req

from . import response


class Video(response.Response):
    def __init__(self, data=[]):
        self.data = data
        self.bitrate = [f"{i['bitrate'] // 1024:,g}" for i in data]
        self.urls = [i["url"] for i in data]
        super().__init__()

    def __len__(self):
        return len(self.urls)

    def __str__(self):
        return ", ".join(self.urls)

    @property
    def resolution(self):
        return [res.split("/")[5] for res in self.urls]

    @property
    def filesize(self):
        resp = list(map(self.session.head, self.urls))
        mb = [int(i.headers["Content-Length"]) // 1024 for i in resp]
        return [f"{i:,g}" for i in mb]

    def download(self, filename, video):
        with self.session.get(video, stream=True) as resp:
            with open(filename, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
