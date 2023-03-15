from datetime import datetime
import student_module as sm
import teacher_module as tm
import subject_module as subm
import batch_module as bm
import re
 
def main_panel():

    while True:

        while True:  
            print("\n-----Admin Panel-----\n")
            print("1:Student management\n2:Teacher management\n3:Batch management\n4:subject management\n5:Back")
            select = input("\nmake choice: ")
            try:
                assert ord(select)>48 and ord(select)<54
                break
            except:
                print("Invalid entry")


        if select == '1':
            # global s, b
            while True:
                print("\n1:Insert Student\n2:Display Student\n3:Update Student\n4:Delete Student\n5:Back")
                choice = input("\nmake choice: ")
                try:
                    assert ord(choice)>48 and ord(choice)<54
                    break
                except:
                    print("Invalid entry")

            if choice == '1':
                while True:
                    std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
                    if std == '11' or std == '12':
                        break
                    else:
                        print("select 11 or 12")   
                stu_name = (re.sub(' +', ' ',input("enter student name: "))).strip()
                b = bm.batch()
                ls1 = b.display(std = std)
                b_id = int(input("\nenter batch: "))
                if b_id in ls1:
                    while True:
                        pwd = (re.sub(' +', ' ',input("enter Password: "))).strip() 
                        if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})",pwd):
                            break
                        else:
                            print("Password must have 1 lowercase alphabet, 1 uppercase alphabet, 1 numeric, 1 special symbol and at least 8 characters")

                    s = sm.student(std=std,stu_name=stu_name,b_id=b_id)
                    s.insert_stu_data(pwd)
                else:
                    print("Invalid entry")

            elif choice == '2':
                while True:
                    std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
                    if std == '11' or std == '12':
                        break
                    else:
                        print("select 11 or 12") 
                s = sm.student(std = std)
                s_id_ls =  s.get_existing_stu_id()
                print(f"existing stu id: {' | '.join(s_id_ls)}")
                stu_id = int(input("select stu id: "))
                if str(stu_id) in s_id_ls: 
                    s.display(stu_id)
                else:
                    print("Invalid entry")

            elif choice == '3':
                while True:
                    std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
                    if std == '11' or std == '12':
                        break
                    else:
                        print("select 11 or 12")
                s = sm.student(std = std)
                s_id_ls =  s.get_existing_stu_id()
                print(f"existing stu id: {' | '.join(s_id_ls)}")
                stu_id = int(input("select stu id: "))
                if str(stu_id) in s_id_ls:
                    while True:                        
                        print("1:Update name\n2:Update Batch\n3:Back")
                        choose = input("\nmake choice: ")
                        try:
                            assert ord(choose)>48 and ord(choose)<52
                            break
                        except:
                            print("Invalid entry\n")

                    if choose == '1':
                        up_stu_name = (re.sub(' +', ' ',input("enter student name: "))).strip()
                        query = f"update {'student'+std} set name = ? where id = ?", (up_stu_name,stu_id)
                        s.update_stu_data(query)

                    elif choose == '2':
                        b = bm.batch()
                        ls = b.display(std = std)
                        b_id = int(input("\nenter batch: "))
                        if b_id in ls:
                            query = f"update {'student'+std} set batch_id = ? where id = ?", (b_id,stu_id)
                            s.update_stu_data(query)

                    elif choose == '3':
                        pass


                else:
                    print("Invalid entry")

            elif choice == '4':
                while True:
                    std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
                    if std == '11' or std == '12':
                        break
                    else:
                        print("select 11 or 12")
                s = sm.student(std = std)
                s_id_ls =  s.get_existing_stu_id()
                print(f"existing stu id: {' | '.join(s_id_ls)}")
                stu_id = int(input("select stu id: "))
                if str(stu_id) in s_id_ls:
                    s.display(stu_id)
                    choose = input("\nWant to delete Y:yes N:no >> ")
                    if choose.upper()  == "Y":
                        s.delete_stu_data(stu_id)    

            elif choice == '5':
                pass

        elif select == '2':
            # global t
            while True:

                print("1:Insert Teacher\n2:Display Teacher\n3:Update Teacher\n4:Delete Teacher\n5:Back")
                choice = input("\nmake choice: ")

                try:
                    assert ord(choice)>48 and ord(choice)<54
                    break
                except:
                    print("Invalid entry")


            if choice == '1':

                t_name = (re.sub(' +', ' ',input("enter teacher name: "))).strip()
                s = subm.subject()
                print("Subject: ")
                x = s.display()
                ls = [i[0] for i in x]
                sub_id = int(input("\nselect subject for teacher: "))
                if sub_id in ls:
                    while True:
                        pwd = (re.sub(' +', ' ',input("enter Password: "))).strip() 
                        if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})",pwd):
                            break
                        else:
                            print("Password must have 1 lowercase alphabet, 1 uppercase alphabet, 1 numeric, 1 special symbol and at least 8 characters")

                    t = tm.teacher(t_name = t_name,sub_id = sub_id)
                    t.insert_teacher_data(pwd)
                else:
                    print("Invalid entry")

            elif choice == '2':

                t = tm.teacher()
                t.display()

            elif choice == '3':

                t = tm.teacher()
                ls = t.display()
                t_id = int(input("\nenter teacher id you want to Update: "))
                if t_id in ls:
                    up_teacher_name = (re.sub(' +', ' ',input("Update teacher name: "))).strip()
                    t.update_teacher_data(t_id,up_teacher_name)
                else:
                    print("Invalid entry")


            elif choice == '4':

                t = tm.teacher()
                ls = t.display()
                t_id = int(input("\nenter teacher id you want to delete: "))
                if t_id in ls:
                    b = t.teacher_info(t_id)

                    choose = input("\nWant to delete Y:yes N:no >> ")
                    if choose.upper()  == "Y":
                        if len(b):
                            print("\ncan't delete teacher has few batches")
                        else:
                            t.delete_teacher_data(t_id)
                else:
                    print("Invalid entry")

            elif choice == '5':
                pass

        elif select == '3':
            # global b
            while True:
                print("1:Insert Batch\n2:Display Batch\n3:Update Batch\n4:Delete Batch\n5:Set Batch\n6:Batch TimeTable\n7:Take Attendence\n8:Track Attendence\n9:Update Set Batch\n0:Back")
                choice = input("\nmake choice: ")

                try:
                    assert ord(choice)>47 and ord(choice)<58
                    break
                except:
                    print("Invalid entry")


            if choice == '1':
                print("---enter batch details here---")
                b_name = (re.sub(' +', ' ',input("enter batch name: "))).strip()
                b_time = datetime.strptime(input("enter time:"), "%I %p").strftime("%I:%M %p")
                b = bm.batch(b_name = b_name, b_time = b_time)
                b.insert_batch_data()

            elif choice == '2':
                b = bm.batch()
                b.display()

            elif choice == '3':
                b = bm.batch()
                ls = b.display()
                b_id = int(input("\nenter batch id you want to Update: "))
                if b_id in ls:
                    while True:
                        print("1:Update name\n2:Update Time\n3:Back")
                        choose = input("\nmake choice: ")
                        try:
                            assert ord(choose)>48 and ord(choose)<52
                            break
                        except:
                            print("Invalid entry\n")

                    if choose == '1':
                        up_b_name = (re.sub(' +', ' ',input("enter batch name: "))).strip()
                        query = f"update batch set name = ? where id = ?", (up_b_name,b_id)
                        b.update_batch_data(query)

                    elif choose == '2':
                        up_b_time = datetime.strptime(input("enter time:"), "%I %p").strftime("%I:%M %p")
                        query = f"update batch set batch_time = ? where id = ?", (up_b_time,b_id)
                        b.update_batch_data(query)
                    
                    elif choose == '3':
                        pass

                else:
                    print("Invalid entry")

            elif choice == '4':

                b = bm.batch()
                ls = b.display()
                b_id = int(input("\nenter batch id you want to delete: "))
                if b_id in ls:
                    b.delete_batch_data(b_id)
                else:
                    print("Invalid entry")

            elif choice == '5':
                print("-- Batches --")
                b = bm.batch()
                ls = b.display()
                b_id = int(input("\nenter batch you want to set: "))
                if b_id in ls:
                    print("-- Subject --")
                    sb = subm.subject()
                    x = sb.display()
                    ls1 = [i[0] for i in x]
                    sub_id = int(input("select subject: "))
                    if sub_id in ls1:
                        print("-- Teacher --")
                        t = tm.teacher()
                        ls2 = t.display(sub_id)
                        t_id = int(input("\nenter teacher: "))
                        if t_id in ls2:
                            print("-- Batch Day --")
                            ls3 = b.display_batch_day()
                            bd_id = int(input("\nenter batch day: "))
                            if bd_id in ls3:
                                b.set_batch_data(b_id,sub_id,t_id,bd_id)
                            else:
                                print("Invalid")
                        else:
                            print("Invalid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid entry")

            elif choice == '6':
                b = bm.batch()
                ls = b.display()
                b_id = int(input("\nenter batch: "))
                if b_id in ls:
                    b.show_timetable(b_id)           
                else:
                    print("Invalid entry")


            elif choice == '7':
                print("--Take Attendence of Students--")
                while True:
                    try:
                        date = datetime.strptime(input("Enter Date of attendence in dd/mm/yy format: "),'%d/%m/%y').date()
                        att_day_id = date.weekday()
                        att_day = date.strftime("%A")
                        break
                    except(ValueError,TypeError):
                        print("Invalid!! Try again")

                if att_day_id == 6:
                    print(f"---It's {att_day} Holiday---")
                    continue                
                while True:
                    std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
                    if std == '11' or std == '12':
                        break
                    else:
                        print("select 11 or 12")
                print()
                b = bm.batch()
                ls = b.display(std)
                b_id = int(input("\nenter batch: "))
                if b_id in ls:
                    b.take_attendence(b_id = b_id,date = date,bd_id =att_day_id,std = std,att_day = att_day)
                else:
                    print("Invalid entry")

            elif choice == '8':
                print("--Track Attendence--")
                while True:
                    try:
                        date = datetime.strptime(input("Enter Date of attendence in dd/mm/yy format: "),'%d/%m/%y').date()
                        att_day_id = date.weekday()
                        att_day = date.strftime("%A")
                        break
                    except(ValueError,TypeError):
                        print("Invalid!! Try again")
                    
                if att_day_id == 6:
                    print(f"---It's {att_day} Holiday---")
                    continue                
                while True:
                    std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
                    if std == '11' or std == '12':
                        break
                    else:
                        print("select 11 or 12")
                print()
                b = bm.batch()
                ls = b.display(std)
                b_id = int(input("\nselect batch: "))
                if b_id in ls:
                    b.track_attendence(b_id = b_id,date = date,bd_id =att_day_id,att_day =att_day,std = std)

                else:
                    print("Invalid entry")

            elif choice == '9':
                b = bm.batch()
                ls = b.display()
                b_id = int(input("\nenter batch: "))
                if b_id in ls:
                    b.show_timetable(b_id)
                    print("\nUpdate teacher here")
                    print("-- Subject --")
                    sb = subm.subject()
                    x = sb.display()
                    ls1 = [i[0] for i in x]
                    sub_id = int(input("select subject: "))
                    if sub_id in ls1:
                        print("-- Teacher --")
                        t = tm.teacher()
                        ls2 = t.display(sub_id)
                        t_id = int(input("\nselect teacher: "))
                        b.update_set_batch_data(b_id,sub_id,t_id)
                else:
                    print("Invalid entry")

            elif choice == '0':
                pass

        elif select == '4':

            while True:
                print("1:add subject\n2:display subject\n3:Update subject\n4:delete subject\n5:Back")
                choice = input("\nmake choice: ")

                try:
                    assert ord(choice)>48 and ord(choice)<54
                    break
                except:
                    print("Invalid entry")

            if choice == '1':
                sub_name = (re.sub(' +', ' ',input("enter subject name: "))).strip()
                sb = subm.subject(sub_name)
                sb.insert_sub_data()

            elif choice == '2':
                sb = subm.subject()
                sb.display()

            elif choice == '3':
                sb = subm.subject()
                x = sb.display()
                ls = [i[0] for i in x]
                sub_id = int(input("select sub_id you want to Update: "))
                if sub_id in ls:
                    up_sub_name = (re.sub(' +', ' ',input("enter subject name for Update: "))).strip()
                    sb.update_sub_data(sub_id,up_sub_name)
                else:
                    print("Invalid entry")

            elif choice == '4':
                sb = subm.subject()
                x = sb.display()
                ls = [i[0] for i in x]
                sub_id = int(input("select sub_id you want to delete: "))
                if sub_id in ls:
                    sb.delete_sub_data(sub_id)
                else:
                    print("Invalid entry")

            elif choice == '5':
                pass


        elif select == '5':
            break

        # else:
        #     print("Invalid entry")

