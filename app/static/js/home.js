$( document ).ready(function() {
    $('#homeCalendar').append(HTMLModule.createCalendar());
    $('#courseList').append(HTMLModule.createCourseList());

    $("#fall").click(function(e) {
        e.preventDefault()      
        $.ajax({
            url: '/fall_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                console.log(data);
            }
        });
    });

    $("#winter").click(function() {       
    });

    $("#summer").click(function() {       
    });
});
