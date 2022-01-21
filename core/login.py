#DO NOT TOUCH IT!!!!!!!!!!!!!!!!!!


import os, hashlib

import cgi
import cgitb

cgitb.enable()


import html
import db
import hashlib, os


import session_handle as sh

dataBase = db.dataBaseConnector()
un_form = cgi.FieldStorage()






form = {}

for item in un_form:
    #print(item)
    form[item] = html.escape(un_form[item].value)



def passHash(password, salt=None):
    if salt is None:
        salt = os.urandom(32)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'), salt, 100000)
    return (hashed, salt)


def passVer(password, salt, oldhash):
    newHash = passHash(password, salt)[0]
    if newHash == oldhash:
        return True
    else:
        return False


def fail(code):
    print("HTTP/1.1 400 Bad Request")
    print("Content-Type: text/html")    # HTML is following
    print("")

    print(f"<script>window.location.replace('/login_page/login.html#{code}');</script>")
    quit()





uname = form["uname"].rstrip().lstrip()
unameBreak = uname.split()

if len(unameBreak) != 2:
    fail("invalid")

fname = unameBreak[0]
lname = unameBreak[1]

users = dataBase.select("SELECT * FROM `users`", ())





for u in users:
    if (u["fName"] == fname) and (u["lName"] == lname):

        if passVer(form["pswd"], u["salt"], u["password"]):

            #old = sh.start()
            #if old != None:
                #raise Exception(old)
                #sh.kill(old[0])




            C = sh.setup(u["id"], {"name": [u["fName"], u["lName"]], "role": u["role"] })
            #print("HTTP/1.1 303 See Other")
            #print("Location: /admin/index.shtml")
            print("Content-Type: text/html")    # HTML is following
            print("")

            

            print("<script>window.location.replace('/admin/index.shtml');</script>")
            quit()
        else:
            fail("pass")
else:
    fail("userNF")

