#!/usr/bin/python

import bluetooth
import threading
import time
import random
import sys

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }
def html_escape(text):
     return "".join(html_escape_table.get(c,c) for c in text)

address="80:6C:1B:F0:FA:7B"
host="80:6C:1B:F0:FA:7B"
#address="A8:81:95:94:43:1B"
#host="A8:81:95:94:43:1B"
uuid="8ce255c0-200a-11e0-ac64-0800200c9a66"

#uuid="FA87C0D0-AFAC-11DE-8A39-0800200C9A66" 
service_matches = bluetooth.find_service( uuid = uuid, address = address )

#uuid="66841278-c3d1-11df-ab31-001de000a901" 
#uuid="8ce255c0-200a-11e0-ac64-0800200c9a66"
while True:
  try:
    print "Searching ..."
    try: service_matches
    except NameError:
      service_matches = bluetooth.find_service( uuid = uuid)
    else:
      if not service_matches:
        print ("without address")
        service_matches = bluetooth.find_service( uuid = uuid)
      else:
        print ("with address")
        service_matches_with_addr = bluetooth.find_service( uuid = uuid, address = host )
        if service_matches_with_addr:
          service_matches = service_matches_with_addr
        else:
          continue

    if service_matches:
      first_match = service_matches[0]
      port = first_match["port"]
      name = first_match["name"]
      host = first_match["host"]

      print "connecting to \"%s\" on %s %s" % (name, host,port)
      sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
      sock.connect((host, port))

      print "Happy Spamming"

      while True:
        try:
          #string = 'test' + random.choice('abcdefghij') + '\n'
	  with open('inbox.html', 'r') as content_file:
            string= content_file.read()
          try:
            print(string)
            sock.send(string)
            time.sleep(2)
 	    print "Phew! Done Searching"
            sock.close()
	    break

          except:
            print "Android no longer interested in my spam, socket not valid, going back to searching"
            break
        except KeyboardInterrupt:
          print "Done with Spamming, Press Ctrl-C again if you wish to quit, otherwise I'll keep searching"
          break

  except KeyboardInterrupt:
    print "Phew! Done Searching"
    sys.exit()
  break


