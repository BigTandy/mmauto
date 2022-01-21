import mysql.connector
import json
from mysql.connector.errors import Error

dbCredF = open("C:\\!\\autoLogin.json")

dbCred = json.loads("".join(dbCredF.readlines()))
dbCredF.close()

#cnx = mysql.connector.connect(user=dbCred["user"], password=dbCred["password"], host="localhost", database="automotive")


class dataBaseConnector:

    def __init__(self):
        
        self.db = mysql.connector.connect(user=dbCred["user"], password=dbCred["password"], host="localhost", database="automotive")

    def select(self, query, values=()):
        cursor = self.db.cursor(dictionary=True, buffered=True)

        cursor.execute(query, values) # %s for item to be replaced in querry

        rows = cursor.fetchall()

        #db.commit()
        cursor.close()
        #db.close()

        return rows

    def execute(self, query, values):
        cursor = self.db.cursor(dictionary=True, buffered=True)

        cursor.execute(query, values) # %s for item to be replaced in querry

        self.db.commit()
        cursor.close()
        #db.close()

    def die(self):
        self.db.close()


class requestsTable(dataBaseConnector):

    def __init__(self):
        super().__init__()
    
    def select(self):
        return super().select("SELECT * FROM `requests`")
    
    def insert(self, vals: tuple):
        super().execute("INSERT INTO `automotive`.`requests` (`id`, `firstName`, `lastName`, `EMail`, `phoneNumber`, `vMake`, `vModel`, `vYear`, `canBeLeft`, `descrip`, `datetime`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", vals)
    

class sessionDBConnector(dataBaseConnector):
    def __init__(self):
        super().__init__()
    
    def select_all(self):
        return super().select("SELECT * FROM `sessions`")
    
    def select_id(self, sessID):
        return super().select("SELECT * FROM `sessions` WHERE `session_ident` = '%s'", sessID)

    def select_user(self, user):
        return super().select("SELECT * FROM `sessions` WHERE `sessUserIdent` = '%s'", user)
    
    def newCookie(self, sessID, user, data):

        dataAdd = []
        for datum in data:
            dataAdd.append(f"{datum}={data[datum]}")
        
        data = ":".join(dataAdd)

        #TODO F string cuz broken
        super().execute("INSERT INTO `automotive`.`sessions` (`id`, `session_ident`, `sessData`, `sessUserIdent`) VALUES (NULL, %s, %s, %s);", (sessID, data, user))
    
    def delete(self, sessID):
        super().execute("DELETE FROM `sessions` WHERE `session_ident` = '%s'", sessID)