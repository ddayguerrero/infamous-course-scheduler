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
  $('#addCourse').click(function(e) {
    
    e.preventDefault();
    $.ajax({
      url: '/',
      type: 'POST',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $.each($.parseJSON(data), function(idx, obj) {
          $('#table tr:last').after(
            '<tr>' +
              '<td>' + data.id + '<td>' +
              '<td>' + data.name + '<td>' +
            '<tr>')
        });
      }
    });
  });
});
