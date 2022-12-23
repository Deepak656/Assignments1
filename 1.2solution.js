
// Using the elements and forms arrays of the Document object
Suppose you had a piece of code as below

<form action="blah.php"> 
     <input type="button" name="someButton" /> 
</form>

// So you could access the button as:
var something = document.forms[0].elements[0]; 


// Using element names
Suppose you had a piece of code as below

<form name="blahForm" action="blah.php" /> 
      <input type="button" name="blahButton" /> 
</form> 

//So you could access the button as:
var something = document.blahForm.blahButton; 

Source : https://qr.ae/prhvsL

