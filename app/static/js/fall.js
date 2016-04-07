$( document ).ready(function() {
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

});