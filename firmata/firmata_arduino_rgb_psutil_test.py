#!/usr/bin/python
######################################################################
"""
firmata_arduino_rgb_psutil_test.py - demo to use psutil and pyfirmata
	modules on Python host to control RGB LED's wired to PWM pins on
	an Arduino serial slave running Firmata.

Bart Spainhour <bart@tinkernauts.org>
	
Uses Python modules:
 https://github.com/giampaolo/psutil
 A cross-platform process and system utilities module for Python 
 
 https://github.com/tino/pyFirmata
 Python interface for the Firmata (http://firmata.org/) protocol.
 
"""
######################################################################

from pyfirmata import Arduino, util
from time import sleep
import psutil

######################################################################
__author__ = "Bart Spainhour"
__email__ = "bart@tinkernauts.org"

######################################################################
# Open Serial Connection to Firmata on Arduino
#
print "Intializing Arduino connection ..."

# initialize pyfirmata arduino instance
board = Arduino('COM6')

# get major/minor from the Arduino slave and output to console
firmata_version = board.get_firmata_version()
print "Connected to Firmata " + str(firmata_version[0]) + "." + str(firmata_version[1])

######################################################################
# Set digital pins to PWM mode
#
# RGB LED 1 PWM
r1p = board.get_pin('d:3:p')
g1p = board.get_pin('d:5:p')
b1p = board.get_pin('d:6:p')
#
# RGB LED 2 PWM
# Set digital pins to PWM mode
r2p = board.get_pin('d:9:p')
g2p = board.get_pin('d:10:p')
b2p = board.get_pin('d:11:p')

######################################################################
# Main Loop
#
try:  
	######################################################################
	# Loop Forever
	#
	while True:
		######################################################################
		# Get CPU Load for specified interval
		# percpu=False returns a single percentage.
		# percpu=True returns a percentage for each CPU
		# [0.0, 0.0, 0.0, 0.0]
		mycpu = psutil.cpu_percent(interval=.1, percpu=False)/100.0
		
		######################################################################
		# Get Memory usage
		# svmem(total=8385982464L, available=5219328000L, percent=37.8, used=3166654464L, free=5219328000L)
		mymem = psutil.virtual_memory()
		
		######################################################################
		# Print values to console
		print str(mycpu) + " - " + str(mymem.percent)
		
		######################################################################
		# write float values to firmata PWM pins for RGB LED's
		#
		# Green #1 increases in brightness with CPU load
		g1p.write(mycpu)
		# Blue #2 increases in brightness with memory usage
		b2p.write(mymem.percent/100.0)

######################################################################
# Handle Ctrl-C breaks and turn off all LED's
#
except KeyboardInterrupt:
	print "Keybpoard Interrupt ..."
	# RGB LED 1 PWM
	r1p.write(0)
	g1p.write(0)
	b1p.write(0)
	# RGB LED 2 PWM
	r2p.write(0)
	g2p.write(0)
	b2p.write(0)
	# 
	print "End."
