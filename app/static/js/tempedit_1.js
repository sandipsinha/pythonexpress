
     function  DoHousekeeping()
     {
	      $('#effdt').datepicker({dateFormat:"yy-mm-dd",changeMonth:'true',changeYear:'true',showButtonPanel:'true'});
	      $('#it_end_date').datepicker({dateFormat:"yy-mm-dd",changeMonth:'true',changeYear:'true',showButtonPanel:'true'});

	      $(".chzn-select").slideUp();
	      $(".chzn-select").chosen();
	      $(".mailr").slideUp();    	
	    	$("#mgr").autocomplete({
	        source: function( request, response ) {
	            $.ajax({
	                url: "/hrtemps/mgrlookup",
	                dataType: "json",
	                data: {'q':$("#mgr").val()},
	                success: response
	            });
	        },
	        minLength: 1,
	        select: function(event, ui) {
                  var mgr_data = ui.item.id.split(';');
                  $("#bossid").val(mgr_data[0]);
                  $("#dept").val(mgr_data[3]);
                  $("#location").val(mgr_data[1]);
                  $("#legal").val(mgr_data[2]);
                 }
			});
	
			$("#hr_name").autocomplete({
			        source: function( request, response ) {
			        $.ajax({
			                url: "/hrtemps/hrinq",
			                dataType: "json",
			                data: {'q':$("#hr_name").val()},
			                success: response
			               });
			        									  },
					        minLength: 1,
					        select: function(event, ui) {
				                  var id = ui.item.id;
				                  $("#hr_contact").val(id);
				                  
				                 }
				});
				
							
		    $("#finance").autocomplete({
			        source: function( request, response ) {
			            $.ajax({
			                url: "/hrtemps/finlookup",
			                dataType: "json",
			                data: {'q':$("#finance").val()},
			                success: response
			            });
			        },
			        minLength: 1
			});				
							
		if ($("#action_type").val() == 'cnv' || $("#act_type").val() == 'cnv'){
	    	$("#emplid").show();
	    	$('label[for="emplid"]').show();
	    }
	    else
	    { 	
	        $("#emplid").slideUp();
	        $('label[for="emplid"]').slideUp();
	    }				
	  }
						
		function populatehr() {

			var str = $("#hr_contact").val();
	   	    $.getJSON('/hrtemps/gethr', {
			        q:str 
			      }, function(data) {
	
			        $("#hr_name").val(data.value);
			      });
            
            var str = $("#supervisor").val();
   	    	$.getJSON('/hrtemps/gethr', {
		        q:str 
		      }, function(data) {

		        $("#mgr").val(data.value);
		      });
		      
		    }
		    
     		   

