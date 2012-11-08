$(document).ready(function() {
    $('body').delegate('button.save', 'click', function() {
	var text = $('').html()
	var tag = $('').attr('id')
	$.post($SCRIPT_ROOT + '/edit/update_text',
	       { text : text,
		 tag : tag },
	       function(data) {}
	      );
    });
});

$(document).ready(function() {

    $('body').delegate('button.edit', 'click', function() {
	edit_service('facial', 'edit', id=$(this).data('id'));
    });

    $('body').delegate('button.delete', 'click', function() {
	edit_service('facial', 'delete');
    });
    
});


function edit_service(tag, action, id) {
    var service = $('.service[data-id='+id+']');
    var title = service.find('.service-title').html();
    var body = service.children('.service-body').html();
    var price = service.find('.service-price').html();
    
    $.post($SCRIPT_ROOT + '/edit/edit_service', 
	   { id : id,
	     title : title,
	     body : body,
	     price : price,
	     tag : tag,
	     action : action }, 

	   function() {
	   });
}
