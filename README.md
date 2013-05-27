demoWebLauncher
===============

A python bottle.py implementation for ARM devices, it allows the execution of demos from a web application.


Ownership: 
Francisco Carrillo

DESCRIPTION & PURPOSE

Description:
Normally for Demos, a FAE would create a bash script that helps him go trough the list of demos.

Bash scripts are practical but look very outdated  and unprofessional.

i.MX is capable of running a small web server that gives access to users to run commands from an external 
web browser, which looks nicer and is practical at the same time.


Purpose

Give access to i.MX demo applications from a web platform.


Browser -> Web server => i.MX6 

Background

Board: IMX6QSDB

Web Server: Bottle.py Python minimal server.

Modifications to BSP

In order to be able to execute Bottle.py web server It was needed to install a newer version of Python, 
since Ltib BSP includes 2.4.

Python 2.6 was cross compiled and installed.



CONFIGURATION

In order to add applications easily, it is only needed to edit apps.xml file.

//TODO * 
It is planned to create a script that automatcally fills this apps.xml files from the folders contained in
demos path.
//

'''xml
<?xml version="1.0"?>
<data>
        <module name="gstreamer">
       		 <application name=.H264 mp4 video play>
                	<command>gplay crab.avi &amp;</command>
                	<route>/demo1</route>
        	</application>
       	 	<application name=. Qt5 OpenGL Under QML">
                	<command>/opt/qt5/examples/quick/scenegraph/openglunderqml/openglunderqml </command>
                	<route>/demo2</route>
        	</application>
        </module>
</data>

This is an example of one module "demos"  two applications, one reproduces video, the other executes a Qt5 
application.

The name of the Module is the text that will be in the tab in the web page, normally this will serve to group
different kinds of demos.

The name of the application is the text that will be shown in the web page, it has to be descriptive of what 
the application does.

The command is the line that you will normally execute in the terminal.

The route is a string needed to generate a route where this demo can be accessed directly.

<application name=.H264 mp4 video play>
                <command>gplay crab.avi &amp;</command>
                <route>/demo1</route>
</application>




After filling the xml file with the required applications then the server can be configured.
In the file server.py modify the line:
run(host=.xx.xxx.xxx.xxx', port=8080)
Change the .xx.s  for the ip of the board. (use ifconfig to get this)
Save the file

Start the server with this line:
$python server.py


Now you can access the web page in the IP you configured

xx.xxx.xxx.xxx:8080/demos


And you will see the list of demos in the browser.













