function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

$(function(){
    $("#supprButton").click(function(){
        if (confirm("Voulez vous vraiment supprimer ce vol ?")){
            $("#formSuppr").submit();
        };
    });

    $('#settakeofftime').click(function(){
        var date = new Date();
        var hour = checkTime(date.getHours());
        var min = checkTime(date.getMinutes());
        var time = hour + ":" + min;
        $("#idtakeofftime").val(time);
    });

    $('#setlandingtime').click(function(){
        var date = new Date();
        var hour = checkTime(date.getHours());
        var min = checkTime(date.getMinutes());
        var time = hour + ":" + min;
        $("#idlandingtime").val(time);
    });

});
