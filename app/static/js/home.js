$( document ).ready(function() {
    var url = window.location.pathname;
    console.log(url);
    if(url == '/fall/')
    {      
        $.ajax({
            url: '/student_fall_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $("#fall").unbind('click');
                $.each(data.lectures, function(idx, lecture) {
                    console.log(lecture);
		});
            $('#homeCalendar').append(HTMLModule.createCalendar(data));
            $('#courseList').append(HTMLModule.createCourseList(data));
            }
        });
    }
    else if(url == '/winter/')
    {
        $.ajax({
            url: '/student_winter_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $("#winter").unbind('click');
                $.each(data.lectures, function(idx, lecture) {
                    console.log(lecture);
              });
            }
        }); 
    }
    else if(url == '/summer/')
    {
        $.ajax({
            url: '/student_summer_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $("#summer").unbind('click');
                $.each(data.lectures, function(idx, lecture) {
                    console.log(lecture);
              });
            }
        }); 
    }
});
