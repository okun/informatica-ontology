//page loading:
$(document).ready(function(){
    var loadTree = $SCRIPT_ROOT + 'gettree';
    $.ajax({ type:'GET',
             url:loadTree, //'http://127.0.0.1:5000/gettree',
             success: function(data){
                //createTree(data);
                console.log(data);
                } 
            });//end of ajax
    
});
function createTree(data){
    nodesData = data.results.bindings;
    $("#onto-tree").jstree();
}//end of createTree
