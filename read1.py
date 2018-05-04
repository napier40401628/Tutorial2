import urllib2,json,base64
accesstoken="NDHVJMBQXUGH5XPRFG1U"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/10007772.json"
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)
print data['Name']
