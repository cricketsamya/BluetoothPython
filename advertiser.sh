#!/bin/bash
#set -x
clear
BATTERY_MSB="0B"
BATTERY_LSB="BD"
while :
do
echo "Menu "
echo "1. Start advertise with 10Hz (as Stone)"
echo "2. Start advertise with 1 second (as Stone)"
echo "3. Start advertise with 10Hz (as iBeacon)"
echo "4. Start advertise with 1 second (as iBeacon)"
echo "5. Stop advertise" 
echo "6. Quit"
echo "Please enter option [1 - 6]"
read opts
case $opts in
1) sudo hciconfig hci0 up 
sudo hciconfig hci0 noleadv			  
sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 0E 0C 00 00 11 1E 21 02 1D 00 $BATTERY_LSB $BATTERY_MSB 19 AA C9 06 00 00 00 00 01 06 00 00 C8 00
sudo hcitool -i hci0 cmd 0x08 0x0006 A0 00 A0 00 03 00 00 00 00 00 00 00 00 07 00
sudo hcitool -i hci0 cmd 0x08 0x000a 01
echo "Advertisement Started "
;;
2)
sudo hciconfig hci0 up
sudo hciconfig hci0 noleadv
sudo hciconfig hci0 leadv 3
sudo hciconfig hci0 noscan
sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 0E 0C 00 00 11 1E 21 02 1D 00 $BATTERY_LSB $BATTERY_MSB 19 AA C9 06 00 00 00 00 01 06 00 00 C8 00
echo "Advertisement Started ";;
3)
sudo hciconfig hci0 up
sudo hciconfig hci0 noleadv
sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 E2 0A 39 F4 73 F5 4B C4 A1 2F 17 D1 AD 07 A9 61 00 00 00 00 C8 00
sudo hcitool -i hci0 cmd 0x08 0x0006 A0 00 A0 00 03 00 00 00 00 00 00 00 00 07 00
sudo hcitool -i hci0 cmd 0x08 0x000a 01
echo "iBeacon Advertisement Started ";;
4)
sudo hciconfig hci0 up
sudo hciconfig hci0 noleadv
sudo hciconfig hci0 leadv 3
sudo hciconfig hci0 noscan
sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 E2 0A 39 F4 73 F5 4B C4 A1 2F 17 D1 AD 07 A9 61 00 00 00 00 C8 00
echo "iBeacon Advertisement Started";;
5)
sudo hciconfig hci0 noleadv
echo "Advertisement stopped";;	  
6)
echo "Existed"
exit;;			 
esac
done
