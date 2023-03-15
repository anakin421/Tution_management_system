from db_connect import * 

class tution:

    def __init__(self,b_name = None,b_sub = None,b_day = None,b_time = None):
        self.b_name = b_name
        self.b_sub = b_sub
        self.b_day = b_day
        self.b_time = b_time

    # def insert_batch_data(self,teacher_id): 
    #     query = f"INSERT INTO batch (name,subject,batch_day,batch_time,teacher_id) values (?,?,?,?,?)", (self.b_name,self.b_sub,self.b_day,self.b_time,teacher_id)
    #     db_obj = database(query)
    #     db_obj.execute()

    def display(self):
        query = f"select * from batch where name = ?", (self.b_name,)
        db_obj = database(query)
        x = db_obj.execute()
        print(f"\nBatch : {self.b_name} | Time : {x[0][4]}")
        for i in x:
            print(f"Days : {i[3]} | Subject : {i[2]}")


    def take_attendence(self,date,att_day,std):

        query = f"select b.name,b.subject,b.batch_time,t.name from batch as b inner join teacher as t on b.teacher_id = t.id where b.name = ? and b.batch_day like '%{att_day}%'", (self.b_name,)
        db_obj = database(query)
        x = db_obj.execute()
        table = 'student'+std
        att_table = 'attendence'+std
        sub = x[0][1]
        query = f"select count(*) from '{att_table}' where atten_date = ? and stu_batch = ?", (date,self.b_name)
        db_obj = database(query)
        att = db_obj.execute()
        if att[0][0]:
            print(f"you've already take attendence for {self.b_name} batch")

        else:
            query = f"select id,name from '{table}' where batch = ?", (self.b_name,)
            db_obj = database(query)
            stu_ids = db_obj.execute()
            id_ls = [str(i[0]) for i in stu_ids]
            name_ls = [i[1] for i in stu_ids]

            print(f"\n-----Take Attendence of {self.b_name}-----")
            print(f"\nDate : {date} | Day : {att_day} | Time: {x[0][2]}\nBatch: {x[0][0]}\nSubject: {sub} | Teacher: {x[0][3]} ")

            print()
            for i in range(len(id_ls)): 
                print(f"{id_ls[i]}: {name_ls[i]}")
                att  = input("p: Present | a: Absent >> ")
                query1 = f"INSERT INTO {att_table} (atten_date,stu_id,stu_name,stu_batch,subject,attendence) VALUES (?,?,?,?,?,?)" , (date,id_ls[i],name_ls[i],self.b_name,sub,att)
                db_obj1 = database(query1)
                db_obj1.execute()

    def track_attendence(self,date,att_day,std):
        att_table = 'attendence'+std

        query = f"SELECT stu_id,stu_name,attendence FROM {att_table} where atten_date = ? and stu_batch = ?", (date,self.b_name)
        db_obj = database(query)
        x = db_obj.execute()

        query1 = f"select b.subject,b.batch_time,t.name from batch as b inner join teacher as t on b.teacher_id = t.id where b.name = ? and b.batch_day like '%{att_day}%'", (self.b_name,)
        db_obj1 = database(query1)
        y = db_obj1.execute()

        print("\n-----Attendence Record-----")
        print(f"\nDate : {date} | Day : {att_day} | Time : {y[0][1]}")
        print(f"Batch: {self.b_name}\nSubject: {y[0][0]} | Teacher: {y[0][2]}")
        print(f"\nTotal student : {len(x)}")
        count = 0
        for i in x:
            if i[2] == 'p':
                count += 1
        print(f"Present no of student : {count}")
        print(f"Absent no of student : {len(x) - count}")
        select = input("\nyou want to see more details y: Yes n: No >> ")
        print()
        if select.upper() == 'Y':
            for i in x:
                print(f"{i[0]}: {i[1]} --> {i[2]}")


    def update_batch_data(self,query):
        db_obj = database(query)
        db_obj.execute()

    def delete_batch_data(self):
        table = 'student'+self.b_name[:2]
        query = f"select id from '{table}' where batch = ?", (self.b_name,)
        db_obj = database(query)
        x = db_obj.execute()
        if not len(x):
            query = f"delete from batch where name = ?", (self.b_name,)
            db_obj = database(query)
            db_obj.execute()
            print("deleted successfully!! ")
        else:
            print("can't delete the batch because it has students")
