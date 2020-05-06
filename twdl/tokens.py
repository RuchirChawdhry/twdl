#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re
from functools import lru_cache

from . import response


class Token(response.Response):
    def __init__(self):
        super().__init__()
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

        return {"guest_token": guest_token, "bearer_token": bearer_token}

    @property
    def guest_token(self):
        return self._tokens()["guest_token"]

    @property
    def bearer_token(self):
        return self._tokens()["bearer_token"]
