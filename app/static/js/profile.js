$(function () {
    $('.list-group .list-group-item').each(function () {
        
        // Settings
        var $widget = $(this),
            $checkbox = $('<input type="checkbox" class="hidden" />'),
            color = ($widget.data('color') ? $widget.data('color') : "primary"),
            style = ($widget.data('style') == "button" ? "btn-" : "list-group-item-"),
            settings = {
                on: {
                    icon: 'glyphicon glyphicon-check'
                },
                off: {
                    icon: 'glyphicon glyphicon-unchecked'
                }
            };
            
        $widget.css('cursor', 'pointer')
        $widget.append($checkbox);

        // Event Handlers
        $widget.on('click', function () {
            $checkbox.prop('checked', !$checkbox.is(':checked'));
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });
          

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');
            $widget.data('state', (isChecked) ? "on" : "off");
            $widget.find('.state-icon')
                .removeClass()
                .addClass('state-icon ' + settings[$widget.data('state')].icon);
            // Update colour
            if (isChecked) {
                $widget.addClass(style + color + ' active');
            } else {
                $widget.removeClass(style + color + ' active');
            }
        }
    });
});

$( document ).ready(function()
{
    var url = window.location.pathname;
    if(url == '/home/')
    {
        $.ajax({ //get all the student's fall
            url: '/student_completed_courses',
            type: 'GET',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                data.courses.forEach((d)=>{
                    $('#completedCourses').append('<li class="list-group-item" data-color="success">' +
                        '<input type="checkbox" id=' + d.program + d.number + '>' + d.program + d.number + '</li>');
                });
            }
    });

    $.ajax({ //get all the student's fall
            url: '/student_registered_courses',
            type: 'GET',
            dataType: "json",
            error: function(error) {
                console.log(error);
            },
            success: function(data) {
                data.courses.forEach((d)=>{
                    $('#registeredCourses').append('<li class="list-group-item" data-color="success">' +
                        '<input type="checkbox" id=' + d.program + d.number + '>' + d.program + d.number + '</li>');
                });
            }
        });
    }
});
