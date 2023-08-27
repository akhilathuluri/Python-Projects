from pytube import YouTube

def Download(link):
  YouTubeObject = YouTube(link)
  YouTubeObject = YouTubeObject.streams.get_audio_only()
  try:
    YouTubeObject.download()
  except:
    print("There Has Been An Error In Downloading Your Youtube Audio Please verify and try again")
  print("The Download Has Been Completed. Thank You! For Downloading")

link = input("Paste Your YouTube Link Here. URL: ")
Download(link)

