/* This function is loaded when an Administrator logs into a site
   It pulls information from the html page and sends via ajax on 
   click
*/

/* This ajax request pulls data that is saved and labeled as text
   It sends data that edits miscellaneous html throughout the page
*/
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

/* This document.ready section sets functionality to different 
   buttons with diffent properties. You'll notice the differences
   in the name. eg(facial-edit and facial-delete) 
*/
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

/* This function sends an ajax request to edit data in the 
   service table. The action specified will determine what sort
   of request is being sent over eg.(delete, edit, add)
*/
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
