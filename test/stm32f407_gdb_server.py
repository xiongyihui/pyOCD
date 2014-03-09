#!/usr/bin/env python

import sys

from pyOCD.interface import INTERFACE, usb_backend
from pyOCD.board import MbedBoard
from pyOCD.gdbserver import GDBServer

import logging

logging.basicConfig(level=logging.DEBUG)

mbed_vid = 0x0d28
mbed_pid = 0x0204
target_type = 'stm32f407'
Board = None


try:
    mbed_interfaces = INTERFACE[usb_backend].getAllConnectedInterface(mbed_vid, mbed_pid)
    if mbed_interfaces == None:
        print "Not find mbed board"
        sys.exit(-1)
        
    first_interface = mbed_interfaces[0]
    board = MbedBoard("target_" + target_type, "flash_" + target_type, first_interface)
    board.init()

    if board != None:
        gdb = GDBServer(board, 3333)
        while gdb.isAlive():
            gdb.join(timeout = 0.5)

except KeyboardInterrupt:
    gdb.stop()
except Exception as e:
    print "Unknown exception: %s" % e
    
finally:
    if board != None:
        board.uninit()
        
