import json
import urllib.request 
with urllib.request.urlopen('https://esi.tech.ccp.is/latest/universe/system_kills/') as h1:
    print(h1.read().decode('utf-8'))
