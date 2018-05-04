import urllib2,json,base64
accesstoken = "NDHVJMBQXUGH5XPRFG1U"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution,course)
#url ="http://dataportal.unistats.ac.uk/Pages/ApiDocumentation"
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)
#print json.dumps(data,indent=2)
for c in data:
    if c['Code'] == "SALARY" or c['Code'] == "NSS":
        c = c['Details']
        for d in c:
            if d['Code'] == "MED" or d['Code'] == "LDMED" or d['Code'] == "Q1":
                print(d['Value'])
