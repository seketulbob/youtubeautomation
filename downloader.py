from pytube import YouTube
from sys import argv

link = argv[1]  # Link assigned to first argument from command line
yt = YouTube(link)  # Create youtube object from the link

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()  # Create downloader object

yd.download('/Users/bobs/Desktop/Downloaded Vids/')  # run downloader
