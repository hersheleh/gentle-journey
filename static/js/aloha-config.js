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
    Aloha.jQuery('#phone-number').aloha();
    Aloha.jQuery('#address').aloha();
});



