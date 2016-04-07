$( document ).ready(function() {
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

});