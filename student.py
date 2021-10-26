def student(con, cursor):
    while True:
        print("\nStudent")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student Information")
        print("4. Search Student")
        print("5. View Student")
        print("6. Retrieve the complete data tuples of all students belonging to a particular House.")
        print("7. Retrieve the Names of Students with more than 4 courses")
        print("8. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter the Student's First Name: ")
                second_name = input("Enter the Student's Second Name: ")
                year = int(input("Enter the Student's Year: "))
                stream = input("Enter the Student's Stream: ")
                address = input("Enter the Student's Address: ")
                aadhaar = int(input("Enter the Student's Aadhaar Number: "))
                number_of_courses = int(input("Enter the number of courses the student is enrolled in: "))
                dob = input("Enter the Student's Date of Birth (yyyy-mm-dd): ")
                enrollment_date = input("Enter the Student's Enrollment Date (yyyy-mm-dd): ")
                house = input("Enter the Student's House: ")
                cursor.execute(query, (student_id, first_name, second_name, year, stream, address, aadhaar, number_of_courses, dob, enrollment_date, house))
                number = input("Enter the Student's number (code number): ")
                num_list = number.split(' ')
                if(len(num_list) == 1):
                    code = 91
                    num = int(num_list[0])
                else:
                    code = int(num_list[0])
                    num = int(num_list[1])
                query = "INSERT INTO StudentContactNumber VALUES (%s, %s, %s)"
                cursor.execute(query, (student_id, code, num))
                email_id = input("Enter the Student's EmailID: ")
                query = "INSERT INTO StudentEmailID VALUES (%s, %s)"
                cursor.execute(query, (student_id, email_id))
                while True:
                    print("\nStudent Medical Conditions: ")
                    print("1. Add Medical Condition")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Student_MedicalConditions VALUES (%s, %s)"
                        condition = input("Enter the Medical Condition: ")
                        cursor.execute(query, (student_id, condition))
                    elif ch == 2:
                        break
                while True:
                    print("\nStudent Emergency Contacts: ")
                    print("1. Add Emergency Contact")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Student_Emergency VALUES (%s, %s, %s)"
                        name = input("Enter the Emergency Contact's Name: ")
                        code = int(input("Enter the Emergency Contact's Telephone Code: "))
                        number = int(input("Enter the Emergency Contact's Telephone Number: "))
                        cursor.execute(query, (student_id, name, code, number))
                        con.commit()
                    elif ch == 2:
                        break
                while True:
                    print("\nStudent Courses: ")
                    print("1. Add Course")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Student_Courses VALUES (%s, %s)"
                        course_id = int(input("Enter the Course ID: "))
                        query1 = "SELECT * FROM Courses WHERE CourseID = %s"
                        cursor.execute(query1, (course_id))
                        result = cursor.fetchone()
                        if result is None:
                            print("Course does not exist")
                            continue
                        cursor.execute(query, (student_id, course_id))
                    elif ch == 2:
                        break
                while True:
                    print("\nStudent Guardians: ")
                    print("1. Add Guardian")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Guardian VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        first_name = input("Enter the Guardian's First Name: ")
                        second_name = input("Enter the Guardian's Second Name: ")
                        address = input("Enter the Guardian's Address: ")
                        code = int(input("Enter the Guardian's Telephone Code: "))
                        number = int(input("Enter the Guardian's Telephone Number: "))
                        email_id = input("Enter the Guardian's EmailID: ")
                        cursor.execute(query, (first_name, second_name, student_id, address, code, number, email_id))
                    elif ch == 2:
                        break
                con.commit()
                print("Student added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:    
                student_id = int(input("Enter Student ID: "))
                query = "DELETE FROM Student WHERE StudentID = %s"
                cursor.execute(query, (student_id))
                query = "DELETE FROM Guardian WHERE StudentID = %s"
                cursor.execute(query, (student_id))
                query = "DELETE FROM StudentContactNumber WHERE StudentID = %s"
                cursor.execute(query, (student_id))
                query = "DELETE FROM Student_MedicalConditions WHERE StudentID = %s"
                cursor.execute(query, (student_id))
                query = "DELETE FROM Student_Emergency WHERE StudentID = %s"
                cursor.execute(query, (student_id))
                query = "DELETE FROM Student_Courses WHERE StudentID = %s"
                cursor.execute(query, (student_id))
                con.commit()
                print("Student deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                query = "SELECT * FROM Student WHERE StudentID = %s"
                upd_row = dict() 
                cursor.execute(query, (student_id))
                result = cursor.fetchone()
                if result is None:
                    print("Student does not exist")
                    continue
                print("\nUpdate Student Information")
                print("Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['FirstName'] = input("1. First Name: ")
                if upd_row['FirstName'] == '':
                    upd_row['FirstName'] = result['FirstName']
                upd_row['LastName'] = input("2. Last Name: ")
                if upd_row['LastName'] == '':
                    upd_row['LastName'] = result['LastName']
                upd_row['Year'] = input("3. Year: ")
                if upd_row['Year'] == '':
                    upd_row['Year'] = result['Year']
                else:
                    upd_row['Year'] = upd_row['Year']
                upd_row['StreamName'] = input("4. Stream: ")
                if upd_row['StreamName'] == '':
                    upd_row['StreamName'] = result['StreamName']
                upd_row['Address'] = input("5. Address: ")
                if upd_row['Address'] == '':
                    upd_row['Address'] = result['Address']
                upd_row['Aadhaar'] = input("6. Aadhaar Number: ")
                if upd_row['Aadhaar'] == '':
                    upd_row['Aadhaar'] = result['Aadhaar']
                else:
                    upd_row['Aadhaar'] = int(upd_row['Aadhaar'])
                upd_row['NumberOfCourses'] = input("7. Number of Courses: ")
                if upd_row['NumberOfCourses'] == '':
                    upd_row['NumberOfCourses'] = result['NumberOfCourses']
                else:
                    upd_row['NumberOfCourses'] = int(upd_row['NumberOfCourses'])
                upd_row['DOB'] = input("8. Date of Birth: ")
                if upd_row['DOB'] == '':
                    upd_row['DOB'] = result['DOB']
                upd_row['EnrollmentDate'] = input("9. Enrollment Date: ")
                if upd_row['EnrollmentDate'] == '':
                    upd_row['EnrollmentDate'] = result['EnrollmentDate']
                upd_row['House'] = input("10. House: ")
                if upd_row['House'] == '':
                    upd_row['House'] = result['House']
                query = "UPDATE Student SET StudentID = %s, FirstName = %s, LastName = %s, Year = %s, StreamName = %s, Address = %s, Aadhaar = %s, NumberOfCourses = %s, DOB = %s, EnrollmentDate = %s, House = %s"
                cursor.execute(query, (student_id, upd_row['FirstName'], upd_row['LastName'], upd_row['Year'], upd_row['StreamName'], upd_row['Address'], upd_row['Aadhaar'], upd_row['NumberOfCourses'], upd_row['DOB'], upd_row['EnrollmentDate'], upd_row['House']))
                con.commit()
                print("Student updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Student WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchone()
            if result is None:
                print("Student does not exist")
                continue
            print("Student Information: ")
            print("Student ID: ", result['StudentID'])
            print("First Name: ", result['FirstName'])
            print("Last Name: ", result['LastName'])
            print("Year: ", result['Year'])
            print("Stream: ", result['StreamName'])
            print("Address: ", result['Address'])
            print("Aadhaar Number: ", result['Aadhaar'])
            print("Number of Courses: ", result['NumberOfCourses'])
            print("Date of Birth: ", result['DOB'])
            print("Enrollment Date: ", result['EnrollmentDate'])
            print("House: ", result['House'])
        elif choice == 5:
            try:
                query = "SELECT * FROM Student"
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
            except Exception as e:
                print(e)
        elif choice == 6:
            query = "SELECT * FROM Student WHERE HOUSE = %s"
            house = input("Enter the House whose Students data you wish to view: ")
            cursor.execute(query, (house))
            result = cursor.fetchall()
            if result is None:
                print("No Students in this House")
                continue
            for row in result:
                print(row)
        elif choice == 7:
            query = "SELECT FirstName, LastName FROM Student WHERE NumberOfCourses > 4"
            cursor.execute(query)
            result = cursor.fetchall()
            if result is None:
                print("No Students with more than 4 courses")
                continue
            for row in result:
                print(row[0], row[1])
        elif choice == 8:
            return
        else:
            print("Invalid choice")

def guardian(con, cursor):
    while True:
        print("1. Add Guardian")
        print("2. Delete Guardian")
        print("3. Update Guardian")
        print("4. View Guardians of a Student")
        print("5. View Guardian Information")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            query = "INSERT INTO Guardian VALUES (%s, %s, %s, %s, %s, %s, %s)"
            student_id = int(input("Enter Student ID: "))
            first_name = input("Enter the Guardian's First Name: ")
            second_name = input("Enter the Guardian's Second Name: ")
            address = input("Enter the Guardian's Address: ")
            code = int(input("Enter the Guardian's Telephone Code: "))
            number = int(input("Enter the Guardian's Telephone Number: "))
            email_id = input("Enter the Guardian's EmailID: ")
            cursor.execute(query, (first_name, second_name, student_id, address, code, number, email_id))
            con.commit()
            print("Guardian added successfully")
        elif choice == 2:
            student_id = int(input("Enter Student ID: "))
            first_name = input("Enter the Guardian's First Name: ")
            last_name = input("Enter the Guardian's Last Name: ")
            query = "DELETE FROM Guardian WHERE FirstName = %s AND LastName = %s AND StudentID = %s"
            cursor.execute(query, (first_name, last_name, student_id))
            con.commit()
            print("Guardian deleted successfully")
        elif choice == 3:
            student_id = int(input("Enter Student ID: "))
            first_name = input("Enter the Guardian's First Name: ")
            last_name = input("Enter the Guardian's Last Name: ")
            upd_row = dict()
            query = "SELECT * FROM Guardian WHERE FirstName = %s AND LastName = %s AND StudentID = %s"
            cursor.execute(query, (first_name, last_name, student_id))
            result = cursor.fetchone()
            if result == None:
                print("Guardian does not exist")
                continue
            print("Guardian Information: ")
            print("Press ENTER if no update is required, otherwise enter the new value: ")
            upd_row['FirstName'] = input("First Name: ")
            if upd_row['FirstName'] == '':
                upd_row['FirstName'] = result[0]
            upd_row['LastName'] = input("Last Name: ")
            if upd_row['LastName'] == '':
                upd_row['LastName'] = result[1]
            upd_row['Address'] = input("Address: ")
            if upd_row['Address'] == '':
                upd_row['Address'] = result[3]
            upd_row['CountryCode'] = input("Country Code")
            if upd_row['CountryCode'] == '':
                upd_row['CountryCode'] = result[4]
            else:
                upd_row['CountryCode'] = int(upd_row['CountryCode'])
            upd_row['PhoneNumber'] = input("Phone Number: ")
            if upd_row['PhoneNumber'] == '':
                upd_row['PhoneNumber'] = result[5]
            else:
                upd_row['PhoneNumber'] = int(upd_row['PhoneNumber'])
            upd_row['EmailID'] = input("Email ID: ")
            if upd_row['EmailID'] == '':
                upd_row['EmailID'] = result[6]
            query = "UPDATE Guardian SET FirstName = %s, LastName = %s, Address = %s, CountryCode = %s, PhoneNumber = %s, EmailID = %s WHERE FirstName = %s AND LastName = %s AND StudentID = %s"
            cursor.execute(query, (upd_row['FirstName'], upd_row['LastName'], upd_row['Address'], upd_row['CountryCode'], upd_row['PhoneNumber'], upd_row['EmailID'], first_name, last_name, student_id))
            con.commit()
            print("Guardian updated successfully")
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Guardian WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchall()
            if result == None:
                print("Guardian does not exist")
                continue
            print("Guardian Information: ")
            for row in result:
                print(row)
        elif choice == 5:
            first_name = input("Enter the Guardian's First Name: ")
            last_name = input("Enter the Guardian's Last Name: ")
            query = "SELECT * FROM Guardian WHERE FirstName = %s AND LastName = %s"
            cursor.execute(query, (first_name, last_name))
            result = cursor.fetchone()
            if result == None:
                print("Guardian does not exist")
                continue
            print("Guardian Information: ")
            print("Student ID: ", result[2])
            print("First Name: ", result[0])
            print("Last Name: ", result[1])
            print("Address: ", result[3])
            print("Country Code: ", result[4])
            print("Phone Number: ", result[5])
            print("Email ID: ", result[6])
        elif choice == 6:
            return
        else:
            print("Invalid choice")

