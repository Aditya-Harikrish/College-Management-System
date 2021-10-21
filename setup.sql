DROP DATABASE IF EXISTS COLLEGE_MANAGEMENT_SYSTEM;
CREATE DATABASE COLLEGE_MANAGEMENT_SYSTEM;

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Guardian 
(
    FirstName varchar(50),
    LastName varchar(50),
    StudentID int ,
    Address varchar(500),
    CountryCode int,
    PhoneNumber int,
    EmailID varchar(255),
    PRIMARY KEY(FirstName,LastName,StudentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Student 
(
    StudentID int NOT NULL UNIQUE,
    FirstName varchar(50),
    LastName varchar(50),
    Year int,
    StreamName varchar(3),
    Address varchar(500),
    Aadhaar int,
    NumberOfCourses int,
    DOB date,
    EnrollmentDate date,
    House varchar(6),
    PRIMARY KEY(StudentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StudentAge
(
    DOB date,
    Age int,
    PRIMARY KEY(DOB)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StudentContactNumber
(
    StudentID int,
    CountryCode int,
    PhoneNumber int,
    PRIMARY KEY(StudentID,CountryCode,PhoneNumber)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StudentEmailID
(
    StudentID int,
    EmailID varchar(255),
    PRIMARY KEY(StudentID,EmailID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Student_MedicalConditions
(
    StudentID int,
    MedicalConditions varchar(500),
    PRIMARY KEY(StudentID,MedicalConditions)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Student_Emergency
(
    StudentID int,
    Name varchar(100),
    CountryCode int,
    PhoneNumber int,
    PRIMARY KEY(StudentID,Name)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Student_Courses
(
    StudentID int,
    CoursesStudyingID varchar(6),
    PRIMARY KEY(StudentID,CoursesStudyingID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Staff 
(
    StaffID int NOT NULL UNIQUE,
    FirstName varchar(50),
    LastName varchar(50),
    Salary real,
    BankAccountNumber int,    
    Aadhaar int,
    Address varchar(500),
    DOB date,
    JoiningDate date,
    PermanencyStatus varchar(15),
    PRIMARY KEY(StaffID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StaffAge 
(
    DOB date,
    Age int,
    PRIMARY KEY(DOB)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StaffContactNumber
(
    StaffID int,
    CountryCode int,
    PhoneNumber int,
    PRIMARY KEY(StaffID,CountryCode,PhoneNumber)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StaffEmailID
(
    StaffID int,
    EmailID varchar(255),
    PRIMARY KEY(StaffID,EmailID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StaffDesignation
(
    StaffID int,
    Designation varchar(20),
    PRIMARY KEY(StaffID,Designation)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StaffMedicalConditions
(
    StaffID int,
    MedicalConditions varchar(500),
    PRIMARY KEY(StaffID,MedicalConditions)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Staff_Qualifications
(
    StaffID int,
    Qualifications varchar(500),
    PRIMARY KEY(StaffID,Qualifications)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Teacher
(
    StaffID int,
    CoursesTeachingID int,
    PRIMARY KEY(StaffID,CoursesTeachingID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.TeachingAssistant
(
    StaffID int,
    StudentID int,
    CourseID varchar(6),
    PRIMARY KEY(StaffID,StudentID,CourseID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Classroom
(
    ClassroomID int,
    BuildingName varchar(50),
    PRIMARY KEY(ClassroomID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.CoursesInClassroom
(
    ClassroomID int,
    CourseID varchar(6),
    PRIMARY KEY(ClassroomID,CourseID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Department
(
    DepartmentID int,
    Name varchar(100),
    HOD_ID int,
    PRIMARY KEY(DepartmentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.WorksForDepartment
(
    DepartmentID int,
    StaffID int,
    PRIMARY KEY(DepartmentID,StaffID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.StudiesInDepartment
(
    DepartmentID int,
    StudentID int,
    PRIMARY KEY(DepartmentID,StudentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Course
(
    CourseID varchar(6),
    Credits int,
    PRIMARY KEY(CourseID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.CoursePrerequisites
(
    CourseID varchar(6),
    Prerequisites varchar(6),
    PRIMARY KEY(CourseID,Prerequisites)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Dependent
(
    StaffID int,
    FirstName varchar(50),
    LastName varchar(50),
    CountryCode int,
    PhoneNumber int,
    EmailID varchar(255),
    Address varchar(500),
    PRIMARY KEY(StaffID,FirstName,LastName)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Grade
(
    Grade real,
    CourseID varchar(6),
    StudentID int,
    PRIMARY KEY(CourseID,StudentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Teaches
(
    StudentID int,
    StaffID int,
    PRIMARY KEY(StudentID,StaffID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Enrolled
(
    StudentID int,
    CourseID varchar(6),
    PRIMARY KEY(StudentID,CourseID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Partof
(
    TeacherHOD_ID int,
    TeacherMember_ID int,
    DepartmentID int,
    PRIMARY KEY(TeacherHOD_ID,TeacherMember_ID,DepartmentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.MentorAStudent
(
    StudentID int,
    TeacherID int,
    DepartmentID int,
    PRIMARY KEY(StudentID,TeacherID, DepartmentID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.Lecture
(
    StudentID int,
    TeacherID int,
    CourseID varchar(6),
    ClassroomID int,
    PRIMARY KEY(StudentID,TeacherID,CourseID,ClassroomID)
);

CREATE TABLE COLLEGE_MANAGEMENT_SYSTEM.InvolvedInACourse
(
    StudentID int,
    TeacherID int,
    CourseID varchar(6),
    TeachingAssistantStaffID int,
    PRIMARY KEY(StudentID,TeacherID,CourseID,TeachingAssistantStaffID)
);