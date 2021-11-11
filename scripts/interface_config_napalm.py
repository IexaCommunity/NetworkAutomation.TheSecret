from napalm import get_network_driver
import json

driver = get_network_driver('ios')
device = driver('192.168.183.111', 'enginesan', 'cisco')

device.open()
interface = 'GigabitEthernet1'
interface_config = device.get_interfaces()
file = open('check_interface_status_napalm.txt', 'w')
#file.write(interface_config)
file.write(json.dumps(interface_config))
file.close()

if interface_config['GigabitEthernet1']['is_up']:
    print("GigabitEthernet1 is up!")
else:
    print("GigabitEthernet1 is down!")
