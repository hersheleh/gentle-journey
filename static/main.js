$(document).ready(function() {
		$('#front-page').fadeIn(1000);
});

/*$(document).ready(function() {
    $('.service-body').attr('hidden', 'true');
});*/


$(document).ready(function() {
    $('#main').delegate(".service","click", function() {
	// Show the appointment message
	/*var serv = $(this).find('.service-title').html();
	$('.reminder').html(serv);
	$('.appointment').hide().fadeIn(800)*/

	
	if($(this).children('.service-body').is(':hidden')) {
	    // Fade out and slide up any open service-body
	    $('.service-body').
		slideUp(800).
		animate(
		    { opacity:0 },
		    { queue: false, duration: 800 });
	    
	    // Fade in and slide down the selected service-body
	    $(this).children('.service-body').
		css('opacity', '0').
		slideDown(800).
		animate(
		    { opacity: 1 },
		    { queue: false, duration: 800 });
	}
	else {
	    // Fade out and slide up the selected service body
	    $(this).children('.service-body').		
		slideUp(800).
		animate(
		    { opacity:0 },
		    { queue: false, duration: 800 });
	}
    });
});