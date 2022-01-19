import cgi
import cgitb

cgitb.enable()


import core.db as db

#dataBase = db.dataBaseConnector()
requestsT = db.requestsTable()


import core.session_handle as session





#Following Lines required for HTTP
#print("Content-Type: text/html")    # HTML is following
#print("")                             # blank line, end of headers

#print(requestsT.select())


print("""
<table>
<tr>
    <th>Name</th>
    <th>E-Mail</th>
    <th>Phone Number</th>
    <th>Make & Model</th>
    <th>Can be left?</th>
    <th>Description</th>
    <th>Approve?</th>
    <th>Delete?</th>
</tr>

""")

canLeft = {
    1: "Yes",
    0: "No"
}

for req in requestsT.select():
    print(f"""
    <tr>
        <td>{req["firstName"] + " " + req["lastName"]}</td>
        <td>{req["EMail"]}</td>
        <td>{req["phoneNumber"]}</td>
        <td>{req["vMake"] + " " + req["vModel"]}</td>
        <td>{canLeft[req["canBeLeft"]]}</td>
        <td>{req["descrip"]}</td>
        <td>
            <input type="checkbox" name="APPROVE" value="{req["id"]}" />
         </td>
        <td>
            <input type="checkbox" name="DELETE" value="{req["id"]}" />
        </td>
    </tr>
    """)

print("</table>")

#sess = session.start()
#if sess is None:
#    key = session.setup(0, {"Arggg": "Help me", "testetstestest": "Hi"})
#    print(key)
#else:
#    print(sess)