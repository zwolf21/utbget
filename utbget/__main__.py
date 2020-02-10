import argparse
from pytube import YouTube

def get_youtube_content(url, save_to=None, mime_type='audio/mp4', **kwargs):
    utb = YouTube(url)
    for stream in utb.streams.filter(mime_type=mime_type, **kwargs).all():
        stream.download()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Simple YouTube Downloader'
    )

    argparser.add_argument('keywords', help='동영상 url', nargs='*')

    args = argparser.parse_args()

    for url in args.keywords:
        print(f"downloading from ({url})....")
        get_youtube_content(url)



