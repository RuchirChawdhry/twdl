#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cnamedtuple import namedtuple
from plumbum import cli
from functools import lru_cache
from rich.console import Console
from rich.table import Column, Table

from .tokens import Token
from .query import Query
from .video import Video


class TWDL(cli.Application):
    console = Console()

    VERSION = "0.1"
    PROGNAME = "twdl"
    DESCRIPTION = ""
    DESCRIPTION_MORE = ""

    guest_token = cli.Flag(["G", "guest-token"], help="Gets the guest token")
    bearer_token = cli.Flag(["B", "bearer-token"], help="Gets the bearer token")
    video_quality = cli.Flag(["best-quality"])
    tweet_id = cli.SwitchAttr(["I", "tweet-id"])

    @cli.switch(["-D", "--download"], str)
    def download(self, tweet_url):
        console = self.console

        tweet = Query(tweet_url)
        videos = Video(tweet.get())

        # table
        columns = ["#", "Bitrate", "Filesize", "Link"]
        table = Table(show_header=True, header_style="bold")
        for column in columns:
            table.add_column(column)

        for i in range(len(videos)):
            table.add_row(
                str(i + 1),
                videos.bitrate[i],
                videos.filesize[i] + " KB",
                videos.urls[i],
            )

        console.print(table)

    def main(self):
        token = Token()
        console = self.console
        console.rule("TWDL - Twitter Video Downloader")

        if self.guest_token:
            console.print(
                f"\n\tGuest Token: [bold green]{token.guest_token}\n[/bold green]\n",
                highlight=False,
            )

        if self.bearer_token:
            console.print(
                f"\n\tBearer Token: [bold green]{token.bearer_token}\n[/bold green]\n",
                highlight=False,
            )

        if self.tweet_id:
            query = Query(self.tweet_id)
            console.print(
                f"\n\tTweet ID: [bold green]{query.tweet_id}\n[/bold green]\n",
                highlight=False,
            )


if __name__ == "__main__":
    TWDL.run()
