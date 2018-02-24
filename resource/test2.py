import urllib
import urllib2

values = {}
values['username'] = "13297916138"
values['password'] = "nzj1341125"
date = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()