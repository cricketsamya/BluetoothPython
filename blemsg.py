from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#uuid="00001101-0000-1000-8000-00805F9B34FB"
#uuid="0000110e-0000-1000-8000-00805f9b34fb"
#uuid="8ce255c0-200a-11e0-ac64-0800200c9a66"
x = 0

while x<3:
        print "Waiting for connection on RFCOMM channel %d" % port

        client_sock, client_info = server_sock.accept()
        print "Accepted connection from ", client_info
        x = 1

        while x == 1:
                try:
                        data = client_sock.recv(1024)
                        if len(data) == 0: break
                        print "received [%s]" % data

                        if data == 'temp':
                                data = str(read_temp())+'!'
                        elif data == 'a':
                                data = 'A A A!'
                        elif data == 'b':
                                data = 'B B B'
                        else:
                                data = 'WTF!'
                                x = 5
                        client_sock.send(data)
                        print "sending [%s]" % data

                except IOError:
                        pass


                except KeyboardInterrupt:

                        print "disconnected"

                        client_sock.close()
                        server_sock.close()
                        print "all done"

                        break

if x == 5:
        print "disconnected"
        client_sock.close()
        server_sock.close()
        print "all done"
