import cgi
import cgitb

from mysql.connector.errors import DatabaseError

cgitb.enable()

import datetime as dt
#Following Lines required for HTTP
#print("Content-Type: text/html")    # HTML is following
#print("")                             # blank line, end of headers

import html

import session_handle as sh

try:
    import core.db as db
except ModuleNotFoundError:
    import db as db



dataBase = db.dataBaseConnector()
#requestsT = db.requestsTable()

form = cgi.FieldStorage()

sess = sh.start()


print("Content-Type: text/html")    # HTML is following
print("")



for item in form.getlist("APPROVE"):

    reqTab = dataBase.select("SELECT * FROM `requests` WHERE `id` = %s", (item, ))

    dataBase.execute("INSERT INTO `automotive`.`approved` (`id`, `firstName`, `lastName`, `EMail`, `phoneNumber`, `vMake`, `vModel`, `vYear`, `canBeLeft`, `descrip`, `datetime`, `whoApproved`, `whenApr`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, NULL);", (reqTab[0]["firstName"], reqTab[0]["lastName"], reqTab[0]["EMail"], reqTab[0]["phoneNumber"], reqTab[0]["vMake"], reqTab[0]["vModel"], reqTab[0]["vYear"], reqTab[0]["canBeLeft"], reqTab[0]["descrip"], reqTab[0]["datetime"] ))

    dataBase.execute("DELETE FROM `requests` WHERE `id` = %s", (reqTab["id"],))

    
for item in form.getlist("DELETE"):
    dataBase.execute("DELETE FROM `requests` WHERE `id` = %s", (item,))


print("<script>window.location.replace('/admin/index.shtml');</script>")
quit()


#print("HTTP/1.1 303 See Other")
#print("Location: index.html")


#print(form)
