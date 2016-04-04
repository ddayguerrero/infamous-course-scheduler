//////////
// HTTP Requests for searching for courses
//////////
$( document ).ready(function() {
  var url = window.location.pathname;
  if(url == '/change_fall/')
  {
    $.ajax({
      url: '/fall_lectures',
      type: 'POST',
      dataType: "json",
      error: function(error) {
          console.log(error);
      },
      success: function(data) {
	  HTMLModule.createSearchList(data);
      }
    });
  }
  else if(url == '/change_winter/')
  {
    $.ajax({
      url: '/winter_lectures',
      type: 'POST',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        HTMLModule.createSearchList(data);
      }
    });
  }
  else if(url == '/change_summer/')
  {
    $.ajax({
      url: '/summer_lectures',
      type: 'POST',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        HTMLModule.createSearchList(data);
      }
    });
  }

    function hoverInLogo(){
	document.getElementById("nav-logo").src="../../static/images/NullPointer-noarrow.png";
    }

    function hoverOutLogo(){
	document.getElementById("nav-logo").src="../../static/images/NullPointer.png";
    }

});
