#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
from rich.progress import Progress

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
        kb = [int(i.headers["Content-Length"]) // 1024 for i in resp]
        return kb
        # return [f"{i:,g}" for i in kb]

    def download(self, size, video, filename):
        progress = Progress()
        progress.add_task("Downloading...", total=size)

        with progress:
            progress.update(task_id=0, advance=0)

            with self.session.get(video, stream=True) as resp:
                with open(filename, "wb") as f:

                    for chunk in resp.iter_content(chunk_size=4096):
                        f.write(chunk)
                        progress.update(task_id=0, advance=len(chunk))
