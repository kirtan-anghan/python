from pytube import Playlist

link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)
count= 0
for video in yt_playlist.videos:
    if(count>=0):{
            video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='/Users/kirtan/Desktop/code/python/youtube')
            }
    count += 1
    
    print("Video Downloaded: ",count)

print("\nAll videos are downloaded.")
