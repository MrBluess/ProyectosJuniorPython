import pytube

link = input("Link de Youtube")
video_download = pytube.YouTube(link)             
video_download.streams.first().download()
print (('Video Downloaded'), link)