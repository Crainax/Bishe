import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")
fhandle = open("test1.html", "wb")
data = file.read()
fhandle.write(data)
