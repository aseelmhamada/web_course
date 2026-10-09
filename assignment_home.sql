use web_course2;
CREATE TABLE students (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(25) NOT NULL,
    age INT,
    major VARCHAR(30),
    city VARCHAR(25),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    
    

);
INSERT INTO students(student_name,age,major,city) 
VALUES
 ('Aseel','22','Computer Science','Gaza'),
 ('Yousef','29','Management','Cairo'),
 ('Sarah','23','IT','Jorden');

SELECT*FROM students;
SELECT*FROM students WHERE age >20;
UPDATE students 
SET age ='25',student_name ='mona'
 WHERE id =1;
DELETE FROM students
WHERE id=2;