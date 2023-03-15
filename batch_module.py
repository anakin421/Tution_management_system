from db_connect import * 

class batch:

    def __init__(self, b_name = None, b_time = None):
        self.b_name = b_name
        self.b_time = b_time

    def insert_batch_data(self):
        query = f"INSERT INTO batch (name,batch_time) values (?,?)", (self.b_name,self.b_time)
        db_obj = database(query)
        db_obj.execute()

    def display(self,std = None):
        if std == None:
            query = f"select * from batch"
            db_obj = database(query)
            x = db_obj.execute()

            print("---Batch Details---")
            for i in x:
                print(f"Id: {i[0]} | Name: {i[1]} | Time: {i[2]}")
            return [i[0] for i in x]

        else:
            query = "select distinct batch_id,count(*) from junction group by batch_id"
            db_obj = database(query)
            y = db_obj.execute()

            ls = [i[0] for i in y if i[1] == 6]
            ls1 = []
            print("---Batch Details---")

            for i in ls:
                query = f"select * from batch where id = ? and name like '%{std}%'", (i,)
                db_obj = database(query)
                x = db_obj.execute()
                for j in x:
                    print(f"Id: {j[0]} | Name: {j[1]} | Time: {j[2]}")
                    ls1.append(j[0])

            return ls1


    def update_batch_data(self,query):

        db_obj = database(query)
        db_obj.execute()

    def delete_batch_data(self,b_id): #working
        
        query = f"select count(*) from student11 where batch_id = ? union select count(*) from student12 where batch_id = ?", (b_id,b_id)
        db_obj = database(query)
        x = db_obj.execute()

        if (x[0][0] == 0) and (x[1][0] == 0):
            query = f"delete from batch where id = ?", (b_id,)    
            db_obj = database(query)
            db_obj.execute()
        else:
            print("can't delete batch have few students")

    def display_batch_day(self):
        query = f"select * from batch_day"
        db_obj = database(query)
        x = db_obj.execute()
        for i in x:
            print(f"{i[0]} : {i[1]}")
        return [i[0] for i in x]

    def set_batch_data(self,b_id,sub_id,t_id,bd_id):

        query = f"select count(*) from junction where batch_id = ? and bday_id = ?", (b_id,bd_id)
        db_obj = database(query)
        x = db_obj.execute()
        if x[0][0]:
            print("already exist")
        else:
            query = f"INSERT INTO junction (batch_id,sub_id,teacher_id,bday_id) values (?,?,?,?)", (b_id,sub_id,t_id,bd_id)
            db_obj = database(query)
            db_obj.execute()

    def show_timetable(self,b_id):

        query = f"select * from junction where batch_id = ?", (b_id,)
        db_obj = database(query)
        x = db_obj.execute()

        query = f"select name,batch_time from batch where id = ?",(b_id,)
        db_obj = database(query)
        b = db_obj.execute()

        print("---Batch TimeTable---")
        print(f"Batch: {b[0][0]} | Time: {b[0][1]}")
        print()
        for i in x:
            t_id = i[3]
            bd_id = i[4]

            query = f"select t.name,s.name from teacher as t inner join subject as s on t.sub_id = s.id where t.id  = ?", (t_id,)
            db_obj = database(query)
            ts = db_obj.execute()

            query = f"select name from batch_day where id = ?", (bd_id,)
            db_obj = database(query)
            bd = db_obj.execute()

            print(f"{i[0]}- Day: {bd[0][0]} | Subject: {ts[0][1]} | Teacher: {ts[0][0]}")


    def update_set_batch_data(self,b_id,sub_id,t_id):

        query = f"update junction set teacher_id = ? where batch_id = ? and sub_id = ?", (t_id,b_id,sub_id)
        db_obj = database(query)
        db_obj.execute()       

    def take_attendence(self,b_id,date,bd_id,std,att_day):

        table = 'student'+std
        att_table = 'attendence'+std

        query = f"select count(*) from '{att_table}' where atten_date = ? and batch_id = ?", (date,b_id)
        db_obj = database(query)
        att = db_obj.execute()
        if att[0][0]:
            print(f"you've already take attendence for this batch today")

        else:

            query = f"select teacher_id,id from junction where batch_id = ? and bday_id = ?", (b_id,bd_id)
            db_obj = database(query)
            x = db_obj.execute()

            query = f"select t.name,s.name from teacher as t inner join subject as s on t.sub_id = s.id where t.id  = ?", (x[0][0],)
            db_obj = database(query)
            y = db_obj.execute()

            query = f"select name,batch_time from batch where id = ?", (b_id,)
            db_obj = database(query)
            b = db_obj.execute()        

            query = f"select id,name from '{table}' where batch_id = ?", (b_id,)
            db_obj = database(query)
            stu_ids = db_obj.execute()
            id_ls = [str(i[0]) for i in stu_ids]
            name_ls = [i[1] for i in stu_ids]

            print(f"\n-----Take Attendence-----")
            print(f"\nDate : {date} | Day : {att_day} | Time: {b[0][1]}\nBatch: {b[0][0]}\nSubject: {y[0][1]} | Teacher: {y[0][0]} ")

            print()
            for i in range(len(id_ls)): 
                print(f"{id_ls[i]}: {name_ls[i]}")
                att  = input("p: Present | a: Absent >> ")
                query1 = f"INSERT INTO {att_table} (atten_date,stu_id,stu_name,batch_id,junc_id,attendence) VALUES (?,?,?,?,?,?)" , (date,id_ls[i],name_ls[i],b_id,x[0][1],att)
                db_obj1 = database(query1)
                db_obj1.execute()


    def track_attendence(self,b_id,date,bd_id,att_day,std):
        att_table = 'attendence'+std

        query = f"select count(*) from {att_table} where atten_date = ? and batch_id = ?",(date,b_id)
        db_obj = database(query)
        ack = db_obj.execute()   

        if ack[0][0]:

            query = f"SELECT stu_id,stu_name,attendence,junc_id FROM {att_table} where atten_date = ? and batch_id = ?", (date,b_id)
            db_obj = database(query)
            st = db_obj.execute()

            query = f"select teacher_id from junction where id = ?", (st[0][3],)
            db_obj = database(query)
            x = db_obj.execute()

            query = f"select t.name,s.name from teacher as t inner join subject as s on t.sub_id = s.id where t.id  = ?", (x[0][0],)
            db_obj = database(query)
            y = db_obj.execute()

            query = f"select name,batch_time from batch where id = ?", (b_id,)
            db_obj = database(query)
            b = db_obj.execute()  

            print("\n-----Attendence Record-----")
            print(f"\nDate : {date} | Day : {att_day} | Time : {b[0][1]}")
            print(f"Batch: {b[0][0]}\nSubject: {y[0][1]} | Teacher: {y[0][0]}")
            print(f"\nTotal student : {len(st)}")
            count = 0
            for i in st:
                if i[2] == 'p':
                    count += 1
            print(f"Present no of student : {count}")
            print(f"Absent no of student : {len(st) - count}")
            select = input("\nyou want to see more details y: Yes n: No >> ")
            print()
            if select.upper() == 'Y':
                for i in st:
                    print(f"{i[0]}: {i[1]} --> {i[2]}")

        else:
            print("No Record")