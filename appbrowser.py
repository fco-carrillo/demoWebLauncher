import xml.etree.ElementTree as ET
import os
import demo
import module

path = './demos';


xmlfiles = 	[os.path.join(root,name)
		for root, dirs, files in os.walk(path)
		for name in files
		if name.endswith(('.xml'))]

modules = {};
demos = [];






for xmlapp in xmlfiles:
	#print(xmlapp);
	app_file = open(xmlapp, 'r');

	app_tree = ET.parse(xmlapp);

	app_root = app_tree.getroot();
	
	
	for modulexml in app_root:
		mod = module.Module();
		mod.name = modulexml.get('name');
		#print(mod.name);	        
		mod.demos=[];
		
		# If module already exist we retrieve it here, else we add it.
		mod = modules.setdefault(mod.name,mod);		

		# Add demos to module
		demos = [];
		for appxml in modulexml:
			app = demo.Demo();
			app.name = appxml.get('name');
			#print(app.name);
			app.description = appxml.find('description').text;
			app.route = appxml.find('route').text;
			app.command = appxml.find('command').text;
			demos.append(app)
		
		mod.demos.extend(demos);
	
	app_file.close();
	

#Create main XML
root = ET.Element('data');

for modname,mod in modules.items():
	modxml = ET.SubElement(root, 'module');
        print(mod)
	modxml.set('name', mod.name);
	
	
	for app in mod.demos:
		appxml = ET.SubElement(modxml, 'application');
		appxml.set('name', app.name);
		description = ET.SubElement(appxml, 'description');
		description.text= app.description;

		command = ET.SubElement(appxml, 'command');
		command.text = app.command;

		route = ET.SubElement(appxml, 'route');
		route.text = app.route;


file = open('apps.xml', 'w')

ET.ElementTree(root).write(file);
file.close();





