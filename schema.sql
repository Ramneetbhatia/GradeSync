CREATE DATABASE IF NOT EXISTS gradesync_db;

USE gradesync_db;


CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE
);


CREATE TABLE IF NOT EXISTS subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    marks DECIMAL(5,2) NOT NULL,

FOREIGN KEY (student_id)
    REFERENCES students(student_id),

FOREIGN KEY (subject_id)
    REFERENCES subjects(subject_id),

CHECK (marks >= 0 AND marks <= 100),

UNIQUE (student_id, subject_id)
);