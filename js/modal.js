// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("btnAdd");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var btnSalvar = document.getElementById("btnSalvar");



var form = document.getElementById("modalForm");



// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

var count = 0;
var diff = 0;

btnSalvar.onclick = function(){
    if(window.addDataToTable(form))
        window.saveDataToCookie();
      //  window.retriveCookieData();
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
   // window.retriveCookieData();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
       // window.retriveCookieData();
    }
}

