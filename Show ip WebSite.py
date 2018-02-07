print """
#	Telegram : @zero_day_hack  #
#	Zero Day Hack Security     #
"""


import socket

while True:
      
      name_site = raw_input("Enter Address Web Site : ")
      try:
            print(socket.gethostbyname(name_site))
            print "\n"
      except:
            print "Url Error !"
