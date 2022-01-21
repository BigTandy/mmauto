import cgi
import cgitb

cgitb.enable()

import datetime as dt
#Following Lines required for HTTP
#print("Content-Type: text/html")    # HTML is following
#print("")                             # blank line, end of headers

import html
#import core.db as db

#dataBase = db.dataBaseConnector()
#requestsT = db.requestsTable()

form = cgi.FieldStorage()

print("Content-Type: text/html")    # HTML is following
print("")


for item in form:
    print(f"{item} ~ {form[item]}<br>")
    if isinstance(form[item], list):
        for car in form[item]:
            print(f"<i>{car}</i><br>")





#requestsT.insert((form["fname"], form["lname"], form["email"], form["phone"], form["vehicle_make"], form["vehicle_model"], form["vehicle_year"], vLeft, form["description"], dt.datetime.now()))


#print(requestsT.select())

#print("HTTP/1.1 303 See Other")
#print("Location: index.html")


#print(form)
