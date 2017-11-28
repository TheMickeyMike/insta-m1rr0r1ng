"""Mirroring Instagram user photos.

Usage:
  insta_mirror.py <target_username> --username=<username> --password=<password>
  insta_mirror.py (-h | --help)
  insta_mirror.py --version

Options:
  -h --help                Show this screen.
  --version                Show version.
  --username=<username>    Your username.
  --password=<password>    Your password.

"""
import asyncio

from docopt import docopt
from insta_downloader import Downloader
from insta_provider import create_insta_provider


def run(target, username, password):
    instagram_provider = create_insta_provider(username, password)

    print(f'Logged in as: {instagram_provider.authed_web_api_client.username}')
    print('Fetching feed...')
    user_id = instagram_provider.get_user_id(target)
    user_feed = instagram_provider.get_user_feed(user_id)

    loop = asyncio.get_event_loop()
    Downloader(loop).start_processing(user_feed)
    loop.close()


if __name__ == "__main__":
    arguments = docopt(__doc__, version='Insta Mirror 1.0')
    run(target=arguments['<target_username>'], username=arguments['--username'], password=arguments['--password'])
