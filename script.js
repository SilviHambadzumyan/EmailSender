function SubjectCharacters (inputtxt, minlength, maxlength) {
var field = inputtxt.length;
document.getElementById("subject").innerHTML = field; 
var mnlen = minlength;
var mxlen = maxlength;

if(field<mnlen || field> mxlen)
{ 
console.log("We suggest that you keep your subject between " +mnlen+ " and " +mxlen+ " characters");
}
}

function sendfunction() {
  alert("Your email has been sent");
}
