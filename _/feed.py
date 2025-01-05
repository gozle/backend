import feedparser

rss_url_1= "https://feeds.bbci.co.uk/news/world/rss.xml"
rss_url_2 = "http://rss.cnn.com/rss/edition_world.rss"

list_of_rss_urls = []

feed = feedparser.parse(rss_url_2)

if feed.status == 200:
    for entry in feed.entries:
        # print(entry.keys())

        title = entry.get("title", "")
        summary = entry.get("summary", "")

        if entry.get("content", ""):
            content =  entry.get('content', '')

        if entry.get("media_content", ""):
            image = entry.get("media_content", "")[0]

        link = "link_of_item",entry.get("link", "")
        
        source_name = feed.feed.get('title', '')
        source_link = feed.feed.get('link', '')
        source_language = feed.feed.get('language', '')

        source_icon = feed.feed.image.get('url', '')

else:
    print('smth went wrong')