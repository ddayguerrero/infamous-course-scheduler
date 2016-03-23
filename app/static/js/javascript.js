/* global $ */
/*function validatePass(str){
  if(!(/[0-9]/.test(str))){
    alert("Password must contain atleast one number")
    return false;
  }
  if(!(/[a-z]/.test(str))){
    alert("Password must contain atleast one lowercase letter")
    return false;
  }
  if(!(/[A-Z]/.test(str))){
    alert("Password must contain atleast one uppercase letter")
    return false;
  }
  if(str.length < 6 || str.length > 16){
    alert("Password must contain a minimun of 6 character and a maximum of 16 characters")
    return false;
  }
  if(!(/^\w+$/.test(str))){
    alert("Password cannot contain special characters")
    return false;
  }
  return true;
}

function checkPass(){
  if(!validatePass(document.getElementById('password').value)){
    alert("Unvalid password")
  }
}

function confirmSame(){
  if(document.getElementById('password').value != document.getElementById('confirmPass').value){
    alert("The passwords are not the same");  
  }
}*/

function hoverInLogo(){
  document.getElementById("nav-logo").src="../../static/images/NullPointer-noarrow.png";
}

function hoverOutLogo(){
  document.getElementById("nav-logo").src="../../static/images/NullPointer.png";
}
// function changeActivelink(obj){
// 	document.getElementById("active").id= "";
// 	obj.id="active";
// }
/* NEEDS FIXING
function setUpLinks(){
	alert("inside setup");
	var links = document.getElementsByClassName("navlink");
	alert("passed links");
	for(i = 0; i < links.length; i++){
		links[i].addEventListener("click",changeActivelink());
	}
	alert("finished assigning");
}*/

//////////
// HTTP Requests Actions
//////////
$( document ).ready(function() {

$('#addCourse').click(function(){
    $.ajax({
        url: 'http://localhost:5000/courses',
        data: {
            format: 'text'
        },
        error: function() {
            alert("fail");
        },
        dataType: 'jsonp',
        success: function(data) {
            console.log(typeof(data));
        },
        type: 'GET'
    });
});

});