import mysql.connector


mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Abcd@123",
    database= "emp"
   
    
)
mycursor= mydb.cursor()


def addtodb(ac,nm,amunt,dt):
    x = (ac, nm, amunt,dt)
    mycursor.execute("INSERT INTO employee (ac,name,amt,dt) VALUES (%s,%s,%s,%s)",x)
    mydb.commit()

    return "yes"
#def maxid():
#    
#    mycursor.execute("select sr from employee where sr = @MaxId ")
#    no = mycursor.fetchall()
#    for row in no:
#        print(row[0])

    
