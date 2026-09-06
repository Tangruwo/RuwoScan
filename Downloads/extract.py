import html
from html.parser import HTMLParser
import sys

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

def main():
    # Read HTML from stdin or file
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()
    else:
        data = sys.stdin.read()
    parser = LinkExtractor()
    parser.feed(data)
    # Deduplicate and filter
    seen = set()
    for link in parser.links:
        if link.startswith('vul/') and not link.startswith('http'):
            # normalize: remove leading ./ etc
            link = link.strip()
            if link not in seen:
                seen.add(link)
                print(link)

if __name__ == '__main__':
    main()