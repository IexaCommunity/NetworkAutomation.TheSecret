import netmiko
from netmiko import ConnectHandler
import re
import time

device1 = {
'device_type': 'cisco_ios',
'ip': '192.168.183.111',
'username': 'enginesan',
'password': 'cisco',
}

net_connect = ConnectHandler(**device1) 
net_connect.send_command("terminal length 0\n") 
time.sleep(1) 
output = net_connect.send_command("sh interface g1\n") 
#print(running_config)
file = open('check_interface_status_netmiko.txt', 'w')
file.write(output)
file.close()

p = re.compile('^GigabitEthernet1 is up.*')

i = 0
for line in output:
    m = p.findall(line)
    if len(m) > 0:
        i = i + 1

if i > 0:
    print("GigabitEthernet1 is up")
else:
    print("GigabitEthernet1 is down")
