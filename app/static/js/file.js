function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

function validTime(t1, t2) {
    function strToInt(t) {
        return parseInt(t.slice(0, 2)) * 60 + parseInt(t.slice(3))
    }
    if (strToInt(t2) > strToInt(t1)) {
        return true
    } else {
        return false
    }
}

function parsePython(s, cn){
    var info = s.slice(1, -1)
    info = info.replace(/ /g, "")
    sub = info.split(",")
    for (var i = 0; i < sub.length; i++){
        const couple = sub[i].split(":")
        couple[0] = couple[0].slice(1, -1)
        couple[1] = couple[1].slice(1, -1)
        if (couple[0] == cn){
            return couple[1]
        }
    }
}

$(function(){
    $("#cnInput").focusout(function(){
        var cn = $("#cnInput").val();
        var gliders = $("#glidersDict").val();
        var gliderImmat = parsePython(gliders, cn)
        $("#immatInput").val(gliderImmat);
    });

    $("#saveButton").click(function(){
        var start = $("#idtakeofftime").val()
        var end = $("#idlandingtime").val()
        if (validTime(start, end)){
            $("#formSave").submit();
        } else {
            alert("Heure d'arrivée avant le départ.")
        };
    });

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
