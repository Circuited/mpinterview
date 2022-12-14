from pytube import Channel
from pytube import YouTube
import json
c = Channel('https://www.youtube.com/user/mohnishpabrai/videos')
mpdataset = {}
i = 0

for url in c.videos[:55]:
    mpdataset[i]={"URL": c.video_urls[i], "Title": url.title, "Upload data":url.publish_date}
    i = i+1

final = json.dumps(mpdataset, indent=2, default=str)

with open('mpdataset.json', 'w', encoding='utf-8') as JSON_file:
    JSON_file.write(final)

