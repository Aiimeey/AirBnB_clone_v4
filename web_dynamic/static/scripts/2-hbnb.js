$(document).ready(function(){
    $.get("http://127.0.0.1:5001/2-hbnb", function(data, status){
    $('#api_status').addClass('available');
  }).fail(function() {
    $('#api_status').removeClass('available');
  });    
});
