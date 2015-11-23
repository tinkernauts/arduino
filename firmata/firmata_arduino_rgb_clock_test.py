#!/usr/bin/python
######################################################################
"""
firmata_arduino_rgb_clock_test.py - demo to use pyfirmata
	modules on Python host to control RGB LED's wired to PWM pins on
	an Arduino serial slave running Firmata.

Bart Spainhour <bart@tinkernauts.org>
	
Uses Python modules:
 https://github.com/tino/pyFirmata
 Python interface for the Firmata (http://firmata.org/) protocol.
 
"""
######################################################################
from pyfirmata import Arduino, util
from datetime import datetime
from sys import stdout
from time import sleep

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
# Main Time Function
#
def get_time():
	######################################################################
	# Get Current time from datetime.now()
	now = datetime.now()
	
	######################################################################
	# Options for datetime object
	#
	# now.year
	# now.month
	# now.day
	# now.hour
	# now.minute
	# now.second
	# now.microsecond


	######################################################################
	# Concatenate strings to display time in console.
	# HH:MM:SS.SSS
	dsp_time = str(now.hour)+":"+str(now.minute)+":"+str(now.second)+"."+str(now.microsecond/1000)
	
	######################################################################
	# Convert values to floats for PWM control
	# Using PWM to control brightness, float value is 0 (off) to 1 (full brightness)
	#
	# Set current hour to percentage of a 24-hour day
	# i.e. 11pm 23/24 = 0.9583333333333333 or 95.83% brightness
	led_hour = (now.hour/24.00)
	#
	# Set current minute to percentage of a 60-minute hour
	# i.e. xx:47 47/60 = 0.7833333333333333 or 78.33% brightness
	led_minute = (now.minute/60.00)
	#
	# Set current second to percentage of a 60-second minute
	# i.e. xx:xx:17 17/60 = 0.2833333333333333 or 28.33% brightness
	led_second = (now.second/60.00)
	#
	# Set current microsecond to percentage of a full second
	# i.e. xx:xx:xx.886000 886000/1000000 = 0.886 or 88.60% brightness
	led_micro = (now.microsecond/1000000.00)

	######################################################################
	# Concatenate strings to display RGB values in console.
	# xx % : xx % : xx % : xx %
	rgb_time = str(int(round((led_hour*100),0))) +" % : "+ str(int(round((led_minute*100),0))) +" % : "+ str(int(round((led_second*100),0)))  +" % : " + str(int(round((led_micro*100),0)))+" %"
	
	######################################################################
	# write time and percentages to console / stdout with CR/LF
	# 67 % : 73 % : 72 % : 42 %     16:44:43.422
	# stdout.write(dsp_time + "     " + rgb_time +"\r\n")
	stdout.write(rgb_time + "     " + dsp_time +"\r\n")
	stdout.flush()
	
	######################################################################
	# write float values to firmata PWM pins for RGB LED's
	#
	# Red/Green inverse example:
	# as seconds ascend from :00 to :59
	# LED fades from red to green
	#
	r1p.write(1-led_second)
	g1p.write(led_second)
	# b1p.write(led_second)
	#
	# Red/Green inverse example:
	# as microseconds ascend from :xx.000 to :xx.999
	# LED fades from red to green
	#
	r2p.write(1-led_micro)
	g2p.write(led_micro)
	# b2p.write(led_minute)
	#
	#

######################################################################
# Main Loop
#
def main():
	######################################################################
	# Loop Forever
	#
	try:
		while True:
			######################################################################
			# Call get_time function
			#
			get_time()
			#

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

######################################################################
# 		
if __name__ == '__main__':
	main()

#

