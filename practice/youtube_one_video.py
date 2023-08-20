from pytube import YouTube
from pytube.cli import on_progress
link = str(input("enter link to video"))
yt = YouTube(link)
yt=YouTube(link,on_progress_callback=on_progress)
stream = yt.streams.get_highest_resolution()
stream.download()
