import urllib2,json,base64
accesstoken = "NDHVJMBQXUGH5XPRFG1U"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution,course)
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)
#print json.dumps(data,indent=2)
for d in data:
    if d['Code'] == "SALARY" or d['Code'] == "NSS":
        for v in d['Details']:
            if v['Code'] == "MED" or v['Code'] == "LDMED" or v['Code'] == "Q1":
                print(v['Value'])
