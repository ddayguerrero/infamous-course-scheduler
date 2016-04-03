$( document ).ready(function() {

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
                console.log(typeof(data));
            $.each(data.lectures, function(idx, lecture) {
                console.log(lecture);
              });
              $('#courseList').append(HTMLModule.createCourseList(data));
              $('#homeCalendar').append(HTMLModule.createCalendar(data));
            }
        });
    });

    $("#winter").click(function() {       
    });

    $("#summer").click(function() {       
    });
});
