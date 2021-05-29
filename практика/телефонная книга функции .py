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


list()
def find(name):
    for contact in contacts:
        if contact['name']==name:
            print("Имя",contact['name'],"найдено,","его номер телефона",contact['phone'])
            break
        else:
            print("Такого имени в телефонной книге нет")
            break
find()

def add(new_name,new_phone):
    for contact in contacts:
        if contact['name'] != new_name and contact['phone'] != new_phone:
            contact = {'name': new_name, 'phone': new_phone}
            contacts.append(contact)
            break
        elif contact['name'] == new_name and contact['phone'] == new_phone:
            print("такой контакт уже существует ")
            break
    print(list())
def edit(old_name,new_name,new_phone):
    for contact in contacts:
        if contact['name']==old_name:
            contact['name']=new_name
            contact['phone']=new_phone
            break
        if contact['name']!=old_name:
            print("Такого контакта не существует ")
            break
    list()
edit()

def delete(*args):
    a = input("Введите имя контакта который вы хотите удалить из списка ")
    for contact in contacts:
        if contact['name'] == a:
            contact['name'] = ' '
            contact['phone'] = ' '
            break
        elif contact['name']!=a:
                print("Контакта с таким именем не существует ")
                break
        list()
delete()

