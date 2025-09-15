import re
from collections import defaultdict

def solution(word, pages):
    answer = 0
    word = word.lower()
    pout, pin, pcnt = defaultdict(list), defaultdict(list), defaultdict(int) 
    urls = []
    for p in pages:
        url = re.search(r'(<meta property.+content=")(https://.*)"/>', p).group(2)
        urls.append(url)
        url_outs = re.findall(r'(<a href=")(https://\S*)">', p)
        for _, url_out in url_outs:
            pout[url].append(url_out)
            pin[url_out].append(url)
        p = p.lower()
        pcnt[url] = re.findall('[a-z]+', p).count(word)
    maxv, maxi = 0, 0
    for i, url in enumerate(urls):
        score = pcnt[url]
        for in_url in pin[url]:
            score += pcnt[in_url] / len(pout[in_url])
        if maxv < score:
            maxv = score
            maxi = i
    return maxi