#!/bin/sh

HOST='ip_address'
USER='username'
PASSWD='password'
CMD='show interface g1'

(
echo open "$HOST"
sleep 2
echo "$USER"
sleep 2
echo "$PASSWD"
sleep 2
echo "$CMD"
sleep 2
echo "exit"
) | telnet > check_interface_status_bash.txt
sleep 10
echo exit

line1 = $(sed -n '/GigabitEthernet1 is/ p' check_interface_status_bash.txt)

if [[line1 -eq "GigabitEthernet1 is down, line protocol is down"]]
then
    echo "GigabitEthernet1 is down"
else
    echo "GigabitEthernet1 is up"
fi
