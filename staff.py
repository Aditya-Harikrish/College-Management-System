def staff(con, cursor):
    while True:
        print("\Staff")
        print("1. Add Staff Member")
        print("2. Delete Staff Member")
        print("3. Update Staff Information")
        print("4. Search Staff Member")
        print("5. View Staff Members")
        print("6. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            query = "INSERT INTO Staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            staff_id = int(input("Enter Staff ID: "))
            first_name = input("Enter the Staff Member's First Name: ")
            second_name = input("Enter the Staff Member's Second Name: ")
            salary = float(input("Enter the Staff Member's Salary: "))
            bank_account = int(input("Enter the Staff Member's Bank Account Number: "))
            address = input("Enter the Staff Member's Address: ")
            aadhaar = int(input("Enter the Staff Member's Aadhaar Number: "))
            dob = input("Enter the Student's Date of Birth (yyyy-mm-dd): ")
            Joining_date = input("Enter the Staff Member's Joining Date (yyyy-mm-dd): ")
            permanency = input("Enter the Staff Member's Permanency Status: ")
            cursor.execute(query, (staff_id, first_name, second_name, salary, bank_account, aadhaar, address, dob, Joining_date, permanency))
            con.commit()
            number = input("Enter the Staff Member's number (code number): ")
            num_list = number.split(' ')
            if(len(num_list) == 1):
                code = 91
                num = int(num_list[0])
            else:
                code = int(num_list[0])
                num = int(num_list[1])
            query = "INSERT INTO StaffContactNumber VALUES (%s, %s, %s)"
            cursor.execute(query, (staff_id, code, num))
            con.commit()
            email_id = input("Enter the Staff Member's EmailID: ")
            query = "INSERT INTO StaffEmailID VALUES (%s, %s)"
            cursor.execute(query, (staff_id, email_id))
            con.commit()
            designation = input("Enter the Staff's Designation: ")
            query = "INSERT INTO StaffDesignation VALUES (%s, %s)"
            cursor.execute(query, (staff_id, designation))
            con.commit()
            while True:
                print("\Staff Qualifications: ")
                print("1. Add Qualification")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Staff_Qualifications VALUES (%s, %s)"
                    qualification = input("Enter the Qualification: ")
                    cursor.execute(query, (staff_id, qualification))
                    con.commit()
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
                    con.commit()
                elif ch == 2:
                    break
            print("Staff Member added successfully")
        elif choice == 2:
            staff_id = int(input("Enter Staff ID: "))
            query = "DELETE FROM Staff WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffContactNumber WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffEmailID WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffDesignation WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Staff_Qualifications WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffMedicalConditions WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Teacher WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM TeachingAssistant WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM WorksForDepartment WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Teaches WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Dependent WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
        elif choice == 3:
            staff_id = int(input("Enter Staff ID: "))
            query = "SELECT * FROM Staff WHERE StaffID = %s"
            upd_row = dict()
            cursor.execute(query, (staff_id))
            result = cursor.fetchone()
            if result is None:
                print("Staff Member doesn't exist")
                continue
            print("\nUpdate Student Information")
            print("Press ENTER if no update is required, otherwise enter the new value: ")
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
                upd_row['BankAccountNumber'] = int(upd_row['BankAccountNumber'])
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
            cursor.execute(query, (upd_row['FirstName'], upd_row['LastName'], upd_row['Salary'], upd_row['BankAccountNumber'], upd_row['AadhaarNumber'], upd_row['Address'], upd_row['DOB'], upd_row['JoiningDate'], upd_row['PermanencyStatus'], staff_id))
            con.commit()
            print("Staff Member updated successfully")
        elif choice == 4:
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
            exit()
        else:
            print("Invalid choice")
