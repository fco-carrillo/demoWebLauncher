

$(document).ready(function() {
	
	$("ul").first().fadeIn();

	$('div[id*="tab"]').first().addClass("selected");
	

	$('div[id*="tab"]').click( function(){
		
		$(this).addClass("selected");
		$(this).removeClass("unselected");

		$(this).siblings().removeClass("selected");

		$('ul[id*="list"]').fadeOut();
		$( '#'+($(this).attr('module'))+'_list' ).fadeIn();
	} );

});



