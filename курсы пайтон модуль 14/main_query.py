import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="ruslan"

)

mycursor = mydb.cursor()

while True:
  print("PRESS 1 TO ADD PLAYER")
  print("PRESS 2 TO LIST PLAYERS")
  print("PRESS 0 TO EXIT")

  choice = input()

  if choice=="1":

    print("INSERT NAME:")
    name = input();
    print("INSERT NUMBER:")
    number = int(input())

    print("INSERT PRICE:")
    price = int(input())


    sql = "INSERT INTO players (id, name, number, price) VALUES (NULL, %s, %s, %s)"
    values = (name, number, price)
    mycursor.execute(sql,values)
    mydb.commit()

  elif choice=="2":

    sql = "SELECT * FROM players"
    mycursor.execute(sql)
    result = mycursor.fetchall()

    for player in result:
      print(str(player[0]) + " " + player[1] + " " + str(player[2]) + " " + str(player[3]) )


  elif choice=="0":
    mycursor.close()
    mydb.disconnect()
    break