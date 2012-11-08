Aloha.settings = {
    floatingmenu: {
	width:50,
	pin:false,
    },
    plugins: {
	format: {
	    config : ['b','i']
	}
    }
}

Aloha.ready( function() {
    Aloha.jQuery('.service-title').aloha();
    Aloha.jQuery('.service-body').aloha();
    Aloha.jQuery('.service-price').aloha();
    Aloha.jQuery('#phone-number').aloha();
    Aloha.jQuery('#address').aloha();
});



