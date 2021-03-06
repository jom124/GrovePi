#!/usr/bin/env python
#
# GrovePi Example for using the Grove Magnetic Switch (http://www.seeedstudio.com/wiki/Grove_-_Magnetic_Switch)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
# LICENSE: 
# These files have been made available online through a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

import time
import grovepi

# Connect the Grove Magnetic Switch to digital port D3
# SIG,NC,VCC,GND
magnetic_switch = 3

grovepi.pinMode(magnetic_switch,"INPUT")

while True:
    try:
        print grovepi.digitalRead(magnetic_switch)
        time.sleep(.5)

    except IOError:
        print "Error"
