import os
import subprocess
import optparse

def change_mac():
    interface = input("enter the interface name:- ")
    new_mac = input("enter the mac address:- ")
    subprocess.call(["ifconfig "  + interface +  " down"], shell=True)
    subprocess.call(["ifconfig "  + interface +  " hw ether "  + new_mac], shell=True)
    subprocess.call(["ifconfig "  + interface +  " up"], shell=True)
    subprocess.call(["ifconfig "], shell=True)
    
change_mac()
 
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)