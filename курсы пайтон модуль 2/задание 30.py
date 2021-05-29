x=int(input("Choose your branch:\n 1 - Science\n 2 - Humanitarian subjects\n 3 - Art\n 4 - Sport\n"))
print()
if x==1:
    print("(Вы выбрали Science - Науку , сделайте свой выбор дальше в какую "
          "отрасль хотите пойти\n 1 - Math\n 2 - Physics\n")
    y=int(input("сделайте свой выбор: "))
    if y==1:
        print("You are Financier")
    elif y==2:
        print("You are Engineer")
elif x==2:
    print("Вы выбрали Humanitarian subjects - Гуманитарные предметы,"
          "сделайте свой выбор дальше в какую отрасль хотите пойти \n 1 - History\n 2 - Foreign Languages:\n")
    y = int(input("сделайте свой выбор: "))
    if y==1:
        print("You are Historic or Diplomat ")
    elif y==2:
        print("You are Translator")
elif x==3:
    print("Вы выбрали Art - Искусство,сделайте свой выбор дальше в какую "
          "отрасль хотите пойти \n 1 - Drawing\n 2 - Singing:\n ")
    y=int(input("сделайте свой выбор: "))
    if y==1:
        print("You are Painter or Architect")
    elif y==2:
        print("You are Singer or Tamada")
elif x==4:
    print("Вы выбрали Sport , сделайте свой выбор дальше в какую "
          "отрасль хотите пойти"
          " \n 1 - Team\n 2 - Individual:\n ")
    y=int(input("сделайте свой выбор: "))
    if y==1:
        print("You are footballer or Basketball player")
    elif y==2:
        print("You are boxer or tennis player")




