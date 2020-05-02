#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plumbum import cli
from twtoken import Token


class TWDL(cli.Application):

    VERSION = "0.1"
    PROGNAME = "twdl"
    DESCRIPTION = ""
    DESCRIPTION_MORE = ""

    guest_token = cli.Flag(["G", "guest-token"], help="Gets the guest token")
    bearer_token = cli.Flag(["B", "bearer-token"], help="Gets the bearer token")
    video_quality = cli.Flag(["best-quality"])
    tweet_url = cli.Flag(["T", "tweet"])

    def main(self):
        print(self.helpall())

        if self.guest_token or self.bearer_token:
            token = Token()
            print(
                f"Guest Token: {token.guest_token}\nBearer Token: {token.bearer_token}"
            )


if __name__ == "__main__":
    TWDL.run()
