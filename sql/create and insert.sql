create table student(
    id char(2),
    name varchar(20),
    marks number(2)
);
insert into student (id,name,marks)
values('01','aditya',79),
('02','tomar',97);
rename student to student2;
 truncate table student2;
 drop table student2;