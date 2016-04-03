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
  $('#add_course').click(function(e) {
    e.preventDefault();

    console.log($('.active_page').attr('id'));
    console.log("hello");
    if($('.ui-page-active').attr('id') == 'fall') 
    {
      $.ajax({
      url: '/',
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
    else if($('.ui-page-active').attr('id') == 'winter')
    {
      $.ajax({
      url: '/',
      type: 'POST',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $.each($.parseJSON(data), function(idx, obj) {
          
        });
      }
    });
    }
    else if($('.ui-page-active').attr('id') == 'summer')
    {
      $.ajax({
      url: '/',
      type: 'POST',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $.each($.parseJSON(data), function(idx, obj) {
          
        });
      }
    });
    }
  });
});
