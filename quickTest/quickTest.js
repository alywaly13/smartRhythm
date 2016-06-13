$(document).ready(function(){
    var firstClick=true;
    var n;
    
    values =[];
    
    var calcStandardDev = function(avg){
        sum = 0;
        n = values.length;
        for (var i=0;i<n; i++){
            sum = sum + (avg-values[i])*(avg-values[i])
        }
        return Math.sqrt(sum/n);
    };
    
    var calcAvg = function(){
        sum = 0;
        n = values.length;
        for (var i=0;i<n; i++){
            sum = sum + values[i]
        }
        return sum/n;
    };
    
    $("#clickme").click(function(){
        if (firstClick){
            var d = new Date();
            n = d.getTime();
            firstClick=false;
        }
        else{
            var nnew = (new Date()).getTime();
            var diff = nnew- n;
            values.push(diff);
            $("#durations").append("<p>" + diff + "</p>");
            n=nnew;
        }
    });
    
    $("#done").click(function(){
        var avg = calcAvg();
        var sd = calcStandardDev(avg);
        $("#Time").html("avg is: " + avg + "  sd is: " + sd);
    });
});

