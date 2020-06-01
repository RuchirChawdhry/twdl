#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req


class Response:
    def __init__(self, headers={}, params={}):
        self.session = req.Session()
        self.headers = headers
        self.params = params

        if not headers or params:
            self._default_headers()

    # //TODO: randomization of user_agents instead of hard-coding one

    def _default_headers(self):
        user_agent = [
            "Mozilla/5.0",
            "(Windows NT 10.0; Win64; x64)",
            "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Chrome/81.0.4044.92 Safari/537.36",
        ]
        language = ["en-US,en;q=0.9"]
        encoding = ["gzip, deflate"]
        referer = ["https://twitter.com/"]

        self.session.headers = {
            "User-Agent": " ".join(user_agent),
            "Accept-Language": "".join(language),
            "Accept-Encoding": "".join(encoding),
            "Referer": "".join(referer),
        }
        return self.session.headers
