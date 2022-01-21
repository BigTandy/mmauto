import cgi
import cgitb

cgitb.enable()

import datetime as dt
#Following Lines required for HTTP
#print("Content-Type: text/html")    # HTML is following
#print("")                             # blank line, end of headers

import html
import core.db as db
dataBase = db.dataBaseConnector()
requestsT = db.requestsTable()

un_form = cgi.FieldStorage()

#print(un_form)

vLeft = None
if un_form["vehicle_left"].value == "Yes":
    vLeft = True
else:
    vLeft = False

form = {}

for item in un_form:
    #print(item)
    form[item] = html.escape(un_form[item].value)



requestsT.insert((form["fname"], form["lname"], form["email"], form["phone"], form["vehicle_make"], form["vehicle_model"], form["vehicle_year"], vLeft, form["description"], dt.datetime.now()))


#print(requestsT.select())

print("HTTP/1.1 303 See Other")
print("Location: index.html")
print("Content-Type: text/html")    # HTML is following
      
print("")

