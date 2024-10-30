
from urllib.parse import urlparse, parse_qs


def compare_urls(url1, url2):
    """ compare two urls """
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)

    # Compare scheme, netloc, and path
    if (parsed_url1.scheme, parsed_url1.netloc, parsed_url1.path) != (
    parsed_url2.scheme, parsed_url2.netloc, parsed_url2.path):
        return False

    # Compare query parameters, ignoring order
    return parse_qs(parsed_url1.query) == parse_qs(parsed_url2.query)