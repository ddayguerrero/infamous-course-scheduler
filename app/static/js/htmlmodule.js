var HTMLModule = (function(){
    return {
	createCalendar: createCalendar,
	createCourseList : createCourseList,
	createSearchList: createSearchList
    };
    
    function createCalendar(listOfClasses){
	let tbl  = document.createElement('table');
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
	    for (var i = 0; i < 52; i++){ //rows
		row = document.createElement('tr');
		for (var j = 0; j < daysOfWeek.length + 1; j++){ //column
		    td = document.createElement('td');
		    if(j==0){//hours and min
				hour = 8+Math.floor(i/4);
				min = (i%4)*15;
				if(min!=0)
					td.innerHTML = hour+":"+min;
				else td.innerHTML = hour+":00";
				td.style.border = '1px solid black';
				row.appendChild(td);
		    }		    
		    else{ 
		     td.innerHTML = "";	
		    } 
		    td.style.border = '1px solid black';
		    row.appendChild(td); 
		}
		tbody.appendChild(row);
	    }
	}

	var getTableBoundsForEachCourse = function(){
	var day1, day2, starthour,endhour;
	   //$.each(listOfClasses.lectures, function(index, lecture) {
	   	var lecture = listOfClasses.lectures[0];
	   	console.log(lecture.day_one+" "+lecture.day_two+" "+lecture.start_time+" "+lecture.end_time);
		switch (lecture.day_one) {
			case "M":
			day1 = 1;
			break;
			case "T":
			day1 = 2;
			break;
			case "W":
			day1 = 3;
			break;
			case "J":
			day1 = 4;
			break;
			case "F":
			day1 = 5;
			break;
			case "S":
			day1 = 6;
			break;
			case  "D":
			day1 = 7;
			break;
			default: 
			day1= ""
		}
		switch (lecture.day_two) {
			case "M":
			day2 = 1;
			break;
			case "T":
			day2 = 2;
			break;
			case "W":
			day2 = 3;
			break;
			case "J":
			day2 = 4;
			break;
			case "F":
			day2 = 5;
			break;
			case "S":
			day2 = 6;
			break;
			case  "D":
			day2 = 7;
			break;
			default: 
			day2= ""
		}
		var time1 = lecture.start_time.split(":");
		starthour = parseInt(time1[0]) + 4*Math.floor(parseInt(time1[1])/15)-7;
		var time2 = lecture.end_time.split(":");
		endhour = parseInt(time2[0]) + Math.floor(parseInt(time2[1])/15)-7;
		if(day1!="")
			printCourse(lecture,day1,starthour,endhour);
		if(day2!="")
			printCourse(lecture,day2,starthour,endhour);

	//});
}

var printCourse = function(lecture,day,startTime,endTime){
		var classDuration = endTime - startTime;
		for(row=1; row<=classDuration;row++){
			var timeOnTable= tbody.rows[row];
			var timeCell = timeOnTable.cells[day];
			timeCell.innerHTML= lecture.name
			//var timeCell = tbl.rows[row].cells[day];
			timeCell.style.backgroundColor = "yellow";
			if(row!=0 || row!=classDuration){
				timeCell.style.borderTop = "thick solid yellow";
				timeCell.style.borderBottom = "thick solid yellow";
				if(row==Math.floor(classDuration/2)){
					timeCell.innerHTML=lecture.name;
				}
				else if(row==Math.floor(classDuration/2)+1){
					timeCell.innerHTML=lecture.number;
				}
				else if(row==Math.floor(classDuration/2)+2){
					timeCell.innerHTML=lecture.start_time+ "-";
				}
				else if(row==Math.floor(classDuration/2)+3){
					timeCell.innerHTML=lecture.end_time;
				}
			}
			else if(row==1){//first cell needs bottom border removed
				timeCell.style.borderBottom = "thick solid yellow";
			}
			else if(row==classDuration){
				timeCell.style.borderTop = "thick solid yellow";
			} 
		}
	}


	createCells(daysOfWeek);
	createTimeSlots();
	getTableBoundsForEachCourse();
	tbl.className = "table table-striped";
	tbl.appendChild(head);
	tbl.appendChild(tbody);
	return tbl;
    }

    function createCourseList(d){
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

    function createSearchList(d){
	var row = document.createElement('tr');
	var td = document.createElement('td');
	td.className = "section";
	td.innerHTML = d.section;
	row.appendChild(td);
	td = document.createElement('td');
	td.className = "code";
	td.innerHTML = d.full_name;
	row.appendChild(td);
	$('#fallList').add(row);
	td = document.createElement('td');
	td.className = "name";
	td.innerHTML = d.name;
	row.appendChild(td);
	$('#fallList').add(row);
	td = document.createElement('td');
	td.className = "startTime";
	td.innerHTML = d.start_time;
	row.appendChild(td);
	$('#fallList').add(row);
	td = document.createElement('td');
	td.className = "endTime";
	td.innerHTML = d.end_time;
	row.appendChild(td);
	$('#fallList').add(row);
	td = document.createElement('td');
	td.className = "instructor";
	td.innerHTML = d.instructor;
	row.appendChild(td);
	$('#fallList').add(row);
	td = document.createElement('td');
	input = document.createElement('input');
	input.setAttribute('type', 'checkbox');
	input.setAttribute('value', 'class1');
	var selectionId = d.full_name + '/' +  d.section;
	input.setAttribute('id', selectionId);
	td.appendChild(input);
	row.appendChild(td);
	return row;	
    }
}());