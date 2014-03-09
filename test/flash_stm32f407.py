#!/usr/bin/env python

from time import sleep, time
from random import randrange
from struct import unpack
import sys

from pyOCD.interface import INTERFACE, usb_backend
from pyOCD.board import MbedBoard

import logging

logging.basicConfig(level=logging.DEBUG)

mbed_vid = 0x0d28
mbed_pid = 0x0204
target_type = 'stm32f407'
Board = None

addr = 0x20000001

def getSecNum(addr):
    n = (addr >> 12) & 0x00FF;
    if n >= 0x20:
        n = 4 + (n >> 5)
    elif n > 0x10:
        n = 3 + (n >> 4)
    else:
        n = 0 + (n >> 2)
    return n

def flashBinary(flash, path_file):
    """
    Flash a binary
    """
    f = open(path_file, "rb")
    
    start = time()
    flash.init()
    logging.debug("flash init OK: pc: 0x%X", flash.target.readCoreRegister('pc'))
    # flash.eraseAll()
    # logging.debug("eraseAll OK: pc: 0x%X", flash.target.readCoreRegister('pc'))

    """
    bin = open(os.path.join(parentdir, 'res', 'good_bin.txt'), "w+")
    """
    
    flashPtr = 0
    nb_bytes = 0
    lastSecNum = -1
    try:
        bytes_read = f.read(flash.page_size)
        while bytes_read:
            bytes_read = unpack(str(len(bytes_read)) + 'B', bytes_read)
            nb_bytes += len(bytes_read)
            
            currentSecNum = getSecNum(flashPtr)
            if lastSecNum != currentSecNum:
                # erase sector
                flash.eraseSector(flashPtr)
                logging.debug("eraseSector OK: sector: %d, pc: 0x%X", currentSecNum, flash.target.readCoreRegister('pc'))
                lastSecNum = currentSecNum
                
            # page download
            flash.programPage(flashPtr, bytes_read)
            """
            i = 0
            while (i < len(bytes_read)):
                bin.write(str(list(bytes_read[i:i+16])) + "\n")
                i += 16
            """
            flashPtr += flash.page_size

            bytes_read = f.read(flash.page_size)
    finally:
        f.close()
        """
        bin.close()
        """
    end = time()
    logging.info("%f kbytes flashed in %f seconds ===> %f kbytes/s" %(nb_bytes/1000, end-start, nb_bytes/(1000*(end - start))))

if len(sys.argv) != 2:
    print "Usage: %s binary_file"
    sys.exit(-1)
    
binary_file = sys.argv[1]

try:
    mbed_interfaces = INTERFACE[usb_backend].getAllConnectedInterface(mbed_vid, mbed_pid)
    if mbed_interfaces == None:
        print "Not find mbed interface"
        sys.exit(-2)

    first_interface = mbed_interfaces[0]
    board = MbedBoard("target_" + target_type, "flash_" + target_type, first_interface)
    board.init()
    
    target = board.target
    transport = board.transport
    flash = board.flash
    interface = board.interface
    
    flashBinary(flash, binary_file)
    
    target.reset()

except Exception as e:
    print "Unknown exception: %s" % e
    
finally:
    if board != None:
        board.uninit()
        
