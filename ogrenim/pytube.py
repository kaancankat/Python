import ogrenim.pytube as pytube
url = input("enter video url")
path = ""
pytube.youtube(url).streams.get_highest_resolution().download(path)
