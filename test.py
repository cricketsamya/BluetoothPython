import struct
from bluepy import btle

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(data)


if __name__ == '__main__':
    heartrate_uuid = btle.UUID(0x2a38)

p = btle.Peripheral("80:6c:1b:f0:fa:7b")
p.setDelegate(MyDelegate())

print("Connected")

try:
    print("Setting Characteristics")
    ch = p.getCharacteristics(uuid=heartrate_uuid)[0]
    print("Setting Done, writing now")
    ch.write(struct.pack('<bb', 0x01, 0x00))
    print("writing Done, looping now")
    while True:
        if p.waitForNotifications(1.0):
            print("Notification trigger")
            continue
    print("Waiting")
finally:
    p.disconnect()
