$(document).ready(function() {
    $('body').delegate('button.save', 'click', function() {
	var text = $('').html()
	var tag = $('').attr('id')
	$.post($SCRIPT_ROOT + '/update_text',
	       { text : text,
		 tag : tag },
	       function(data) {}
	      );
    });
});


$(document).ready(function() {
    
});