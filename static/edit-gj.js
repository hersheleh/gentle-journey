/* This file contains code that works on text fields. 
   They change the value of the text-area / field to display 
   instructions. 
*/

$(document).ready(function() {
    $('.service-body').removeAttr('hidden');
});

$(document).ready(function() {
    $('input[type=text], textarea').focus(function() {
	if(this.value == this.defaultValue) {
	    $(this).val('');
	}
    });
    
    $('input, textarea').blur(function() {
	if(this.value == '') {
	    $(this).val(this.defaultValue);
	}
    }); 
});

