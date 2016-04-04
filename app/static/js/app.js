function hoverInLogo(){
  document.getElementById("nav-logo").src="../../static/images/NullPointer-noarrow.png";
}

function hoverOutLogo(){
  document.getElementById("nav-logo").src="../../static/images/NullPointer.png";
}

//////////
// HTTP Requests for searching for courses
//////////
$( document ).ready(function() {
  var url = window.location.pathname;
  console.log(url);
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
        $.each(data.lectures, function(idx, lecture) {
          $('#table tr:last').after('<tr>' + 
            '<td>' + lecture.section + '</td>' + 
            '<td>' + lecture.name + '</td>' + 
            '<td>' + lecture.start_time + '</td>' + 
            '<td>' + lecture.end_time + '</td>' + 
            '<td>' + lecture.instructor + '</td>' +
            '<td><input type="checkbox" value="class1"></td></tr>');
        });
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
        $.each(data.lectures, function(idx, lecture) {
          $('#table tr:last').after('<tr>' + 
            '<td>' + lecture.section + '</td>' + 
            '<td>' + lecture.name + '</td>' + 
            '<td>' + lecture.start_time + '</td>' + 
            '<td>' + lecture.end_time + '</td>' + 
            '<td>' + lecture.instructor + '</td>' +
            '<td><input type="checkbox" value="class1"></td></tr>');
        });
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
        $.each(data.lectures, function(idx, lecture) {
          $('#table tr:last').after('<tr>' + 
            '<td>' + lecture.section + '</td>' + 
            '<td>' + lecture.name + '</td>' + 
            '<td>' + lecture.start_time + '</td>' + 
            '<td>' + lecture.end_time + '</td>' + 
            '<td>' + lecture.instructor + '</td>' +
            '<td><input type="checkbox" value="class1"></td></tr>');
        });
      }
    });
  }
});
