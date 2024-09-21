# pip install pytube
# Play YOutube
from pytube import YouTube
import webbrowser

# Input the YouTube video URL
# video_url = input("Enter the YouTube video URL: ")
video_url = "https://www.youtube.com/watch?v=MFtfIpt7DfY"

# Create a YouTube object
yt = YouTube(video_url)

# Get the video title and thumbnail URL
video_title = yt.title
thumbnail_url = yt.thumbnail_url

# Open the video in a web browser
webbrowser.open(video_url)

# Display the video details
# print("Playing YouTube video:")
# print("Title:", video_title)
# print("Thumbnail URL:", thumbnail_url)

# Lyric
import time

time.sleep(62)

lyrics = [
    ["จำได้ไหมในวัน", 2],
    ["ที่รักของเรานั้นหอมหวาน", 3],
    ["นึกถึงคราที่เรา", 1.5],
    ["สองคนได้เคยตกหลุมรัก", 3],
    ["Feeling like DAY ONE", 1.5],
    ["ฉันยังคงนึกถึง DAY ONE", 2.5],
    ["วันที่เราทั้งสองมีกัน…", 5]
]

for x in lyrics:
    print(x[0])
    print()
    time.sleep(x[1])
