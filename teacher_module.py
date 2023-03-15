from db_connect import * 

class teacher:

    def __init__(self,t_name = None, sub_id = None):
        self.t_name = t_name
        self.sub_id = sub_id

    def insert_teacher_data(self,pwd):
        query = f"INSERT INTO teacher (name,sub_id,password) values (?,?,?)", (self.t_name,self.sub_id,pwd)
        db_obj = database(query)
        db_obj.execute()

    def display(self,sub_id = None):
        # query = f"select teacher.id,teacher.name,teacher.subject,batch.name from batch inner join teacher on batch.teacher_id = teacher.id where batch.teacher_id = ?", (self.t_id,)      
        if sub_id == None:
            query = f"select t.id,t.name,s.name from teacher as t inner join subject as s on t.sub_id = s.id"
            db_obj = database(query)
            x = db_obj.execute()
            print("\n--Teacher Details--")
            for i in x:
                print(f"Id: {i[0]} | name: {i[1]} | subject: {i[2]}")
            return [i[0] for i in x]
           
        else:
            query = f"select t.id,t.name,s.name from teacher as t inner join subject as s on t.sub_id = s.id where sub_id = ?", (sub_id,)
            db_obj = database(query)
            x = db_obj.execute()
            print("\n--Teacher Details--")
            for i in x:
                print(f"Id: {i[0]} | name: {i[1]} | subject: {i[2]}")
            return [i[0] for i in x]  


    def update_teacher_data(self,t_id,up_teacher_name):
        query = f"UPDATE teacher SET name = ? WHERE id = ?",(up_teacher_name,t_id)
        db_obj = database(query)
        db_obj.execute()
 
    def delete_teacher_data(self,t_id):  #working
        query = f"delete from teacher where id = ?", (t_id,)
        db_obj = database(query)
        db_obj.execute()

    def login(self,t_id,pwd):
        query = f"select id from teacher where id = ? and password = ?", (t_id,pwd)
        db_obj = database(query)
        x = db_obj.execute()   
        
        if not len(x):
            return False
        else:
            return True

    def teacher_info(self,t_id):
        query = f"select t.id,t.name,s.name from teacher as t inner join subject as s on t.sub_id = s.id where t.id = ? and t.sub_id = (select t.sub_id from teacher where t.id = ?)", (t_id,t_id)
        db_obj = database(query)
        x = db_obj.execute()   

        query = f"select distinct batch_id from junction where teacher_id = ?",(t_id,)
        db_obj = database(query)
        b = db_obj.execute()  
        b_ids =  [i[0] for i in b]
        b_name = []

        for i in b_ids:
            query = f"select name from batch where id = ?", (i,)
            db_obj = database(query)
            bname = db_obj.execute()
            b_name.append(bname[0][0])    

        print("\n--Information--")
        print(f"Name: {x[0][1]}\nSubject: {x[0][2]}\nBatches: {','.join(b_name)}")
        return b_name