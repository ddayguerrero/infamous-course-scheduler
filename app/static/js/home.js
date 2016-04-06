$( document ).ready(function() {
    var url = window.location.pathname;
    if(url == '/fall/')
    {      
        $.ajax({ //get all the student's fall
            url: '/student_fall_lectures',
            type: 'GET',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $('#courseList').empty();
                $('#courseList').append(HTMLModule.createCourseList(data));
                $('#homeCalendar').append(HTMLModule.createCalendar(data));
            }
        });

    }
    else if(url == '/winter/') //get all the students winter classes
    {
        $.ajax({
            url: '/student_winter_lectures',
            type: 'GET',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $('#courseList').empty();
	           $('#homeCalendar').append(HTMLModule.createCalendar(data));
                $('#courseList').append(HTMLModule.createCourseList(data));
            }
        }); 
    }
    else if(url == '/summer/') //get all the students summer classes
    {
        $.ajax({
            url: '/student_summer_lectures',
            type: 'GET',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $('#courseList').empty();
	           $('#homeCalendar').append(HTMLModule.createCalendar(data));
	           $('#courseList').append(HTMLModule.createCourseList(data));
            }
        }); 
    }
});
