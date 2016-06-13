#! /usr/bin/python

# Troubleshooting
# Make sure the ref to python in line one /usr/bin/python point to your python directory
# Make sure the file WebInterfaceKit.py is in the cgi-bin /var/www/cgi-bin and executable (run chmod -R /var/www/cgi-bin)

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *

import cgi
import cgitb

cgitb.enable()
errors = ""

# Print the HTML header
print("Content-type: text/html\n\n")
print("<html><title>FULL INTERFACE KIT</title><body>\n")
print('<center><b><font size="16" color="#0000ff">FULL INTERFACEKIT</font></b></center><br>')
print('<font size="4">THIS PROJECT WILL DEVELOP IN A FULL FUNCTIONAL WEB APPLICATION TO CONTROL THE PHIDGETS SBC</font>')
print('<br>&#169 J J Slabbert')
print('<br><a href="mailto:jaco.slabbert@mweb.co.za">jaco.slabbert@mweb.co.za</a><br><br>')

# Create, Open, and Attach the Interface Kit
try:
    ifk = InterfaceKit()
except RuntimeError as e:
    errors = errors + "<h5>Runtime Exception on object creation: " + e.details + "</h5>\n"
try:
    ifk.openPhidget()
except PhidgetException as e:
    errors = errors + "<h5>Phidget Exception on Open: " + e.details + "</h5>\n"
try:
    ifk.waitForAttach(10000)
except PhidgetException as e:
    errors = errors + "<h5>Phidget Exception on Attach: " + e.details + "</h5>\n"
    errors = errors + "<h5>If Phidget is 'Not Physically Attached' it may be in use</h5>\n"

try:
    ifk.setOutputState(5,1)
    print('<font size="16">Digital Output 5 set True</font>')
except:
    print('<font size="16">Error in setting Digital output 5 to True</font>')

print('<br><br><a href="WebInterfaceKit.py">Go back to WebInterfaceKit Main Page. Do not use the browser back button, since the page may not refresh</a>')

print('</body></html>')

ifk.closePhidget()
exit()
