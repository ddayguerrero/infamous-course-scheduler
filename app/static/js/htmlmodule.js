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
	var list = document.createElement('ul');
	list.className="courses"
	var courseSlot = document.createElement('li');
	var courseType = document.createElement('div');
	courseType.id = 'type';
	var course = document.createElement('span');
	course.className += 'course';
	course.innerHTML = "COMP";
	var info = document.createElement('div');
	info.className = 'info';
	var title = document.createElement('h2');
	title.className += 'title';
	title.innerHTML = "232";
	var name = document.createElement('p');
	name.className += 'desc';
	name.innerHTML = "Logic of Programming";
	var section = document.createElement('div');
	section.className = "section";
	var start = document.createElement('input');
	start.setAttribute('type', "checkbox");
	start.setAttribute('value', "class1");
	var end = document.createElement('input');
	end.setAttribute('type', "checkbox");
	end.setAttribute('value', "class1");
	section.appendChild(start);
	section.appendChild(end);

	
	info.appendChild(title);
	info.appendChild(name);
	info.appendChild(section);
	courseType.appendChild(course);
	courseSlot.appendChild(courseType);
	courseSlot.appendChild(info);
	list.appendChild(courseSlot);
	return list;
    }
}());
