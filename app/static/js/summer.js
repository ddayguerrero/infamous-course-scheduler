$( document ).ready(function() {
    $.ajax({
        url: '/student_summer_lectures',
        type: 'GET',
        dataType: "json",
        error: function(error) {
            },
            success: function(data) {
            $('#courseList').empty();
		if(data.lectures.length === 0){
		    $('#courseList').append('<div class="well">...</div>');
		}
            $('#homeCalendar').append(HTMLModule.createCalendar(data));
            $('#courseList').append(HTMLModule.createCourseList(data));
            }
    });

});
