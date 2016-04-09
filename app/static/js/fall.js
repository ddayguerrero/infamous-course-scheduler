$( document ).ready(function() {
	$.ajax({ //get all the student's fall
    	url: '/student_fall_lectures',
        type: 'GET',
        dataType: "json",
        error: function(error) {
            },
            success: function(data) {
		$('#courseList').empty();
		if(data.lectures.length === 0){
		    $('#courseList').append('<div class="well">You are currently not registered for any courses this semester.</div>');
		}
                $('#courseList').append(HTMLModule.createCourseList(data));
                $('#homeCalendar').append(HTMLModule.createCalendar(data));

            }

        });

});
