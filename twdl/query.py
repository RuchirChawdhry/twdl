#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests as req
from functools import lru_cache

from .tokens import Token
from .video import Video
from . import response


class Query(response.Response):
    def __init__(self, tweet_url):
        self.tweet_url = tweet_url
        self.video_list = []
        super().__init__()

    @staticmethod
    def get_tweet_id(*args):
        try:
            return re.search(r"(\d{19})", "".join(args)).group(0)
        except:
            raise ValueError("Invalid Tweet ID")

    def _videos(self, tweet, data):
        vids = self.video_list

        for item in data["globalObjects"]["tweets"][tweet]["extended_entities"][
            "media"
        ]:
            for v in item["video_info"]["variants"]:
                if ".mp4" in v["url"]:
                    vids.append(v)
        return vids

    def get(self):
        t = Token()

        headers = {
            "authorization": f"Bearer {t.bearer_token}",
            "x-guest-token": t.guest_token,
        }
        params = {"refsrc_tweet": self.tweet_id, "tweet_mode": "extended"}

        self.session.headers.update(headers)
        self.session.params.update(params)

        response = self.session.get("https://api.twitter.com/2/rux.json")
        return self._videos(self.tweet_id, response.json())

    # @lru_cache(5)
    def videos(self):
        vids = self.video_list

        bitrates = [i["bitrate"] for i in vids]
        urls = [i["url"] for i in vids]
        resolution = [url.split("/")[6] for url in urls]

        return bitrates, urls, resolution

    @property
    def tweet_id(self):
        return Query.get_tweet_id(self.tweet_url)

    @property
    def mp3u8_url(self):
        raise NotImplementedError

    @property
    def status(self):
        raise NotImplementedError

    @property
    def found(self):
        raise NotImplementedError


if __name__ == "__main__":
    d = Query("1256610010257375235")
    d.get()
