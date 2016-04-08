var selectedCheckBoxes=[]; //keeps track of selected courses to preview

var HTMLModule = (function(){
	return {
		createCalendar: createCalendar,
		createCourseList : createCourseList,
		createSearchList: createSearchList
	};

	function createCalendar(listOfClasses){
		let tbl  = document.createElement('table');
		tbl.className="courseCalendar"
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
	    for (var i = 0; i < 61; i++){ // rows
	    	row = document.createElement('tr');
			for (var j = 0; j < daysOfWeek.length + 1; j++){ // column
				td = document.createElement('td');
			    if(j==0){ // hours and min
			    	hour = 8+Math.floor(i/4);
			    	min = (i%4)*15;
			    	if(min!=0)
			    		td.innerHTML = hour+":"+min;
			    	else 
			    		td.innerHTML = hour+":00";

			    	td.className = 'time';

			    	row.appendChild(td);
			    }		    
			    else{ 
			    	td.innerHTML = "";	
			    } 
			    row.appendChild(td); 
			}
			tbody.appendChild(row);
		}
	}

	var getTableBoundsForEachCourse = function(){
		var day1, day2, starthour,endhour;
		$.each(listOfClasses.lectures, function(index, lecture) {
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
			var minutesRows;
			if(time1[1]<15)
				minutesRows=4
			else if(time1[1]<30)
				minutesRows=3
			else if(time1[1]<45)
				minutesRows=2
			else if(time1[1]>=45)
				minutesRows=1
			starthour = 4*(parseInt(time1[0])-7)-minutesRows;
			var time2 = lecture.end_time.split(":");
			if(time2[1]<15)
				minutesRows=4
			else if(time2[1]<30)
				minutesRows=3
			else if(time2[1]<45)
				minutesRows=2
			else if(time2[1]>=45)
				minutesRows=1
			endhour = 4*(parseInt(time2[0])-7)-minutesRows;
			if(day1!="")
				printCourse(lecture,day1,time1,time2,starthour,endhour);
			if(day2!="")
				printCourse(lecture,day2,time1,time2,starthour,endhour);

		});
}

function printCourse(lecture,day,startTime,endTime,startRow,endRow){
	var classDuration = endRow - startRow +1;
	var startingTime = startTime[0] + ":" + startTime[1];

	tbody.rows[startRow].cells[day].className="timeSlot";
	tbody.rows[startRow].cells[day].rowSpan=classDuration;
	tbody.rows[startRow].cells[day].innerHTML=lecture.program +" "+ lecture.number;
}


createCells(daysOfWeek);
createTimeSlots();
getTableBoundsForEachCourse();
tbl.appendChild(head);
tbl.appendChild(tbody);
return tbl;
}

function createCourseList(d){
	var list = document.createElement('ul');
	list.className="courses"

	$.each(d.lectures, function(idx, lecture) {
		console.log(lecture);

		var courseSlot = document.createElement('li');
		var courseType = document.createElement('div');

		courseType.id = 'type';
		var course = document.createElement('span');
		course.className += 'course';
		course.innerHTML = lecture.program;
		var info = document.createElement('div');
		info.className = 'info';
		var title = document.createElement('h2');
		title.className += 'title';
		title.innerHTML = lecture.number;
		var name = document.createElement('p');
		name.className += 'desc';
		name.innerHTML = lecture.name;
		var section = document.createElement('div');
		section.className = lecture.section;
		var checkbox = document.createElement('input');
		checkbox.setAttribute('type', "checkbox");
		checkbox.setAttribute('id', lecture.full_name + '/' + lecture.section);
		section.appendChild(checkbox);

		info.appendChild(title);
		info.appendChild(name);
		info.appendChild(section);
		courseType.appendChild(course);
		courseSlot.appendChild(courseType);
		courseSlot.appendChild(info);
		list.appendChild(courseSlot);
	});

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
	input.setAttribute('class',"selectClass");
	var selectionId = d.full_name + '/' +  d.section;
	input.setAttribute('id', selectionId);
	input.onclick = function()
	{
		if(this.checked)
		{
			var checkboxes = document.getElementsByClassName("selectClass");
			for (var i = 0; i < checkboxes.length; i++) {
				if(checkboxes[i].id!=this.id)
					checkboxes[i].disabled = true;
			}
			addPrerequisites($(this).closest('tr').index(), this.id);
			checkTimeConflicts($(this).closest('tr').index(), this.id);
		}
		else
		{
			removePrerequisites($(this).closest('tr').index());
			uncheckTimeConflicts();
			var checkboxes = document.getElementsByClassName("selectClass");
			for (var i = 0; i < checkboxes.length; i++) {
				checkboxes[i].disabled = false;
			}
		}
	};
	td.appendChild(input);
	row.appendChild(td);
	return row;	
}

function addPrerequisites(index, id)
{
	$.ajax({
		url: '/get_prerequisites',
		type: 'POST',
		cache: false,
		data: {
			lecture_id: id
		},
		dataType: "json",
		error: function(error) {
			console.log(error);
		},
		success: function(data) {
			prerequisites = "";
			$.each(data.courses, function(index, course)
			{
				if(course.completed)
				{
					prerequisites += '<td bgcolor="#66FF66">' + course.program + course.number + '</td>';
				}
				else
				{
					prerequisites += '<td bgcolor="#FF6666">' + course.program + course.number + '</td>';
				}
			});	
			$('#courseList > tr').eq(index).after('<tr id="prerequisites"><td bgcolor="#6699FF"></td><td>Prereqs:</td><td></td>' + prerequisites + '</tr>');
		}
	});
}


function removePrerequisites()
{
	$('#prerequisites').remove();
}

function checkTimeConflicts(index, id)
{
	var url = window.location.pathname;
	if(url == '/change_fall/')
	{
		console.log('time conflicts ' + id);
		$.ajax({
			url: '/student_fall_lectures',
			type: 'GET',
			cache: false,
			dataType: "json",
			error: function(error) {
				console.log(error);
			},
			success: function(data) {
				data.lectures.forEach((d)=>{
					$.ajax({
						url: '/time_conflicts',
						type: 'POST',
						cache: false,
						data: {
							lecture_id1: id,
							lecture_id2: d.full_name + '/' + d.section
						},
						dataType: "json",
						error: function(error) {
							console.log(error);
						},
						success: function(data1) {
							if(data1 == true)
							{
								$('#courseList > tr').eq(index).after('<tr id="conflict"><td bgcolor="#FF6666"></td><td>Time conflict:</td>' +
									'<td></td><td>' + d.start_time + '</td><td> ' + d.end_time + '</td></tr>');
								$('#add').prop('disabled', true);
							}						       	
						}
					});
				});
			}
		});
	}
	else if(url == '/change_winter/')
	{
		$.ajax({
			url: '/student_winter_lectures',
			type: 'GET',
			cache: false,
			dataType: "json",
			error: function(error) {
				console.log(error);
			},
			success: function(data) {
				data.lectures.forEach((d)=>{
					data.lectures.forEach((d)=>{
						$.ajax({
							url: '/time_conflicts',
							type: 'POST',
							cache: false,
							data: {
								lecture_id1: id,
								lecture_id2: d.full_name + '/' + d.section
							},
							dataType: "json",
							error: function(error) {
								console.log(error);
							},
							success: function(data1) {
								if(data1 == true)
								{
									$('#courseList > tr').eq(index).after('<tr id="conflict"><td bgcolor="#FF6666"></td><td>Time conflict:</td>' +
										'<td></td><td>' + d.start_time + '</td><td> ' + d.end_time + '</td></tr>');
									$('#add').prop('disabled', true);
								}						       	
							}
						});
					});
				});
			}
		});
	}
	else if(url == '/change_summer/')
	{
		$.ajax({
			url: '/student_summer_lectures',
			type: 'GET',
			cache: false,
			dataType: "json",
			error: function(error) {
				console.log(error);
			},
			success: function(data) {
				data.lectures.forEach((d)=>{
					data.lectures.forEach((d)=>{
						$.ajax({
							url: '/time_conflicts',
							type: 'POST',
							cache: false,
							data: {
								lecture_id1: id,
								lecture_id2: d.full_name + '/' + d.section
							},
							dataType: "json",
							error: function(error) {
								console.log(error);
							},
							success: function(data1) {
								if(data1 == true)
								{
									$('#courseList > tr').eq(index).after('<tr id="conflict"><td bgcolor="#FF6666"></td><td>Time conflict:</td>' +
										'<td></td><td>' + d.start_time + '</td><td> ' + d.end_time + '</td></tr>');
									$('#add').prop('disabled', true);
								}						       	
							}
						});
					});
				});
			}
		});
	}
}

function uncheckTimeConflicts()
{
	$('#conflict').remove();
	$('#add').prop('disabled', false);
}
}());
