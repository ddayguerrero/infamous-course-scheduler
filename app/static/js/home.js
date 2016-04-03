$( document ).ready(function() {
    $('#homeCalendar').append(HTMLModule.createCalendar());
    $('#courseList').append(HTMLModule.createCourseList());

    $("#fall").click(function(e) {
        e.preventDefault()      
        $.ajax({
            url: '/student_fall_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $.each(data.lectures, function(idx, lecture) {
                    console.log(lecture);
              });
            }
        });
    });

    $("#winter").click(function(e) {  
        e.preventDefault()      
        $.ajax({
            url: '/student_winter_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $.each(data.lectures, function(idx, lecture) {
                    console.log(lecture);
              });
            }
        });     
    });

    $("#summer").click(function(e) { 
        e.preventDefault()      
        $.ajax({
            url: '/student_summer_lectures',
            type: 'POST',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                $.each(data.lectures, function(idx, lecture) {
                    console.log(lecture);
              });
            }
        });      
    });
});
