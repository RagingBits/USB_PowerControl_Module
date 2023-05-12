#########################################################################################################
# Developed by Raging Bits. (2022)                                                                       #
# This code is provided free and to be used at users own responsability.                                #
#########################################################################################################
import subprocess
import os
import time
import serial
import argparse
import os.path
from pathlib import Path
import sys
import platform 


global serial_port
coms_port = "COM5"
debug_active = True
port_is_open = False

def debug_print(data):
    global debug_active
    if(True == debug_active):
        print(data)


def serial_open():

    global serial_port
    global coms_port
    global port_is_open
 
    while(port_is_open is False):

        debug_print("Serial port retry open...")
        
        try:         
            serial_port = serial.Serial(
                    port=coms_port,
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)
            
            port_is_open = True
            
            debug_print("Serial port open.\n")

        except:
            debug_print("Serial port open failure.\nSleep...")
            time.sleep(5)
            
 

def serial_reopen():

    global serial_port
    global coms_port
    global port_is_open
    global debug_active
    
    if(port_is_open == False):
        while(port_is_open is False):

            debug_print("Serial port retry open...")
            
            try:         
                serial_port.close()
                serial_port.open()
                port_is_open = True
                
                debug_print("Serial port open.\n")
            
            except:
                debug_print("Serial port open failure.\nSleep...")
                time.sleep(5)

    else:
        while(port_is_open == False):
            debug_print("Waiting Serial port to open.\nSleep...")
            time.sleep(1)
        
    return port_is_open
    

def main():
    
    #Declaration of globals to use.
    global serial_port
    global coms_port
    global port_is_open
    
    #Absorb the input arguments.
    #parser = argparse.ArgumentParser(description='Serial Port DTR example.')
    #parser.add_argument('-p', metavar='com_port', required=True, help='COM port. (Mandatory argument.)')
    #parser.add_argument('-v', metavar='verbose', required=False, help='Verbose mode. (Optional argument.)')
    #args = parser.parse_args()
    
    #if(args.v):
    #    if(args.v == "True" or args.v == "true" or args.v == "TRUE"):
    #        debug_active = True
    #        print("Verbose mode active.")
    #    else:
    #        print("Verbose mode inactive.")
    #else:
    #    print("Verbose mode inactive.")
    
            
    #coms_port = args.p
    
    serial_open()
    
    #Start MQTT client
    while(True):
        debug_print("DTR ON!")
        serial_port.setDTR(False)
        time.sleep(0.5)
        debug_print("DTR OFF!")
        serial_port.setDTR(True)
        time.sleep(0.5)
        
        
    print("Service ended.")
    
    
if __name__ == "__main__":
    main()
