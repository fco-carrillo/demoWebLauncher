<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<HTML>
   <HEAD>
      	<link rel="stylesheet" href="static/960/code/css/960_12_col.css" type="text/css">
	<link rel="stylesheet" href="static/main.css" type="text/css">
	<script src="static/jquery-1.10.0.min.js"></script>
	<script src="static/webdemos.js"></script>
      <TITLE>
         Freescale i.MX6 Multimedia Demos 
      </TITLE>
   </HEAD>
<BODY>
   	

	
	<div class="container_12" style="font-family: arial,sans-serif;"> 

		<div class="grid_3">
			<img src="static/images/Freescale_logo.jpg" width="210" />
		</div>
		<div class="grid_9" >
			
		</div>
		
		<div class="grid_12" style="background: #e66a08; height: 2em; padding-top: .4em; border: 1px solid #e66a08;">
			
			% for module in modules:

				<div class="grid_2" id="{{ module }}_tab" module="{{ module }}" style="text-align:center; font-weight: 700; color: #51626f;  height: 2em; cursor: pointer; padding: 0.4em 0.4em 0.4em 0;">{{ module }}</div>

			% end


		</div>
		
		<div class="grid_12" id="demo_groups" style="border: 1px solid #b6babf; border-top: 0; ">
				
			% for module in modules:
				
			
			
			<ul class="grid_11" id="{{module}}_list" style="display: none" >
				
				% for app_name in modules[module]:


				<li class="grid_10">
					<div class="grid_5 alpha">
						<div class="grid_4 alpha title"><a href="/demo/{{routes[app_name]}}" target="_blank">{{ app_name }} </a></div>
						<div class="grid_4 omega description"> {{descriptions[app_name]}} </div>
					</div>
					
					<div class="grid_5 omega"><img src="static/images/{{routes[app_name]}}.jpg" width="320" /></div>



					
				</li>
	                        


				% end
				

			</ul>
			
			% end
			
		</div>

		<div class="grid_12 copyright"> © 2004-2013 Freescale Semiconductor, Inc. All rights reserved. </div>

	</div>  

</BODY>
</HTML>
