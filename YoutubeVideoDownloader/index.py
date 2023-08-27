from pytube import YouTube

def Download(link):
  YouTubeObject = YouTube(link)
  YouTubeObject = YouTubeObject.streams.get_highest_resolution()
  try:
    YouTubeObject.download()
  except:
    print("There Has Been An Error In Downloading Your Youtube video Please verify and try again")
  print("The Download Has Been Completed. Thank You! For Downloading")

link = input("Paste Your YouTube Link Here. URL: ")
Download(link)

