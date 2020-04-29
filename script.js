function SubjectCharacters (inputtxt, minlength, maxlength) {
var field = inputtxt.value;
var mnlen = minlength;
var mxlen = maxlength;

if(field.length <mnlen || field> mxlen.length)
{ 
alert("We suggest that you keep your subject between " +mnlen+ " and " +mxlen+ " characters");
}
else
{ 
alert('Your subject line looks great!');
return true;
}
}

function sendfunction() {
  alert("Your email has been sent");
}

