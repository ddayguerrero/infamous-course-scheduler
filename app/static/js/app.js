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
  $('#addCourse').click(function(){
    var inputCourse = $('input[name="courseSearch"]').val()
    $.ajax({
      url: '/courses',
      data: {
        course: inputCourse
      },
      error: function(error) {
        console.log(error)
      },
      success: function(data) {
        $("#courseIdNum").html(data.id)
        $("#courseName").html(data.name)
        $("#startTime").html(data.startTime)
        $("#endTime").html(data.endTime)
        $("#instructor").html(data.instructor)
      },
      type: 'POST'
    });
  });
});
