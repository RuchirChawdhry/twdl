#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re
from functools import lru_cache


class Token:
    def __init__(self):
        self.session = req.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        self._tokens()

    @lru_cache(4)
    def _tokens(self):
        data = self.session.get("https://twitter.com").text
        guest_token = re.search(r'decodeURIComponent\("gt=(.*?)\;', data).group(1)

        version = re.search(r"\/web\/main.(.*?)\.js", data).group(1)
        data = self.session.get(
            f"https://abs.twimg.com/responsive-web/web/main.{version}.js"
        ).text
        bearer_token = "AAAAAAAAAAA" + data.split("AAAAAAAAAAA")[-1].split('"')[0]

        return {"gtoken": guest_token, "btoken": bearer_token}

    @property
    def guest_token(self):
        return self._tokens()["gtoken"]

    @property
    def gtoken(self):
        return self._tokens()["gtoken"]

    @property
    def bearer_token(self):
        return self._tokens()["btoken"]

    @property
    def btoken(self):
        return self._tokens()["btoken"]
