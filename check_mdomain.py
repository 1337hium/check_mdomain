#!/usr/local/bin/python3
#########
#
# 04.10.2019 Michael Rüedi https://github.com/1337hium/check_mdomain
#
#########
import sys
from datetime import datetime
import datetime
import urllib.request, json
if len(sys.argv) == 1:
    print("Set URL to md-status: check_mdomain.py [URL]")
else:
    url1 = sys.argv[1]
    a=[]
    with urllib.request.urlopen(url1) as url:
        data = json.loads(url.read().decode())
    for domain in data['managed-domains']:
        date = domain["cert"]["valid-until"]
        name = domain["name"]
        today = datetime.datetime.today()
        string = today.strftime('%Y-%m-%d')
        dt = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d')
        datetime_object = datetime.datetime.strptime(dt, '%Y-%m-%d')
        today1 = datetime.datetime.strptime(string, '%Y-%m-%d')
        actual = datetime_object - today1
        if actual.days < 15:
           crit1 = (name, dt)
           crit = ','.join(map(str, crit1))
           a.append(crit)
    if a:
       print(*a, sep = "\n")
       sys.exit(2)
    else:
       print ("MDomains OK")

