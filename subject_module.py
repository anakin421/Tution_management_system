from db_connect import * 

class subject:

    def __init__(self,sub_name = None):
        self.sub_name = sub_name

    def insert_sub_data(self):
        query = f"INSERT INTO subject (name) values (?)", (self.sub_name,)
        db_obj = database(query)
        db_obj.execute()

    def display(self):
        query = f"select * from subject"
        db_obj = database(query)
        x = db_obj.execute()
        for i in x:
            print(f"{i[0]} : {i[1]}")
        return x

    def update_sub_data(self,sub_id,up_sub_name):
        query = f"update subject set name = ? where id = ? ", (up_sub_name,sub_id)
        db_obj = database(query)
        db_obj.execute()

    def delete_sub_data(self,sub_id):
        query = f"delete from subject where id = ?", (sub_id,)
        db_obj = database(query)
        db_obj.execute()
