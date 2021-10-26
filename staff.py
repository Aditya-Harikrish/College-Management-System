def staff(con, cursor):
    while True:
        print("\Staff")
        print("1. Add Staff Member")
        print("2. Delete Staff Member")
        print("3. Update Staff Information")
        print("4. Search Staff Member")
        print("5. View Staff Members")
        print("6. Go back")
        print("7. Add Dependent")
        print("8. Delete Dependent")
        print("9. Update Dependent")
        print("10. Edit Teacher")
        print("10. Edit Teaching Assistant")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                query = "INSERT INTO Staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                staff_id = int(input("Enter Staff ID: "))
                first_name = input("Enter the Staff Member's First Name: ")
                second_name = input("Enter the Staff Member's Second Name: ")
                salary = float(input("Enter the Staff Member's Salary: "))
                bank_account = int(
                    input("Enter the Staff Member's Bank Account Number: "))
                address = input("Enter the Staff Member's Address: ")
                aadhaar = int(
                    input("Enter the Staff Member's Aadhaar Number: "))
                dob = input("Enter the Student's Date of Birth (yyyy-mm-dd): ")
                Joining_date = input(
                    "Enter the Staff Member's Joining Date (yyyy-mm-dd): ")
                permanency = input(
                    "Enter the Staff Member's Permanency Status: ")
                cursor.execute(query, (staff_id, first_name, second_name, salary,
                               bank_account, aadhaar, address, dob, Joining_date, permanency))

                while True:
                    print("\Staff Contact Number: ")
                    print("1. Add Contact Number")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        country_code = input(
                            "Enter the country code (default = 91): ").strip()
                        if country_code == '':
                            country_code = 91
                        phone_number = input("Enter the phone number: ")
                        query = "INSERT INTO StaffContactNumber VALUES (%s, %s, %s)"
                        cursor.execute(
                            query, (staff_id, country_code, phone_number))

                    elif ch == 2:
                        break

                while True:
                    print("\Staff Email ID: ")
                    print("1. Add Email ID")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        email_id = input("Enter the Email ID: ")
                        query = "INSERT INTO StaffEmailID VALUES (%s, %s)"
                        cursor.execute(query, (staff_id, email_id))

                    elif ch == 2:
                        break

                while True:
                    print("\Staff Designation: ")
                    print("1. Add Designation")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        designation = input("Enter the Staff's Designation: ")
                        query = "INSERT INTO StaffDesignation VALUES (%s, %s)"
                        cursor.execute(query, (staff_id, designation))

                    elif ch == 2:
                        break

                while True:
                    print("\Staff Qualifications: ")
                    print("1. Add Qualification")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Staff_Qualifications VALUES (%s, %s)"
                        qualification = input("Enter the Qualification: ")
                        cursor.execute(query, (staff_id, qualification))
                    elif ch == 2:
                        break

                while True:
                    print("\nStaff Medical Conditions: ")
                    print("1. Add Condition")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Staff_Medical_Conditions VALUES (%s, %s)"
                        condition = input("Enter the Condition: ")
                        cursor.execute(query, (staff_id, condition))
                    elif ch == 2:
                        break

                con.commit()
                print("Staff Member added successfully")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 2:
            try:
                staff_id = int(input("Enter Staff ID: "))
                query = "DELETE FROM Staff WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM StaffContactNumber WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM StaffEmailID WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM StaffDesignation WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM Staff_Qualifications WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM StaffMedicalConditions WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM Teacher WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM TeachingAssistant WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM WorksForDepartment WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM Teaches WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                query = "DELETE FROM Dependent WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                con.commit()
                print("Staff deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 3:
            try:
                staff_id = int(input("Enter Staff ID: "))
                query = "SELECT * FROM Staff WHERE StaffID = %s"
                upd_row = dict()
                cursor.execute(query, (staff_id))
                result = cursor.fetchone()
                if result is None:
                    print("Staff Member doesn't exist")
                    continue
                print("\nUpdate Student Information")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['FirstName'] = input("First Name: ")
                if upd_row['FirstName'] == '':
                    upd_row['FirstName'] = result[1]
                upd_row['LastName'] = input("Last Name: ")
                if upd_row['LastName'] == '':
                    upd_row['LastName'] = result[2]
                upd_row['Salary'] = input("Salary: ")
                if upd_row['Salary'] == '':
                    upd_row['Salary'] = result[3]
                else:
                    upd_row['Salary'] = float(upd_row['Salary'])
                upd_row['BankAccountNumber'] = input("Bank Account Number: ")
                if upd_row['BankAccountNumber'] == '':
                    upd_row['BankAccountNumber'] = result[4]
                else:
                    upd_row['BankAccountNumber'] = int(
                        upd_row['BankAccountNumber'])
                upd_row['Address'] = input("Address: ")
                if upd_row['Address'] == '':
                    upd_row['Address'] = result[5]
                upd_row['AadhaarNumber'] = input("Aadhaar Number: ")
                if upd_row['AadhaarNumber'] == '':
                    upd_row['AadhaarNumber'] = result[6]
                else:
                    upd_row['AadhaarNumber'] = int(upd_row['AadhaarNumber'])
                upd_row['DOB'] = input("Date of Birth: ")
                if upd_row['DOB'] == '':
                    upd_row['DOB'] = result[7]
                upd_row['JoiningDate'] = input("Joining Date: ")
                if upd_row['JoiningDate'] == '':
                    upd_row['JoiningDate'] = result[8]
                upd_row['PermanencyStatus'] = input("Permanency Status: ")
                if upd_row['PermanencyStatus'] == '':
                    upd_row['PermanencyStatus'] = result[9]
                query = "UPDATE Staff SET FirstName = %s, LastName = %s, Salary = %s, BankAccountNumber = %s, Address = %s, Aadhaar = %s, DOB = %s, JoiningDate = %s, PermanencyStatus = %s WHERE StaffID = %s"
                cursor.execute(query, (upd_row['FirstName'], upd_row['LastName'], upd_row['Salary'], upd_row['BankAccountNumber'],
                                       upd_row['AadhaarNumber'], upd_row['Address'], upd_row['DOB'], upd_row['JoiningDate'], upd_row['PermanencyStatus'], staff_id))
                con.commit()
                print("Staff Member updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 4:
            try:
                staff_id = int(input("Enter Staff ID: "))
                query = "SELECT * FROM Staff WHERE StaffID = %s"
                cursor.execute(query, (staff_id))
                result = cursor.fetchone()
                if result is None:
                    print("Staff Member doesn't exist")
                    continue
                print("\nStaff Member Information: ")
                print("Staff ID: ", result[0])
                print("First Name: ", result[1])
                print("Last Name: ", result[2])
                print("Salary: ", result[3])
                print("Bank Account Number: ", result[4])
                print("Address: ", result[6])
                print("Aadhaar Number: ", result[5])
                print("Date of Birth: ", result[7])
                print("Joining Date: ", result[8])
                print("Permanency Status: ", result[9])
            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 5:
            try:
                query = "SELECT * FROM Staff"
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 6:
            return

        elif choice == 7:
            try:
                query = "INSERT INTO Dependent VALUES (%s %s %s %s %s %s %s)"
                staff_id = input("Enter Staff ID: ").strip()
                if len(staff_id) == 0:
                    staff_id = "NULL"
                first_name = input("Enter the Dependent's First Name: ")
                last_name = input("Enter the Dependent's Last Name: ")
                country_code = input(
                    "Enter the country code for the phone number (default = 91): ")
                if len(country_code) == 0:
                    country_code = 91

                phone_number = input("Enter the phone number: ")
                email_id = input("Enter the email ID: ")
                address = input("Enter the address: ")

                cursor.execute(query, (staff_id, first_name, last_name,
                                       country_code, phone_number, email_id, address))
                con.commit()
                print("Dependent inserted successfully")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 8:
            try:
                query = "DELETE FROM Dependent WHERE (StaffID = %s AND FirstName = %s AND LastName = %s)"
                staff_id = input("Enter Staff ID: ").strip()
                first_name = input("Enter the Dependent's First Name: ")
                last_name = input("Enter the Dependent's Last Name: ")

                if len(staff_id) == 0 or len(first_name) == 0 or len(second_name) == 0:
                    print("Erro: input missing!")
                    continue

                cursor.execute(query, (staff_id, first_name, last_name))
                con.commit()
                print("Dependent deleted successfully")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 9:
            try:
                staff_id = input("Enter Staff ID: ").strip()
                first_name = input("Enter Dependent's First Name: ")
                last_name = input("Enter Dependent's Last Name: ")

                if len(staff_id) == 0 or len(first_name) == 0 or len(last_name) == 0:
                    print("Error: invalid input!")
                    continue

                query = "SELECT * FROM Dependent WHERE StaffID = %s, FirstName = %s, LastName = %s"
                cursor.execute(query, (staff_id, first_name, last_name))
                if cursor.fetchone() is None:
                    print("Dependent doesn't exist")
                    continue

                new_row = {}
                print("\nUpdate Dependent Information")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value.\n")

                attribute = 'StaffID'
                new_row[attribute] = input("Enter Staff ID: ").strip()
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                attribute = 'FirstName'
                new_row[attribute] = input("Enter First Name: ")
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                attribute = 'LastName'
                new_row[attribute] = input("Enter Last Name: ")
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                attribute = 'Country Code'
                new_row[attribute] = input("Enter Country Code: ")
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                attribute = 'Phone Number'
                new_row[attribute] = input("Enter Phone Number: ")
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                attribute = 'Email ID'
                new_row[attribute] = input("Enter Email ID: ")
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                attribute = 'Address'
                new_row[attribute] = input("Enter Address: ")
                if len(new_row[attribute]) == 0:
                    new_row[attribute] = result[attribute]

                query = "UPDATE Dependent SET StaffID = %s, FirstName = %s, LastName = %s, CountryCode = %s, PhoneNumber = %s, EmailID = %s, Address = %s WHERE (StaffID = %s, FirstName = %s, LastName = %s)"
                cursor.execute(query, (new_row['StaffID'], new_row['FirstName'], new_row['LastName'],
                               new_row['CountryCode'], new_row['PhoneNumber'], new_row['EmailID'], new_row['Address'], staff_id, first_name, last_name))

                con.commit()
                print("Dependent updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 10:
            while True:
                try:
                    print("\n1. Add a teacher")
                    print("2. Delete a teacher")
                    print("3. Go back")
                    ch = input("Enter your choice: ")

                    if ch == "1":
                        staff_id = input("Enter StaffID")
                        course_id = input(
                            "Enter CourseID of the course that the teacher is teaching: ")
                        query = "INSERT INTO Teacher VALUES (%s, %s)"

                        cursor.execute(query, (staff_id, course_id))

                    elif ch == "2":
                        staff_id = input("Enter StaffID")
                        course_id = input(
                            "Enter CourseID of the course that the teacher is teaching: ")
                        query = "DELETE FROM Teacher WHERE (StaffID = %s, CourseTeachingID = %s)"

                        cursor.execute(query, (staff_id, course_id))

                    elif ch == "3":
                        break

                except Exception as e:
                    con.rollback()
                    print(e)
                    continue

            con.commit()

        elif choice == 11:
            while True:
                try:
                    print("\n1. Add a teaching assistant")
                    print("2. Delete a teaching assistant")
                    print("3. Go back")
                    ch = input("Enter your choice: ")

                    if ch == "1":
                        staff_id = input("Enter the Staff ID")
                        student_id = input("Enter the Student ID: ")
                        course_id = input(
                            "Enter the Course ID: ")

                        query = "INSERT INTO TeachingAssistant VALUES (%s, %s, %s, %s)"

                        cursor.execute(
                            query, (staff_id, student_id, course_id))

                    elif ch == "2":
                        staff_id = input("Enter the Staff ID")
                        student_id = input("Enter the Student ID: ")
                        course_id = input(
                            "Enter the Course ID: ")
                        query = "DELETE FROM TeachingAssistant WHERE (StaffID = %s, StudentID = %s, CourseTeachingID = %s)"

                        cursor.execute(
                            query, (staff_id, student_id, course_id))

                    elif ch == "3":
                        break

                except Exception as e:
                    con.rollback()
                    print(e)
                    continue

            con.commit()

        else:
            print("Invalid choice")
