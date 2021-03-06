import subprocess as sp
import pymysql
import pymysql.cursors
import getpass
from staff import *
from student import *
from course import *


def admin_login(admin_id, admin_password):
    try:
        query = "SELECT * FROM Staff WHERE StaffID = %s AND DOB = %s"
        cur.execute(query, (admin_id, admin_password))
        row = cur.fetchone()
        if row is None:
            print("Not Registered\n")
            return -1
        else:
            print("You are logged in.\n")
            return 1
    except Exception as e:
        print("Error: ", e)
        return -1


def admin():
    while True:
        print("Edit an entity: ")
        print("1. Student")
        print("2. Guardian")
        print("3. Student Contact")
        print("4. Student Email")
        print("5. Student Medical Conditions")
        print("6. Student Emergency Contacts")
        print("7. Student Courses")
        print("8. Staff")
        print("9. Course")
        print("10. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            student(con, cur)
        elif ch == 2:
            guardian(con, cur)
        elif ch == 3:
            student_contact(con, cur)
        elif ch == 4:
            student_email(con, cur)
        elif ch == 5:
            student_medical_conditions(con, cur)
        elif ch == 6:
            student_emergency(con, cur)
        elif ch == 7:
            Student_Courses(con, cur)
        elif ch == 8:
            staff(con, cur)
        elif ch == 9:
            course(con, cur)
        elif ch == 10:
            break


def user_login(user_id, user_password):
    try:
        query = "SELECT * FROM Student WHERE StudentID = %s AND DOB = %s"
        cur.execute(query, (user_id, user_password))
        row = cur.fetchone()
        if row is None:
            print("Not Registered\n")
            return -1
        else:
            print("You are logged in.\n")
            return 1
    except Exception as e:
        print("Error: ", e)
        return -1


def user(con, cur):
    return


while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    try:
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=password,
                              db='COLLEGE_MANAGEMENT_SYSTEM',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)
        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE> ")
        with con.cursor() as cur:
            while(1):
                # tmp = sp.call('clear', shell=True)
                print("Login/Register:")
                print("1. Login as Administrator")
                print("2. Login as User")
                print("3. Register as User")
                print("4. Exit")
                choice = int(input(""))
                if choice == 1:
                    while 1:
                        admin_id = int(
                            input("Enter your id to login as administrator: "))
                        admin_password = getpass.getpass(
                            "Enter your Date of Birth to login as administrator: ")
                        result = admin_login(admin_id, admin_password)
                        if result == 1:
                            print("Login Successful")
                            admin()
                        else:
                            print("Login Failed")
                            print("Enter your choice: ")
                            print("1. Login")
                            print("2. Go back")
                            choice = int(input(""))
                            if choice == 1:
                                continue
                            else:
                                break
                elif choice == 2:
                    while 1:
                        user_id = int(
                            input("Enter your id to login as administrator: "))
                        user_password = getpass.getpass(
                            "Enter your Date of Birth to login as administrator: ")
                        result = user_login(user_id, user_password)
                        if result == 1:
                            print("Login Successful")
                            user(con, cur)
                        else:
                            print("Login Failed")
                            print("Enter your choice: ")
                            print("1. Login")
                            print("2. Go back")
                            choice = int(input(""))
                            if choice == 1:
                                continue
                            else:
                                break
                elif choice == 3:
                    exit()
                elif choice == 4:
                    exit()
                else:
                    print("Invalid Choice.")

    except Exception as e:
        # tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
