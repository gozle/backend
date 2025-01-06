import feedparser
import requests
import time

import os
import sys
import django
from django.conf import settings
from pytz import UTC
from datetime import datetime

# Add the project root directory to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rss_main.settings")  # Replace 'rss_main' with your project name

# Configure Django
django.setup()

from rss_app.models import Source, News


list_of_rss_urls = [x for x in Source.objects.all()]

def download_image(url, path='photo_uploads/'):
    # Path to the media directory for storing images
    photo_dir = os.path.join(settings.MEDIA_ROOT, path)
    os.makedirs(photo_dir, exist_ok=True)

    # Download the image
    img_data = requests.get(url).content
    filename = url.split('/')[-1]
    photo_path = os.path.join(photo_dir, filename)

    # Save the image locally
    with open(photo_path, 'wb') as handler:
        handler.write(img_data)
    
    # Return the relative path to be stored in the database
    return os.path.join(path, filename)
    
while True:
    for feed_url in list_of_rss_urls:
        feed = feedparser.parse(feed_url.rss_url)
        
        source = feed_url
        if feed.status == 200:
            for entry in feed.entries:
                # print(entry.keys())


                pubDate = entry.get("published", "")
                parsed_datetime = datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S %Z')
                formatted_datetime = parsed_datetime.replace(tzinfo=UTC).strftime('%Y-%m-%d %H:%M:%S%z')

                guid = entry.get('id', '')
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

                link = entry.get("link", "")
                
                if image:
                    photo_db = download_image(image)


                # FOR NEWS
                if not News.objects.filter(source=source, guid=guid).first():
                    news_item = News.objects.create(source=source, guid=guid, title=title, summary=summary, content=content,
                    photo = photo_db, url=link, pubDate=formatted_datetime)
                    news_item.save()


                # FOR SOURCE----->
                # source_name = feed.feed.get('title', '')
                # source_link = feed.feed.get('link', '')
                # source_language = feed.feed.get('language', '')
                # source_icon = feed.feed.get('image', {}).get('url', '')

                # SOURCE ICON----->
                # if source_icon:
                #     icon_db = download_image(source_icon, f"icon_uploads")
                
                # save to db----->
                # if not Source.objects.filter(name=source_name).first():
                #     source_item = Source.objects.create(name=source_name, link=source_link,
                #     language=source_language.split('-')[0], icon = icon_db)
                #     source_item.save()

                # print('source_name', source_name)
                # print('source_link', source_link)
                # print('source_language', source_language.split('-')[0])
                # print('source_icon', source_icon)

                # print('title', title)
                # print('summary', summary)
                # print('content', content)
                # print('image', image)
                # print('link', link)
                
            
        else:
            print('smth went wrong')
    time.sleep(60)