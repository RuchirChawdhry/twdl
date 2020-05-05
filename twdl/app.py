#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plumbum import cli
from functools import lru_cache
from rich.console import Console

from .tokens import Token


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
        console = Console()
        token = Token()

        if self.guest_token:
            console.rule("Guest Token")
            console.print(
                f"\n\tGuest Token: [center bold green]{token.guest_token}\n[/center bold green]\n",
                highlight=False,
                markup=True,
            )

        if self.bearer_token:
            console.rule("Guest Token")
            console.print(
                f"\n\tBearer Token: [bold green]{token.bearer_token}\n[/bold green]\n"
            )


if __name__ == "__main__":
    TWDL.run()
