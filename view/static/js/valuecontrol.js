
function totalValue(){
    var totalValue = 650.50;
    this.setValue = function(value){
        totalValue = value;
        document.getElementById("totalValue").innerHTML= "R$ " + totalValue;
    }
    this.getValue = function(){return(totalValue);}
}

var VR_VALUE = new totalValue();

function getStoredValue(){
    if(localStorage.getItem("VR_VALUE")!=null){
        var vr = localStorage.getItem("VR_VALUE");
        VR_VALUE.setValue(vr);
    }
    else{
        document.getElementById("totalValue").innerHTML= "R$ " + VR_VALUE.getValue();
    }
}

getStoredValue();
//document.getElementById("totalValue").innerHTML= "R$ " + VR_VALUE.getValue();
 
