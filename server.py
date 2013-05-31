import os
from bottle import route, run, template, static_file
from bottle import view

import xml.etree.ElementTree as ET

tree = ET.parse('apps.xml')
root = tree.getroot()


command_dict = dict()
route_dict = dict()
module_dict = dict()
des_dict = dict()


for module in root:
	app_list = [];
	for app in module:
		app_list.append(app.get('name'))
		command_dict[app.get('name')]=app.find('command').text;
                route_dict[app.get('name')]=app.find('route').text;
		des_dict[app.get('name')]=app.find('description').text;

	module_dict[module.get('name')]=app_list


print module_dict
print route_dict
print command_dict

#for child in root:

#	command_dict[child.get('name')]=child.find('command').text;
#	route_dict[child.get('name')]=child.find('route').text;


@route('/demos')
def index():
    return template('demos', modules=module_dict, commands=command_dict, routes=route_dict, descriptions=des_dict)

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{ope}} {{blu}}</b>!', ope=name, blu=name )


#for module in root:
#	for app in module:
#		@route(app.find('route').text)
#		def index(name='file'):
#			print(app.find('command').text)
#   			os.system(app.find('command').text)


@route('/demo/<application>')
def execute_application(application):
	#print (application);
	command = "echo NO COMMAND FOUND"
	name = "NO NAME FOUND"
        
        for module in root:
	        for app in module:
			#print(app.get('name'));
			route = app.find('route').text;
			#print( route);
			if (route == application):
				command =  app.find('command').text;	
				name = app.get('name');
				break;


	os.system(command);
	print(name);
	return template('executing', demo_name=name, demo_route=application);


#for child in root:
#	@route(child.find('route').text)
#	def index(name='file'):
 #   		os.system(child.find('command').text)

    

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='10.112.102.116', port=8080)


