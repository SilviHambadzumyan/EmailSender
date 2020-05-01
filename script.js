function SubjectCharacters (inputtxt, minlength, maxlength) {
  var field = inputtxt.value;
  var mnlen = minlength;
  var mxlen = maxlength;

  if(field.length <mnlen || field> mxlen.length) { 
    document.getElementById("subjectValid").innerHTML = "We suggest that you keep your subject between " +mnlen+ " and " +mxlen+ " characters";
  } else { 
    document.getElementById("subjectValid").innerHTML = "Looks good!";
  }
}

function sendfunction() {
  console.log("Your email has been sent");
}
