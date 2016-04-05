//////////
// HTTP Requests for searching for courses
//////////
$( document ).ready(function() {
  var url = window.location.pathname;
  if(url == '/change_fall/')
  {
    $.ajax({
      url: '/fall_lectures',
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
      }
    });
  }
  else if(url == '/change_winter/')
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
      }
    });
  }
  else if(url == '/change_summer/')
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
    var selected = [];
    $('td input:checkbox', $('#table')).each(function() {
        if($(this).is(":checked"))
        {
          selected.push($(this).attr('id'));
        }
    });

    if(selected.length === 0)
    {
      alert('no courses were selected');
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
            console.log(error);
          },
          success: function(data) {
            console.log(data);
          }
        });
      });
    }
  });



  function hoverInLogo(){
	     document.getElementById("nav-logo").src="../../static/images/NullPointer-noarrow.png";
    }

    function hoverOutLogo(){
	     document.getElementById("nav-logo").src="../../static/images/NullPointer.png";
    }

});
