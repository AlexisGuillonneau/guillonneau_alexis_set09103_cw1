$(document).ready(function(){

    		function sortItem(selectedActor,selectedYear){
    			if(selectedActor=="All" && selectedYear=="All"){
    				$('.portfolio-item').show();
    			}else if(selectedActor=="All" && selectedYear!="All"){
    				$('.portfolio-item').hide();
    				$('.portfolio-item').each(function(){
    					if($(this).data('year')==selectedYear+".0"){
    						$(this).show();
    					}
    				});
    			}else if(selectedActor!="All" && selectedYear=="All"){
    				$('.portfolio-item').hide();
    				$('.portfolio-item').each(function(){
    					if($(this).data('actors').indexOf(selectedActor)!=-1){
    						$(this).show();
    					}
    				});
    			}else{
    				$('.portfolio-item').hide();
    				$('.portfolio-item').each(function(){
    					if($(this).data('actors').indexOf(selectedActor)!=-1 && $(this).data('year')==selectedYear+".0"){
    						$(this).show();
    					}
    				});
    			}
    		}
    		
    		$('#inputYear').click(function(){
    			
    			var selectedYear = $(this).find(':selected').text();
    			var selectedActor = $('#inputActors').find(':selected').text();
    			sortItem(selectedActor,selectedYear);
    		});

    		$('#inputActors').click(function(){
    			var selectedActor = $(this).find(':selected').text();
    			var selectedYear = $('#inputYear').find(':selected').text();
    			sortItem(selectedActor,selectedYear);

    		});
    	})