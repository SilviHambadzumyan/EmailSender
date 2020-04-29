function SubjectCharacters (inputtxt, minlength, maxlength) {
var field = inputtxt;
document.getElementById("subject").innerHTML = field; 
var mnlen = minlength;
var mxlen = maxlength;

if(field.length <mnlen || field> mxlen.length)
{ 
console.log("We suggest that you keep your subject between " +mnlen+ " and " +mxlen+ " characters");
}
}

function sendfunction() {
  alert("Your email has been sent");
}
