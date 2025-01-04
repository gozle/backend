import feedparser

rss_url_1= "https://feeds.bbci.co.uk/news/world/rss.xml"
rss_url_2 = "http://rss.cnn.com/rss/edition_world.rss"

list_of_rss_urls = []

feed = feedparser.parse(rss_url_2)

if feed.status == 200:
    for entry in feed.entries:
        print(entry.keys())
else:
    print('smth went wrong')