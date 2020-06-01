#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cnamedtuple import namedtuple
from plumbum import cli
from functools import lru_cache
from rich.console import Console
from rich.table import Column, Table

from twdl.tokens import Token
from twdl.query import Query
from twdl.video import Video


class TWDL(cli.Application):
    console = Console()

    VERSION = "0.1"
    PROGNAME = "twdl"
    DESCRIPTION = ""
    DESCRIPTION_MORE = ""

    guest_token = cli.Flag(["G", "guest-token"], help="Get the guest token")
    bearer_token = cli.Flag(["B", "bearer-token"], help="Get the bearer token")
    tweet_id = cli.SwitchAttr(["I", "tweet-id"], help="Get Tweet ID")

    def heading(self):
        return self.console.rule("TWDL - Twitter Video Downloader")

    @cli.switch(
        ["-T", "--table"], str, help="Show all available videos in table format"
    )
    def table(self, tweet_url):
        self.heading()

        tweet = Query(tweet_url)
        videos = Video(tweet.get())

        table = Table(show_header=True, header_style="bold")
        columns = ["#", "Bitrate", "Filesize", "Link"]
        list(map(table.add_column, columns))

        for i in range(len(videos)):
            table.add_row(
                str(i + 1),
                videos.bitrate[i],
                videos.filesize[i] + " KB",
                videos.urls[i],
            )

        self.console.print(table)

    @cli.switch(["-D", "--download"], str, help="Download best quality in mp4")
    def download(self, tweet_url):
        self.heading()
        tweet = Query(tweet_url)
        video = Video(tweet.get())

        video.download(video.filesize[0], video.urls[0], "/Users/ruchir/testestest.mp4")
        self.console.print("\n[bold green]Success![/bold green]\n\n")
        # //TODO: Print path of downloaded file in the success message

    def main(self):
        if self.guest_token:
            self.heading()
            token = Token()
            self.console.print(
                f"\n\tGuest Token: [bold green]{token.guest_token}\n[/bold green]\n",
                highlight=False,
            )
        if self.bearer_token:
            self.heading()
            token = Token()
            self.console.print(
                f"\n\tBearer Token: [bold green]{token.bearer_token}\n[/bold green]\n",
                highlight=False,
            )
        if self.tweet_id:
            self.heading()
            token = Token()
            query = Query(self.tweet_id)
            self.console.print(
                f"\n\tTweet ID: [bold green]{query.tweet_id}\n[/bold green]\n",
                highlight=False,
            )
