from pytube import YouTube
link = str(input("enter link to video"))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()

# print("Title: ",yt.title)
# #Number of views of video
# print("Number of views: ",yt.views)
# #Length of the video
# print("Length of video: ",yt.length,"seconds")
# #Description of video
# print("Description: ",yt.description)
# #Rating
# print("Ratings: ",yt.rating)