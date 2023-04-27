import sqlite3

class Db:
    id=1

    @staticmethod
    def create_tables():
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()

        query="DROP TABLE users"
        cursor.execute(query)
        conn.commit()
        # query= "DROP TABLE credits"
        # cursor.execute(query)
        # conn.commit()
        query="CREATE TABLE users(id TEXT, username TEXT, pass TEXT, credits TEXT)"
        cursor.execute(query)
        conn.commit()




    # create_tables(cursor,conn)
    @staticmethod
    def new_user(d):
        sd = d.split('&')
        us = sd[0].split('=')
        ps = sd[1].split('=')
        username = us[1]
        passw = ps[1]
        list=[Db.id,username,passw,'0']
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()


        find =f"SELECT * FROM users WHERE username = '{username}'"
        data = cursor.execute(find).fetchall()
        conn.commit()

        if(len(data)==0):
            query = f"INSERT INTO users(id, username, pass, credits) VALUES (? , ?, ?, ?) "
            cursor.execute(query,list)
            conn.commit()
            Db.id += 1
            return 1


        return 0


    @staticmethod
    def logIn(d):
        sd= d.split('&')
        us= sd[0].split('=')
        ps=sd[1].split('=')
        username=us[1]
        passw=ps[1]
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()

        find = f"SELECT * FROM users WHERE username = '{username}'"
        data = cursor.execute(find).fetchall()
        conn.commit()

        if len(data)==0:
            return 0


        if data[0][2]==passw:
            return data[0][0]+' '+data[0][1]+' '+data[0][3]
        else:
            return 0


    @staticmethod
    def addCredits(d):
        sd = d.split('&')
        cr = sd[0].split('=')
        print(cr)
        user = sd[1].split('=')
        username = user[1]
        credits = cr[1]
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()

        find = f"SELECT * FROM users WHERE username = '{username}'"
        data = cursor.execute(find).fetchall()
        conn.commit()

        if len(data)==0:
            return 0


        update = f"UPDATE users SET credits = '{str(int(data[0][3])+int(credits))}' WHERE username = '{username}'"
        cursor.execute(update)
        conn.commit()

        return 1



