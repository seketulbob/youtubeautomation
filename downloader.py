from pytube import YouTube
from sys import argv

link = argv[1]  # Link assigned to first argument from command line
yt = YouTube(link)  # Create youtube object from the link

print("Title: ", yt.title)
print("Length: ", yt.length)