# -*- coding: utf-8 -*-
"""
extract_strings.py - Extracts all unique French text strings from HTML files
to build the FR->EN dictionary.
"""
import os, re, json
from html.parser import HTMLParser

ROOT = r'C:\Users\Albert WIB\Desktop\soprocacam-website'
SKIP_TAGS = {'script', 'style', 'noscript'}

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.texts = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if any(t in SKIP_TAGS for t in self.stack):
            return
        txt = re.sub(r'\s+', ' ', data).strip()
        if txt and len(txt) > 1:
            self.texts.append(txt)


all_strings = set()
for fn in sorted(os.listdir(ROOT)):
    if not fn.endswith('.html'):
        continue
    with open(os.path.join(ROOT, fn), 'r', encoding='utf-8') as f:
        html = f.read()
    p = TextExtractor()
    p.feed(html)
    for t in p.texts:
        all_strings.add(t)

strings = sorted(all_strings)
print('Unique strings:', len(strings))
with open(os.path.join(ROOT, '_strings.json'), 'w', encoding='utf-8') as f:
    json.dump(strings, f, ensure_ascii=False, indent=1)
print('Saved _strings.json')
