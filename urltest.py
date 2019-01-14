import httplib2 as http
import json

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

uri = '<url:port with http://>'
path = '/path'
# Use URL encoding if required

target = urlparse(uri+path)
method = 'GET'
body = ''

h = http.Http()

# If you need authentication some example:
#if auth:
#    h.add_credentials(auth.user, auth.password)

response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)

# assume that content is a json reply
# parse content with the json module

class Resp(object):
    def __init__(self, data):
            self.__dict__ = json.loads(data)

for item in Resp(content).contents:
        print item["title"]
        print item["offerIdList"]
