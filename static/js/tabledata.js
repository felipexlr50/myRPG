var modalTable = document.getElementById("dataTable");

function addDataToTable(form){
    var count = (localStorage.getItem("count")!=null) ? localStorage.getItem("count"):0;
    var newRow = modalTable.insertRow(-1);
    var txtData =  form.elements[0].value;
    var txtLocal = form.elements[1].value;
    var txtValor = form.elements[2].value;
    newRow.insertCell(-1).innerHTML = count++;
    newRow.insertCell(-1).innerHTML = txtData;
    newRow.insertCell(-1).innerHTML = txtLocal;
    newRow.insertCell(-1).innerHTML = txtValor;
    if(window.VR_VALUE.getValue() < 0 || window.VR_VALUE.getValue() - txtValor < 0){
        alert("Saldo insuficiente!");
        return false;
    }else{
        window.VR_VALUE.setValue(window.VR_VALUE.getValue()-txtValor);
        localStorage.setItem("count",count);
        return true;
    } 
}

function saveDataToCookie(){
    var dataJson;
    var myObj = {};
    var myRows = [];
    var $headers = $("th");
    var $rows = $("tbody tr").each(function(index) {
      $cells = $(this).find("td");
      myRows[index] = {};
      $cells.each(function(cellIndex) {
        myRows[index][$($headers[cellIndex]).html()] = $(this).html();
      });    
    });

    myObj.myrows = myRows;
    dataJson = JSON.stringify(myObj);

    if (typeof(Storage) !== "undefined") {
        localStorage.setItem("tableData", dataJson);
        localStorage.setItem("VR_VALUE", window.VR_VALUE.getValue());
        console.log(localStorage.getItem("tableData"));
    }
    else{
        alert("local storage not supported!");
    }
}

function retriveCookieData(){
    var localData = localStorage.getItem("tableData");
    //console.log(localStorage.getItem("tableData"));
    if(localData != "undefined" && localData != null){
        var data = JSON.parse(localData);
        var rows = sortByDate(data.myrows);
        console.log(rows);
        var len = rows.length;
        for(var i=0;i<len;i++){
            var newRow = modalTable.insertRow(-1);
            newRow.insertCell(-1).innerHTML = rows[i]["#"];
            newRow.insertCell(-1).innerHTML = rows[i]["Data"];
            newRow.insertCell(-1).innerHTML = rows[i]["Local"];
            newRow.insertCell(-1).innerHTML = rows[i]["Valor"];
        }
    }   
}

function sortByDate(jsonArray){
    var ret=[];
    var len = jsonArray.length;
    for(var i=1;i<len;i++){
        ret.push({"#":jsonArray[i]["#"],"Data":(new Date(jsonArray[i]["Data"])),
        "Local":jsonArray[i]["Local"],"Valor":jsonArray[i]["Valor"]});
    }
    console.log(ret);
    
    ret.sort(function(a,b){ return a.Data.valueOf() > b.Data.valueOf();});
    
    len = ret.length;
    for(var i=0;i<len;i++){
        var date = ret[i]["Data"];
        console.log(date);
        ret[i]["Data"] = date.getFullYear()+"-"+date.getMonth()+"-"+date.getDate();
    }
    return ret;
}
retriveCookieData();