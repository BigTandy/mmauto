import cgi
import cgitb

cgitb.enable()


import html
import db as db
import hashlib, os


dataBase = db.dataBaseConnector()


un_form = cgi.FieldStorage()

#print(un_form)

#print("Content-Type: text/html")    # HTML is following
#print("")

#print(un_form)

form = {}

for item in un_form:
    #print(item)
    form[item] = html.escape(un_form[item].value)



#print(requestsT.select())





def passHash(password, salt=None):
    if salt is None:
        salt = os.urandom(32)

    hashed = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'), salt, 100000)
    #print(len(hashed))
    return (hashed, salt)


passSalt = passHash(form["pswd"])

dataBase.execute("INSERT INTO `users` (`id`, `fName`, `lName`, `role`, `password`, `salt`) VALUES (NULL, %s, %s, 0, %s, %s)", (form["firstname"], form["lastname"], passSalt[0], passSalt[1]))

print("HTTP/1.1 303 See Other")
print("Location: /login_page/login.html")
print("Content-Type: text/html")    # HTML is following
print("")
