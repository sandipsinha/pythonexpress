/**
 * @author SSINHA
 */
//$().ready(function() { 
	function CheckValidForm(){
	    //This is the autocompleter script to populate the Department field - Begin

                
           $("#name").autocomplete({
	        source: function( request, response ) {
	            $.ajax({
	                url: "/hrtemps/lookup",
	                dataType: "json",
	                data: {'q':$("#name").val()},
	                success: response
	            });
	        },
	        minLength: 1,
	        select: function(event, ui) {
                  var id = ui.item.id;
                  $("#id").val(id);
                  
                 }
	});
  
	}