import time
import pafy
import os
os.environ['PAFY_BACKEND'] = 'internal'
import sys
sys.path.append('/path/to/youtube_dl')



url = 'https://www.youtube.com/playlist?list=PLDzeHZWIZsTr3nwuTegHLa2qlI81QweYG'
playlist = pafy.get_playlist(url)

count = 0
for video in playlist['items']:
    best = video['pafy'].getbest()
    best.download(filepath='/Users/kirtan/Desktop/code/python/youtube')
    count += 1
    print("Video Downloaded: ", count)
    time.sleep(5)  # add a 5-second delay between downloads

print("\nAll videos are downloaded.")
