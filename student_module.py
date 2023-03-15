from db_connect import *

class student:

    def __init__(self,std=None,stu_name = None, b_id = None):
        self.std = std
        self.table = 'student'+self.std
        self.stu_name = stu_name
        self.b_id = b_id

    def insert_stu_data(self,pwd):

        query = f"INSERT INTO {self.table} (name,password,batch_id) values(?,?,?)", (self.stu_name,pwd,self.b_id)
        db_obj = database(query)
        db_obj.execute()

    def display(self,stu_id):

        query = f"select batch_id from {self.table} where id = ?", (stu_id,)
        db_obj = database(query)
        x = db_obj.execute()
        query = f"select s.id,s.name,b.name from {self.table} as s inner join batch as b on s.batch_id = b.id where b.id = ? and s.id = ?", (x[0][0],stu_id)
        db_obj = database(query)
        y = db_obj.execute()
        print("\n--student details--")
        print(f"Id: {y[0][0]}\nname: {y[0][1]}\nbatch: {y[0][2]}")


    def update_stu_data(self,query):

        db_obj = database(query)
        db_obj.execute()

    def delete_stu_data(self,stu_id):

        query = f"delete from {self.table} where id = ?", (stu_id,) 
        db_obj = database(query)
        db_obj.execute()
        print("deleted sucessfully!!")


    def get_existing_stu_id(self):
        query = f"select id from {'student'+self.std}"
        db_obj = database(query)
        x = db_obj.execute()
        ls = [str(i[0]) for i in x]
        return ls

    def login(self,stu_id,password):

        query = f"select id from {self.table} where id = ? and password = ?",(stu_id,password)
        db_obj = database(query)
        x = db_obj.execute()

        if not len(x):
            return False
        else:
            return True

    def get_attendence_record(self,stu_id):
        att_table = 'attendence'+self.std
        query = f"select atten_date,attendence from {att_table} where stu_id = ?", (stu_id,)
        db_obj = database(query)
        x = db_obj.execute()

        print("\n--Attendence Record--")
        for i in x:
            print(f"Date: {i[0]} --> {i[1]}")