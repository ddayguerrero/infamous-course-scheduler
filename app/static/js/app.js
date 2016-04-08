//////////
// HTTP Requests for searching for courses
//////////
$( document ).ready(function() {
  var url = window.location.pathname;
  var studentCourses;

  if(url == '/change_fall/')
  {
	$.ajax({ //get all the fall courses
   url: '/fall_lectures',
   type: 'GET',
   cache: false,
   dataType: "json",
   error: function(error) {
    console.log("error");
  },
  success: function(data) {
    console.log("success");
    $.each(data.lectures, function(idx, lecture) {
      console.log(lecture.name);
    });
    $('#courseList').empty();
    data.lectures.forEach((d)=>{
      $('#courseList').append(HTMLModule.createSearchList(d));
    });
    displayFallCalendar();//update student's calendar view
  }
});
}
    else if(url == '/change_winter/')//get all the winter classes
    {
     $.ajax({
       url: '/winter_lectures',
       type: 'GET',
       cache: false,
       dataType: "json",
       error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $('#courseList').empty();
        data.lectures.forEach((d)=>{
          $('#courseList').append(HTMLModule.createSearchList(d));
        });
        displayWinterCalendar(); //update student's calendar view
      }
    });
}
  else if(url == '/change_summer/')//get all the summer classes
  {
    $.ajax({
     url: '/summer_lectures',
     type: 'GET',
     cache: false,
     dataType: "json",
     error: function(error) {
      console.log(error);
    },
    success: function(data) {
     $('#courseList').empty();
     data.lectures.forEach((d)=>{
      $('#courseList').append(HTMLModule.createSearchList(d));
      displaySummerCalendar(); //update student's calendar view
    });
   }
   
 });
    }

    var typingTimer;                
    var doneTypingInterval = 250;

    $('#searchBox').keyup(function(){
     clearTimeout(typingTimer);
     if ($('#searchBox').val) {
       typingTimer = setTimeout(doneTyping, doneTypingInterval);
     }
   });

    function doneTyping () {
     var text = $('#searchBox').val();
     if(url == '/change_fall/')
     {
       $.ajax({
        url: '/fall_lectures_search',
        type: 'POST',
        cache: false,
        data: {
          'search' : text
        },
        dataType: "json",
        error: function(error) {
          console.log(error);
        },
        success: function(data) {
          $('#courseList').empty();
          data.lectures.forEach((d)=>{
           $('#courseList').append(HTMLModule.createSearchList(d));
         });
        }
      });
     }
     else if(url == '/change_winter/')
     {
       $.ajax({
        url: '/winter_lectures_search',
        type: 'POST',
        cache: false,
        data: {
          search: text
        },
        dataType: "json",
        error: function(error) {
          console.log(error);
        },
        success: function(data) {
          $('#courseList').empty();
          data.lectures.forEach((d)=>{
           $('#courseList').append(HTMLModule.createSearchList(d));
         });
        }
      });
     }
     else if(url == '/change_summer/')
     {
       $.ajax({
        url: '/summer_lectures_search',
        type: 'POST',
        cache: false,
        data: {
          search: text
        },
        dataType: "json",
        error: function(error) {
          console.log(error);
        },
        success: function(data) {
          $('#courseList').empty();
          data.lectures.forEach((d)=>{
           $('#courseList').append(HTMLModule.createSearchList(d));
         });
        }
      });
     }
   }

   $('#add').click(function(){
     $('#messages').empty();
     var selected = [];
     $('td input:checkbox', $('#table')).each(function() {
       if($(this).is(":checked"))
       {
        selected.push($(this).attr('id'));
      }
    });

     if(selected.length === 0)
     {
       $('#messages').append('<div class="alert alert-warning">No courses were selected.</div>');
     }
     else
     {
       $.each(selected, function(i, id) {
        console.log(id);
        $.ajax({
          url: '/add_lecture',
          type: 'POST',
          cache: false,
          data: {
           lecture_id: id
         },
         error: function(error) {
         },
         success: function(data) {
           $('#messages').append('<div class="alert alert-info" role="alert">' + id + ': ' + data +'</div>');
            if(url == '/change_fall/'){
              displayFallCalendar();
            }
            else if(url == '/change_winter/'){
              displayWinterCalendar();
            }
            else if(url == '/change_summer/'){
              displaySummerCalendar();
            }
         }
       });
      });
     }
   });

   function displayFallCalendar(){
    $.ajax({ //get all the student's fall courses
      url: '/student_fall_lectures',
      type: 'GET',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $('#homeCalendar').empty();
        $('#homeCalendar').append(HTMLModule.createCalendar(data));
      }
    });
  }

   function displayWinterCalendar(){
    $.ajax({ //get all the student's fall courses
      url: '/student_winter_lectures',
      type: 'GET',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $('#homeCalendar').empty();
        $('#homeCalendar').append(HTMLModule.createCalendar(data));
      }
    });
   }

   function displaySummerCalendar(){
      $.ajax({ //get all the student's fall courses
      url: '/student_summer_lectures',
      type: 'GET',
      dataType: "json",
      error: function(error) {
        console.log(error);
      },
      success: function(data) {
        $('#homeCalendar').empty();
        $('#homeCalendar').append(HTMLModule.createCalendar(data));
      }
    });
   }

   $('#delete_course').click(function(){
    $('#delete_messages').empty();
    var selected = [];
    var courses = "";
    $('input:checkbox', $('#courseList')).each(function() {
      if($(this).is(":checked"))
      {
        var id = $(this).attr('id');
        selected.push(id);
        courses += id + "  ";
      }
    });

    if(selected.length === 0)
    {
      $('#delete_messages').append('<div class="alert alert-warning">No courses were selected.</div>');
    }
    else
    {
      var should_delete = confirm("Are you sure you want to delete: " + courses);
      if(should_delete)
      {
        $.each(selected, function(i, id) {
          console.log(id);
          $.ajax({
           url: '/delete_lecture',
           type: 'POST',
           cache: false,
           data: {
             lecture_id: id
           },
           error: function(error) {
             console.log(error);
           },
           success: function(data) {
             console.log(data);
             location.reload();
           }
         });
        });
      }
      else
      {
        $('#delete_messages').append("Delete aborted.");
      }

    }
  });
});

function hoverInLogo(hoveredOver){
	document.getElementById("active").id="oldActive";
	hoveredOver.id="active";
}

function hoverOutLogo(hoveredOver){
	document.getElementById("oldActive").id="active";
	hoveredOver.removeAttribute("id");
}
