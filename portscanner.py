import socket
import sys
from datetime import datetime as dt


#Target
try:
    target = socket.gethostbyname(sys.argv[1]) #Takes 2nd input as target and translate to IPv4

except NameError:
    print(f'{target} does not exist.')
    quit()
except IndexError:
    print('Syntax Error - python3 scanner.py <domainname>')
    sys.exit()
except socket.gaierror:
    print("Hostname can't be resolved")
    sys.exit()
except socket.error:
    print("Unable to connect to the Server")
    sys.exit()


#Adding Banner to the script
print("\n\n")
print("*" * 50)
print("Scanning target: "+target+ " (www."+sys.argv[1] + ")")
print("Scanning started at: "+str(dt.now()))
print("*" * 50)
print("\n\n")

#Banner ends here

#connecting to the given IP/Host
try:

    for port in range( 1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
            s.close
#In order to avoid infinite loop, applying controlled exiting option
except KeyboardInterrupt:
    print("Seems that you want to quit, Good Bye")   #for conditions similar to ctrl + c command
    sys.exit()
