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
    ifk.openRemoteIP('192.168.10.106',5001)
except PhidgetException as e:
    errors = errors + "<h5>Phidget Exception on Open: " + e.details + "</h5>\n"
try:
    ifk.waitForAttach(10000)
except PhidgetException as e:
    errors = errors + "<h5>Phidget Exception on Attach: " + e.details + "</h5>\n"
    errors = errors + "<h5>If Phidget is 'Not Physically Attached' it may be in use</h5>\n"

print('<table><tr><td>')


# Generating the Sensor Value Table
print('<b>Analog Sensor Values</b>')
print('<table border="1"><tr><td>Sensor Number</td><td>Sensor Value</td></tr>\n')

for i in range (0,8):
    try:        
        print ('<tr><td>'+str(i)+'</td><td>'+str(ifk.getSensorValue(i))+'</td></tr>\n')
    except:
        pint('<tr><td>'+str(i)+'</td><td>Could not Read Censor Value </td></tr>\n')    
print('</table></td><td>')

#Print the Digital Input values
print('<b>Digital Input Values</b>')
print('<table border="1"><tr><td>Input Number</td><td>Input Value</td></tr>\n')

for i in range (0,8):
    try:
        print ('<tr><td>'+str(i)+'</td><td>'+str(ifk.getInputState(i))+'</td></tr>\n')
    except:
        pint('<tr><td>'+str(i)+'</td><td>Could not Read Digital Input State </td></tr>\n')
print('</table></td><td>')

#Print the Digital Output States
print('<b>Digital Output States</b>')
print('<table border="1"><tr><td>Output Number</td><td>Output State</td><td>Set True</td><td>Set False</td></tr>\n')

for i in range (0,8):
    try:
        print ('<tr><td>'+str(i)+'</td><td>'+str(ifk.getOutputState(i))+'</td><td><a href="SetTrue'+str(i)+'.py">Set True</a></td><td><a href="SetFalse'+str(i)+'.py">Set False</a></td></tr>\n')
    except:
        pint('<tr><td>'+str(i)+'</td><td>Could not Read Digital Outputt State </td></tr>\n')
print('</table></td></tr></table>')

print ('<br><br>This page does not automaticly refresh')
print ('<br><br><a href="WebInterfaceKit.py">Refresh this page</a>')
print('</body></html>\n')
 
ifk.closePhidget()
exit(0)
