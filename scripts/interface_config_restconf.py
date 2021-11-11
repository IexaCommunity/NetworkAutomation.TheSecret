import requests
import json

response = requests.get(
    url = 'https://192.168.183.111/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1',
    auth = ('enginesan','cisco'),
    headers = {
        'Accept':'application/yang-data+json'
    },
    verify = False)

dictio = json.loads(response.text)
status = dictio['ietf-interfaces:interface']['enabled']
if status:
    print('GigabitEthernet1 is up!')
else:
    print('GigabitEthernet1 is down!')

file = open('check_interface_status_restconf.txt','w+')
file.write(response.text)
file.close()
