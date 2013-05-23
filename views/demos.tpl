<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<HTML>
   <HEAD>
      	<link rel="stylesheet" href="static/960/code/css/960_12_col.css" type="text/css">
	<link rel="stylesheet" href="static/main.css" type="text/css">
      <TITLE>
         Freescale i.MX6 Multimedia Demos 
      </TITLE>
   </HEAD>
<BODY>
   	

	
	<div class="container_12" style="font-family: arial,sans-serif;"> 

		<div class="grid_3">
			<img src=static/Freescale_logo.jpg width=210>
		</div>
		<div class="grid_9" >
			
		</div>
		
		<div class="grid_12" style="background: #e66a08; height: 2em; padding-top: .4em; border: 1px solid #e66a08;">
			<div class="grid_3" style="text-align:center; font-weight: 700; color: #51626f; background: white; height: 2em; cursor: pointer; padding: 0.4em 0.4em 0.4em 0;">Multimedia Demos</div>
		</div>
		
		<div class="grid_12" style="border: 1px solid #e66a08; border-top: 0; ">
				
			% for module in modules:
				
			
			
			<ul class="grid_11">
				<li>{{ module }}</li>
				% for app_name in modules[module]:
				<li><a href="{{routes[app_name]}}" target="_blank">{{ app_name }} </a></li>
	                        % end
				

			</ul>
			
			% end
			
		</div>

	</div>  

</BODY>
</HTML>
