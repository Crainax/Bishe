import urllib.request
import urllib

values = {}
values['username'] = "13297916138"
values['password'] = "nzj1341125"
date = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read())
