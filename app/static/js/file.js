$(function(){
    $('#settakeofftime').click(function(){
        var date = new Date();
        var time = date.getHours() + ":" + date.getMinutes();
        $("#idtakeofftime").val(time);
    });
    
    $('#setlandingtime').click(function(){
        var date = new Date();
        var time = date.getHours() + ":" + date.getMinutes();
        $("#idlandingtime").val(time);
    });
});
