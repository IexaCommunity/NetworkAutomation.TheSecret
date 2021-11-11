import paramiko 
import re

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh_client.connect(hostname="192.168.183.111",username="enginesan",password="cisco") 

#remote_connection = ssh_client.invoke_shell()
#stdin, stdout, stderr = remote_connection.send("show running-config\n")
stdin, stdout, stderr = ssh_client.exec_command('sh interface g1')
list = stdout.readlines()
output = [line.rstrip() for line in list] 
#print (''.join(output))
file = open('check_interface_status_paramiko.txt', 'w+')
file.write('\n'.join(output))
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


