import pytube
url = input("enter video url")
path = ""
pytube.youtube(url).streams.get_highest_resolution().download(path)
