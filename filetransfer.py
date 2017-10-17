
import bluetooth
from PyOBEX.client import Client
import sys

address = "80:6C:1B:F0:FA:7B"
uuid="8ce255c0-200a-11e0-ac64-0800200c9a66"
print("Searching for OBEX service on %s" % address)

#service_matches = bluetooth.find_service(name='OBEX Object Push', address = address )
service_matches = bluetooth.find_service( uuid = uuid, address = address )
if len(service_matches) == 0:
    print("Couldn't find the service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))
client = Client(host, port)
client.connect()
client.put("hc.apk", open("hc.apk", "rb").read())
client.disconnect()
