from pytube import Playlist

link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)
count= 0
for video in yt_playlist.videos:
    if(count>124):{
            video.streams.get_highest_resolution().download(output_path='/Users/kirtan/Desktop/code/python/youtube')
        
            }
    count += 1
    
    print("Video Downloaded: ",count)

print("\nAll videos are downloaded.")