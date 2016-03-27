var HTMLModule = (function(){
    return {
	createCalendar: createCalendar,
	createCourseList : createCourseList
    };
    
    function createCalendar(){
	var tbl  = document.createElement('table');
	var head = document.createElement('thead');
	var headRow = document.createElement('tr');
	var tbody = document.createElement('tbody');
	let daysOfWeek = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
	var row, dayHeader;

	var createCells = function(days){
	    for (var i = 0; i < days.length + 1 ; i++){
		dayHeader = document.createElement('th');
		if(i==0) {
		    dayHeader.innerHTML = " ";
		} else {
		    dayHeader.innerHTML = days[i-1];
		}
		headRow.appendChild(dayHeader);
	    }
	    head.appendChild(headRow);
	}

	var createTimeSlots = function(){
	    var tr, td, min, hour;
	    for (var i = 0; i < 52; i++){
		row = document.createElement('tr');
		for (var j = 0; j < daysOfWeek.length + 1; j++){
		    td = document.createElement('td');
		    if(j==0){
			hour = 8+Math.floor(i/4);
			min = (i%4)*15;
			if(min!=0) td.innerHTML = hour+":"+min;
			else td.innerHTML = hour+":00";
			td.style.border = '1px solid black';
			row.appendChild(td);
		    }
		    else td.innerHTML = " ";
		    td.style.border = '1px solid black';
		    row.appendChild(td); 
		}
		tbody.appendChild(row);
	    }
	}

	createCells(daysOfWeek);
	createTimeSlots();
	tbl.className = "table table-striped";
	tbl.appendChild(head);
	tbl.appendChild(tbody);
	return tbl;
    }

    function createCourseList(){

    }
}());
