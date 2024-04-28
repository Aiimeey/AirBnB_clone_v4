$(document).ready(function(){
    var Dict = {}
    $('input[type="checkbox]').change(function(){
        var amenityId= $(this).attr('data-id');

        if ($(this).is(':checked')) {
            Dict[amenityId]=true;

        }else {
            delete Dict[amenityId];
        }
        var List = object.keys(Dict).join(', ');
        $('#amenities h4').text('Amenities: ' + List);
    })
});
