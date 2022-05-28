import argparse
import sys
import socket
import random
from datetime import datetime
from pyfiglet import Figlet

print("\n\n\n")

fontList = ["big","bulbhead","roman","epic","larry3d","speed","nancyj","stampatello","smslant","slscript","serifcap","rounded","puffy","o8","letters","colossal","basic"]
fontType = random.choice(fontList)
f = Figlet(font=fontType)
print(f.renderText('portScanner'))

print("by emr4h\n")

print("-"*50)

parser = argparse.ArgumentParser(prog="portScan\n", 
    description="Port Scanner", 
    usage="\n\n  python3 portScanner.py -s <domain> -p <start port> <end port> \n",
    )

parser.add_argument("-s", type=str, help = "Please give a domain for port scan ")

parser.add_argument(
    '-p',
    type=int,
    nargs=2,
    metavar=('startPort', 'endPort'),
    help='Please give start and end ports.',
    )

args = parser.parse_args() 
startPort, endPort = args.p

time1 = datetime.now()

print("Target scanning: {}".format(args.s))
print("Scan start time: {} \n".format(time1))
print("Scanning is starting please wait...")

try:
    for port in range(startPort,endPort):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((args.s,port))

        if result == 0:
            print("Port {} open ".format(port))
        else :
            print("Port {} closed ".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting the program...")
    sys.exit()
except socket.gaierror:
    print("\n Could not resolve hostname!")
    sys.exit()
except socket.error:
    print("\n Error!")
    sys.exit()

time2 = datetime.now()
totalTime = time2 - time1

print("Elapsed time: {} \n".format(totalTime))
