from pytube import Playlist

link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_lowest_resolution().download("/Users/kirtan/Desktop/code/python/")
    print("Video Downloaded: ", video.title)

print("\nAll videos are downloaded.")