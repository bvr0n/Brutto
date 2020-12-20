#!/usr/bin/env python3

# Created by bvr0n
# A Simple Hidden Directories Brute Forcer In Python For Linux/Windows

import requests
import pyfiglet
import sys
import argparse



# Some Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


ascii_banner = pyfiglet.figlet_format('Brutto')
print (bcolors.OKCYAN + ascii_banner)
print (bcolors.WARNING + "            	      by @bvr0n \n")

def usage():
    print('optional arguments:\n   -u\tset url\n   -p\tset port\n   -w\tset wordlist\n')

if len(sys.argv) < 4:
    usage()
    exit()
else:
    url = sys.argv[2] 
    #port = sys.argv[3]
    port = sys.argv[4]
    #w = sys.argv[5]
    w = sys.argv[6]

print ("\n")
print (bcolors.WARNING + "[*] Im Looking...")

# Open the Wordlist
f = open(w, "r")


# Loop inside the wordlist and try every line
for i in f:
    f = i.strip("\n")
    r = requests.get("http://" + url + ":" + port + "/" + f)
    # Check if the header is 200 = [OK]
    if r.status_code == 200:
        print (bcolors.OKGREEN + "[+] I Found This: " + "/" + f)
    else:
        pass
