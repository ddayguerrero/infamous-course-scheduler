drop table if exists courses;
create table courses(
Semester integer primary key,
CourseName text not null secondary key,
days text not null,
time integer not null);


