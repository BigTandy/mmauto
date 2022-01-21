#DO NOT TOUCH IT!!!!!!!!!!!!!!!!!!


import cgi
import cgitb

cgitb.enable()

import os
import http
from http import cookies

import random as rand, string


try:
    import db as db
except ModuleNotFoundError:
    import core.db as db


import datetime as dt

from mysql.connector.errors import IntegrityError

dbConn = db.sessionDBConnector()


def tokenGen(leng=50):
    temp = []
    for i in range(leng):
        temp.append(rand.choice(string.ascii_letters + string.digits))
    return "".join(temp)

#C = cookies.SimpleCookie()
# C["Key"] = Value
# C.load(Header)

#C = cookies.SimpleCookie()
#C["Teest"] = "Ok"
#C["Help"] = "D:"
#C["Hhhhhhhhhhhhh"] = "Amogosussed"
#print(C)
# C.load(Header)

#Following Lines required for HTTP
#print("Content-Type: text/html")    # HTML is following
#print("")                             # blank line, end of headers

grabbed_cookies = ""

for headername, headervalue in os.environ.items():
    if headername.startswith("HTTP_"):
        #print(f"{headername} = {headervalue} <br>")
        if headername == "HTTP_COOKIE":
            grabbed_cookies = headervalue.split(";")
            break


dict_cookies = {}

for cook in grabbed_cookies:
    eq = cook.find("=")
    dict_cookies[cook[:eq]] = cook[eq + 1:]

#print(dict_cookies)


PulledCookies = dict_cookies
try:
    sessionID = dict_cookies["SESS_ID"]
except KeyError:
    sessionID = None

#PulledCookies = None
#sessionID = None
user = None
isSet = None


def start():
    
    #CALL DB TO GRAB ALL VALUES STORED WITH THAT SESS_ID

    if sessionID is None:
        return None

    allSessions = dbConn.select_all()


    for entry in allSessions:
        if entry["session_ident"] == sessionID:
            foundSess = entry
            break           
        else: continue
    else:
        #raise Exception(f"Not Found; AllSess: {allSessions}; SessID: {sessionID}")
        return None
    


    tempSessData = foundSess["sessData"]

    tempSessData = tempSessData.split(":")

    sessionData = {}

    for datum in tempSessData:
        eqSignLoc = datum.find("=")
        sessionData[datum[:eqSignLoc]] = datum[eqSignLoc + 1:]


    return (sessionID, sessionData, foundSess["sessUserIdent"])
    

    #print(dict_cookies)

def setup(user: int, data: dict): #User is the users internal ID, might be a security issue but in press of time im doing it for now -Bud

    #https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie


    #if session already exists kill old one and make new one
    newSessionId = tokenGen()


    

    try:
        dbConn.newCookie(newSessionId, user, data)
    except IntegrityError:
        allSess = dbConn.select_all()

        for sess in allSess:
            if sess["sessUserIdent"] == user:
                #raise Exception(sess)
                dbConn.execute(f"DELETE FROM `sessions` WHERE `session_ident` = '{sess['session_ident']}'", ())
                #dbConn.delete(sess["session_ident"])
                dbConn.newCookie(newSessionId, user, data)
                break
        else:
            raise Exception("Old Session Not Found")
    finally:

        today = dt.date.today()
        cLen = dt.timedelta(days=1)
        when = today + cLen

        C = cookies.SimpleCookie()
        C["SESS_ID"] = newSessionId
        C["SESS_ID"]["expires"] = when
        C["SESS_ID"]["path"] = "/"
        print(C)

        
        #print(f"""
        #<script>
        #    document.cookie = "SESS_ID={newSessionId}; expires={str(when)}; path='/'";
        #</script>
        #""")
        #raise Exception(f"oldID={sessionID}, newID={newSessionId}")

        return C


def setValue(key, value):
    pass

def kill(key):
    dbConn.delete(key)