def student_panel():
    while True:
        std = (re.sub(' +', ' ',input("enter student standard: "))).strip() 
        if std == '11' or std == '12':
            break
        else:
            print("select 11 or 12")
    stu_id = int(input("Enter student id: "))
    password = (re.sub(' +', ' ',input("Enter password: "))).strip()
    s = sm.student(std)
    ack = s.login(stu_id,password)

    if ack:
        s.display(stu_id)
        select = input("\nWant to see attendence record ? Y:yes N:no >> ")
        if select.upper() == 'Y':
            s.get_attendence_record(stu_id)

    else:
        print("Invalid information")

def teacher_panel():
    t_id = int(input("Enter Teacher id: "))
    password = (re.sub(' +', ' ',input("Enter password: "))).strip()
    t = tm.teacher()
    ack = t.login(t_id,password)

    if ack:
        t.teacher_info(t_id)

    else:
        print("Invalid information")

def main():

    while True:

        while True:

            print("\n-----Tution management system-----\n")        
            print("1:Admin panel\n2:Student panel\n3:Teacher panel\n4:exit")
            select = input("\nmake choice: ")
            try:
                assert ord(select)>48 and ord(select)<53
                break
            except:
                print("Invalid entry")


        if select == '1':
            # pwd = int(input("Enter Password: "))
            pwd = 4546
            if pwd == 4546:
                main_panel()
            else:
                print("Invalid entry")

        elif select == '2':
            student_panel()

        elif select == '3':
            teacher_panel() 

        elif select == '4':
            exit()

        # else:
        #     print("Invalid entry")


if __name__ == "__main__":
    main()