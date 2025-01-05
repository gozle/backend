import feedparser
import requests
import time

import os
import sys
import django
from django.conf import settings

# Add the project root directory to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rss_main.settings")  # Replace 'rss_main' with your project name

# Configure Django
django.setup()

from rss_app.models import Source, News


rss_url_1 = "http://rss.cnn.com/rss/edition_world.rss"
rss_url_2 = "https://feeds.bbci.co.uk/news/world/rss.xml"

list_of_rss_urls = [rss_url_1, rss_url_2]

def download_image(url, path= './'):
    photo_dir = os.path.join(settings.MEDIA_ROOT, path)
    os.makedirs(photo_dir, exist_ok=True)

    img_data = requests.get(url).content
    filename = url.split('/')[-1]
    photo_path = os.path.join(photo_dir, filename)

    with open(photo_path, 'wb') as handler:
        handler.write(img_data)
        return f"{path}/{filename}"
    
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
                    content = ''

                if entry.get("media_content", ""):
                    image = entry.get("media_content", "")[0].get("url", None)
                else:
                    image = None

                link = "link_of_item",entry.get("link", "")
                
                source_name = feed.feed.get('title', '')
                source_link = feed.feed.get('link', '')
                source_language = feed.feed.get('language', '')
                source_icon = feed.feed.get('image', {}).get('url', '')


                if source_icon:
                    icon_db = download_image(source_icon, f"icon_uploads")

                if image:
                    photo_db = download_image(image, f"photo_uploads")
                
                # save to db
                if not Source.objects.filter(name=source_name).first():
                    source_item = Source.objects.create(name=source_name, link=source_link,
                    language=source_language.split('-')[0], icon = icon_db)
                    source_item.save()

                if not News.objects.filter(title=title).first():
                    source = Source.objects.filter(name=source_name).first()
                    news_item = News.objects.create(source=source, title=title, summary=summary, content=content,
                    photo = photo_db, url=source_link)
                    news_item.save()
                # print('source_name', source_name)
                # print('source_link', source_link)
                # print('source_language', source_language.split('-')[0])
                # print('source_icon', source_icon)

                # print('title', title)
                # print('summary', summary)
                # print('content', content)
                # print('image', image)
                # print('link', link)
                

                print("*"*50)
            
        else:
            print('smth went wrong')
    time.sleep(60)