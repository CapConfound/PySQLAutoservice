import mysql.connector

class database:
    
    def __getConnection(self):

        try:
            return mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='root',
                database='autoservice'
            )
        except mysql.connector.Error as err:
            print(err)


    def getCursor(self):
        return self.__connect().cursor()

    def closeConn(conn):
        conn.close()
        
    def __init__(self) -> None:
        con = self.connect()
        print("Success!")
        return con
    
    