from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def getInfo(name):
    req = Request("https://www.tiktok.com//{}".format(name),headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    for i in soup.find_all("meta", property="og:description"):
        sentenses = str(i).split("\"")[1].split()
        print(sentenses)
        name=""
        for i in sentenses[14:]:
            name+=" "+i
        return {
            "Name": name,
            "Followers" : sentenses[1],
            "Following": sentenses[3],
            "Likes" : sentenses[5]
                }
        

