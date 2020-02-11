import argparse, re

from pytube import YouTube

try:
    from .search import get_search_results
except:
    from search import get_search_results

def get_youtube_content(url, save_to=None, mime_type='audio/mp4', **kwargs):
    utb = YouTube(url)
    log = f"Downloading {utb.title} from {url}..."
    for stream in utb.streams.filter(mime_type=mime_type, **kwargs).all():
        print(log)
        stream.download()

def main():
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Simple YouTube Downloader'
    )
    argparser.add_argument('keywords', help='동영상 url', nargs='*')
    args = argparser.parse_args()

    for url in args.keywords:
        regx_direct_link = re.compile(r'^https://youtu.be/(?P<content_id>.+)$')
        m = regx_direct_link.search(url)
        if m:
            get_youtube_content(url)
        else:
            keywords = ' '.join(args.keywords)
            results = get_search_results(keywords)
            for i, row in enumerate(results, 1):
                line = f"{i}. {row['title']}"
                print(line)

            print('=============================================================================')
            nlist = input('Input Your choices as seperate with comma: ')
            if not nlist:
                break
            nlist = nlist.split(',')
            nlist = list(map(int, nlist))
            for i, row in enumerate(results, 1):
                if i in nlist:
                    get_youtube_content(row['link'])

        

if __name__ == "__main__":
    main()
