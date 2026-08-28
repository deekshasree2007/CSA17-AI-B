
% Student - Teacher - Subject Code Database

student(deeksha, ravi, ai101).
student(rahul, ravi, ds102).
student(anjali, priya, db103).
student(rohit, kumar, cn104).

% If Student name is given
details(Name) :-
    student(Name, Teacher, Code),
    write('Teacher: '),
    write(Teacher),
    nl,
    write('Subject Code: '),
    write(Code).

% Student - Teacher - Subject Code Database


% Student - Teacher - Subject Code Database

student(deeksha, ravi, ai101).
student(rahul, ravi, ds102).
student(anjali, priya, db103).
student(rohit, kumar, cn104).

% Give student name -> Teacher and Subject Code
details(Name) :-
    student(Name, Teacher, Code),
    write('Teacher: '),
    write(Teacher),
    nl,
    write('Subject Code: '),
    write(Code).

% Student - Teacher - Subject Code Database

student(deeksha, ravi, ai101).
student(rahul, ravi, ds102).
student(anjali, priya, db103).
student(rohit, kumar, cn104).

% Give student name -> Teacher and Subject Code
details(Name) :-
    student(Name, Teacher, Code),
    write('Teacher: '),
    write(Teacher),
    nl,
    write('Subject Code: '),
    write(Code).

% Give teacher name -> Student and Subject Code
teacher_details(Teacher) :-
    student(Student, Teacher, Code),
    write('Student: '),
    write(Student),
    nl,
    write('Subject Code: '),
    write(Code).

% Give subject code -> Student and Teacher
code_details(Code) :-
    student(Student, Teacher, Code),
    write('Student: '),
    write(Student),
    nl,
    write('Teacher: '),
    write(Teacher).
