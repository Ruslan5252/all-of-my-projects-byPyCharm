def spisok(*args):
    s1=input("Введите список из строк ")
    s2=input("строка для определения ")
    if s2 in s1:
        return "Yes"
    else:
        return "No"
print(spisok())