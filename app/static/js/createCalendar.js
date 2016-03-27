function tableCreate(){
 var parent = document.getElementById("calendar-location"); 
 tbl  = document.createElement('table');
 tbl.className = "table table-striped";

 var header = tbl.createTHead();
 var row = header.insertRow(0);
 var cell = row.insertCell(0);
 var cell = row.insertCell(1);
 cell.innerHTML = "Monday";
 var cell = row.insertCell(2);
 cell.innerHTML = "Tuesday";
 var cell = row.insertCell(3);
 cell.innerHTML = "Wednesday";
 var cell = row.insertCell(4);
 cell.innerHTML = "Thursday";
 var cell = row.insertCell(5);
 cell.innerHTML = "Friday";
 var cell = row.insertCell(6);
 cell.innerHTML = "Saturday";
 var cell = row.insertCell(7);
 cell.innerHTML = "Sunday";
 

 for(var i = 0; i < 52; i++){
  var tr = tbl.insertRow();
  for(var j = 0; j < 8; j++){
    var td = tr.insertCell();
    if(j==0){
      var hour = 8+Math.floor(i/4);
      var min = (i%4)*15;
      if(min!=0)
        td.appendChild(document.createTextNode(hour+":"+min));
      else
        td.appendChild(document.createTextNode(hour+":00")); //min would only be 0 instead of 00
      td.style.border = '1px solid black';  
    } 
    td.appendChild(document.createTextNode(""));
    td.style.border = '1px solid black';  

  }
}
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