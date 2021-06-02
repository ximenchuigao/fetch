import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, num_retries=2):
    print('downloading ', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('download error', e.reason)
        html = None
        if num_retries > 0:
            return download(url, num_retries-1)
    return html
