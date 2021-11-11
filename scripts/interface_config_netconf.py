import ncclient
from ncclient import manager
import xml.etree.ElementTree as ET

m = manager.connect(host='192.168.183.111', port=830, username='enginesan', password='cisco',device_params={'name':'csr'})

#for c in m.server_capabilities:
#    print(c)

netconf_data = '''
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces-state>
</filter>
'''
# Execute the get-config RPC
netconf_reply = m.get_config(filter=netconf_data, source='running')
response = netconf_reply.data
status = list(response)[0][0][3].text

if status:
    print('GigabitEthernet1 is up')
else:
    print('GigabitEthernet1 is down')

file = open('check_interface_status_netconf.xml', 'w+')
file.write(str(netconf_reply))
file.close
