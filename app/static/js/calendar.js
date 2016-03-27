function tableCreate(){
    var parent = document.getElementById("calendar-location"); 
    var tbl  = document.createElement('table');
    var header = tbl.createTHead();
    let daysOfWeek = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    var row, cell;

    var createCells = function(days){
	row = header.insertRow(0);
	row.insertCell(0);
	for (var i = 0; i < days.length ; i++){
	    cell = row.insertCell(i+1);
	    cell.innerHTML = days[i];
	}
    }

    var createTimeSlots = function(){
	var tr, td, min, hour;
	for (var i = 0; i < 52; i++){
	    tr = tbl.insertRow();
	    for (var j = 0; j < 8; j++){
		td = tr.insertCell();
		if(j==0){
		    hour = 8+Math.floor(i/4);
		    min = (i%4)*15;
		    if(min!=0)
			td.appendChild(document.createTextNode(hour+":"+min));
		    else
			td.appendChild(document.createTextNode(hour+":00")); // min would only be 0 instead of 00
		    td.style.border = '1px solid black';  
		} 
		td.appendChild(document.createTextNode(""));
		td.style.border = '1px solid black';  
	    }
	}
    }

    createCells(daysOfWeek);
    createTimeSlots();
    tbl.className = "table table-striped";
    parent.appendChild(tbl);
}

//////////
// HTTP Requests for searching for courses
//////////
$( document ).ready(function() {
  tableCreate();
  $('#addCourse').click(function(){
    var inputCourse = $('input[name="courseSearch"]').val()
    $.ajax({
      url: '/courses',
      data: {
        course: inputCourse
      },
      error: function(error) {
        console.log(error)
      },
      success: function(data) {
        console.log(data)
        console.log("success")
        $("#courseIdNum").html(data.id)
        $("#courseName").html(data.name)
        $("#startTime").html(data.startTime)
        $("#endTime").html(data.endTime)
        $("#instructor").html(data.instructor)
      },
      type: 'POST'
    });
  });

}); 
