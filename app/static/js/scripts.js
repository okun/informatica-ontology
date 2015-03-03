//page loading:
$(document).ready(function(){
    //$SCRIPT_ROOT={{ request.script_root|tojson|safe }};
    $.ajax({ type:'GET',
               url:'http://127.0.0.1:5000/gettree',
            success: function(data){
            console.log(data);} });
    $("#onto-tree").jstree();
});
