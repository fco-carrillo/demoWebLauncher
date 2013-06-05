demoWebLauncher
===============

A python bottle.py implementation for ARM devices, it allows the execution of demos from a web application.


Ownership: 
Francisco Carrillo

Description & Purpose
---------------------

Description:
Normally for Demos, a FAE would create a bash script that helps him go trough the list of demos.

Bash scripts are practical but look very outdated  and unprofessional.

i.MX is capable of running a small web server that gives access to users to run commands from an external 
web browser, which looks nicer and is practical at the same time.


Purpose

Give access to i.MX demo applications from a web platform.


Browser -> Web server => i.MX6 

Background
----------

Board: IMX6QSDB

Web Server: Bottle.py Python minimal server.

Modifications to BSP

In order to be able to execute Bottle.py web server It was needed to install a newer version of Python, 
since Ltib BSP includes 2.4.

Python 2.6 was cross compiled and installed.



Configuration
-------------


To add more demos:

1.	Create/copy  a folder at the demoWebLauncher/demos /  directory,  it can have any name.
2.	Add a file app.xml on that directory you just created, (you can copy it from one of the other demos)
3.	The App file should have a module and the application definition,    If your demo already belongs to a certain module/tab please use the exact same name so it gets classified in the same tab
4.	Add the application name, description, command and route.
5.	If to run your application you need several steps, then create a bash script that execute these steps and call this script from the command that you add on the app.xml   (see the app.xml file created for the mm06 samurai demo)  otherwise call the application directly on the “command”.  See the pinball app.xml as example.


``` 
	Pinball demo app.xml example
	<?xml version="1.0"?>

	<data>
	<module name="OpenGL">
         	<application name="OpenGL bbpinball demo">
         	               <description>OpenGL pinball demo, this demo shows a pinball machine</description>
         	               <command>demos/bbPinball/bbPinball</command>
         	               <route>bbPinball</route>
         	</application>
	</module>
	</data>
``` 

This is an example of one module "OpenGL"  one application that executes the bbpinball demo

The name of the Module is the text that will be in the tab in the web page, normally this will serve to group
different kinds of demos.

The name of the application is the text that will be shown in the web page, it has to be descriptive of what 
the application does.

The command is the line that you will normally execute in the terminal.

The route is a string needed to generate a route where this demo can be accessed directly.

``` 
<application name=.H264 mp4 video play>
                <command>gplay crab.avi &amp;</command>
                <route>/demo1</route>
</application>
``` 



After creating the demo folders with their respective app.xml files, go back to demoWebLauncher folder.

execute the script:

``` 
$python appbrowser.py
``` 

This will add the new demos to the webpage,  they will appear the next time you start the server on the tab/modules you specified in the app.xml files.



After generating the apps.xml file with the required applications then the server can be configured.

In the file server.py modify the line:

``` 
run(host=.xx.xxx.xxx.xxx', port=8080)
``` 

Change the .xx.s  for the ip of the board. (use ifconfig to get this)
Save the file

Start the server with this line:

``` 
$python server.py
``` 

Now you can use a browser to access the web page in the IP you configured in the server.py file

xx.xxx.xxx.xxx:8080/demos












