$(document).ready(function() {
    $('.service-body').removeAttr('hidden');
});

$(document).ready(function() {
    $('input, textarea').focus(function() {
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

