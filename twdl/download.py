#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests as req

from .tokens import Token


class Download:
    def __init__(
        self,
        # tweet_url,
        session=req.Session(),
        # headers=None,
        # guest_token=None,
        # bearer_token=None,
    ):
        # self.tweet_url = tweet_url
        self.session = session
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        # self.guest_token = guest_token
        # self.bearer_token = bearer_token
        self.tokens = Token()

    def _download(self, video, filename):
        with self.session.get(video, stream=True) as resp:
            file_size = int(resp["Content-Length"])

            with open(filename, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
        return file_size

    def _get_videos(self, tweet, data):
        videos = []

        for item in data["globalObjects"]["tweets"][tweet]["extended_entities"][
            "media"
        ]:
            for video in item["video_info"]["variants"]:
                if ".mp4" in video["url"]:
                    videos.append(video)
        print(videos)  # videos

    def get(self, target):
        # try:
        #     tweet_id = re.search(r"(\d{19})", target).group(0)
        # except:
        #     raise ValueError("Invalid Tweet ID")

        headers = {
            "authorization": f"Bearer {self.tokens.btoken}",
            "x-guest-token": self.tokens.gtoken,
        }
        params = {"refsrc_tweet": target, "tweet_mode": "extended"}

        resp = self.session.get(
            "https://api.twitter.com/2/rux.json", params=params, headers=headers
        )
        return self._get_videos(target, resp.json())

    @property
    def mp3u8_url(self):
        raise NotImplementedError

    @property
    def status(self):
        raise NotImplementedError

    @property
    def found(self):
        raise NotImplementedError

    @property
    def available_bitrates(self):
        raise NotImplementedError

    @property
    def videos(self):
        raise NotImplementedError


if __name__ == "__main__":
    d = Download()
    d.get("1256610010257375235")
