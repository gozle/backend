import feedparser
import requests
import time


list_of_rss_urls = [rss_url_1, rss_url_2]

def download_image(url, path= './'):
    img_data = requests.get(url).content
    filename = url.split('/')[-1]
    with open(path+filename, 'wb') as handler:
        handler.write(img_data)
    print('[DOWNLOADED SUCCESSFULLY]' + filename)
    
while True:
    for feed_url in list_of_rss_urls:
        feed = feedparser.parse(feed_url)

        if feed.status == 200:
            for entry in feed.entries:
                # print(entry.keys())

                title = entry.get("title", "")
                summary = entry.get("summary", "")

                if "content" in entry.keys():
                    content =  entry.get("content", "")
                else:
                    content = None

                if entry.get("media_content", ""):
                    image = entry.get("media_content", "")[0].get("url", None)
                else:
                    image = None

                link = "link_of_item",entry.get("link", "")
                
                source_name = feed.feed.get('title', '')
                source_link = feed.feed.get('link', '')
                source_language = feed.feed.get('language', '')

                source_icon = feed.feed.get('image', {}).get('url', '')

                if image:
                    download_image(image, "photo_uploads/")
                
                if source_icon:
                    download_image(source_icon, "icon_uploads/")

                print('title', title)
                print('summary', summary)
                print('content', content)
                print('image', image)
                print('link', link)
                print('source_name', source_name)
                print('source_link', source_link)
                print('source_language', source_language)
                print('source_icon', source_icon)

                print("*"*50)
            
        else:
            print('smth went wrong')
    time.sleep(60)