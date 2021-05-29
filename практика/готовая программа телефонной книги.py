contacts = [
{
"name": "John",
"phone": "123456"
},
{
"name": "Jane",
"phone": "564321"
},
{
"name": "Bob",
"phone": "+1234"
},
]
def list(*args):
    print("name", " phone")
    for contact in contacts:
        print(f"{contact['name']}  {contact['phone']}")
def find(name):
    for contact in contacts:
        if name==contact['name']:
            return print("Имя",contact['name'],"найдено,","его номер телефона",contact['phone'])
        else:
            print("Такого имени в телефонной книге нет")
            break

def add(new_name,new_phone):
    for contact in contacts:
        if contact['name'] != new_name and contact['phone'] != new_phone:
            contact = {'name': new_name, 'phone': new_phone}
            contacts.append(contact)
            break
        elif contact['name'] == new_name and contact['phone'] == new_phone:
            print("такой контакт уже существует ")
            break
def edit(old_name,new_name,new_phone):
    for contact in contacts:
        if contact['name']==old_name:
            contact['name']=new_name
            contact['phone']=new_phone
        if contact['name']!=old_name:
            print("Такого контакта не существует ")
    return old_name,new_name,new_phone

def delete(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
    return f"удаленное имя {name}"
a = input(
    "Введите команду\nlist - вывести контакты\nfind - найти контак\nadd - добавить контакт\nedit - изменить контакт"
    "\ndelete - удалить контак\nexit - выход \n")
while a!='exit':
    if a=='list':
        list()
        a = input(
            "Введите команду\nlist - вывести контакты\nfind - найти контак\nadd - добавить контакт\nedit - изменить контакт"
            "\ndelete - удалить контак\nexit - выход \n")
    elif a=='find':
        print(find(input("Введите имя которое хотите найти\n")))
        a = input(
            "Введите команду\nlist - вывести контакты\nfind - найти контак\nadd - добавить контакт\nedit - изменить контакт"
            "\ndelete - удалить контак\nexit - выход \n")
    elif a=='add':
        add(input("Введите имя нового контакта "), input("Введите номер нового контакта  "))
        a = input(
            "Введите команду\nlist - вывести контакты\nfind - найти контак\nadd - добавить контакт\nedit - изменить контакт"
            "\ndelete - удалить контак\nexit - выход \n")
    elif a=='edit':
        print(edit(input("Имя которое хотите поменять"),input("имя на которое хотите поменять"), input("новый номер телефона")))
        a = input(
            "Введите команду\nlist - вывести контакты\nfind - найти контак\nadd - добавить контакт\nedit - изменить контакт"
            "\ndelete - удалить контак\nexit - выход \n")
    elif a=='delete':
        b=input("Вы уверены что хотите удалить контакт из списка?")
        if b=='Yes':
            print(delete(input("Имя которое хотите удалить ")))
            list()
        elif b=="No":
            list()
        a = input(
            "Введите команду\nlist - вывести контакты\nfind - найти контак\nadd - добавить контакт\nedit - изменить контакт"
            "\ndelete - удалить контак\nexit - выход \n")
    elif a=='exit':
        print("Работа с приложением завершена ")
        break

