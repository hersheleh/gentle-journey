$(document).ready(function() {
    $('body').delegate('button.save', 'click', function() {
	var tag = $(this).data('tag');
	var text = $('#'+tag).html();

	$.post($SCRIPT_ROOT + '/edit/update_text',
	       { text : text,
		 tag : tag },
	       function(data) {}
	      );
    });
});

$(document).ready(function() {

    $('body').delegate('button.facial-edit', 'click', function() {
	edit_service('facial', 'edit', id=$(this).data('id'));

    });

    $('body').delegate('button.facial-delete','click', function() {
	if(confirm('Are you sure you want to delete?')) {
	    edit_service('facial','delete', id=$(this).data('id'));
	}

    });
    
    $('body').delegate('button.wax-edit','click',function() {
	edit_service('waxing','edit',id=$(this).data('id'));
    });
    
    $('body').delegate('button.wax-delete','click',function() {
	if(confirm('Are you sure you want to delete?')) {
	    edit_service('waxing','delete',id=$(this).data('id'));
	}
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
	       window.location.reload();
	   });
}
