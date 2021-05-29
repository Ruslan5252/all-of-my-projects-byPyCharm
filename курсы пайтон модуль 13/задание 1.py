import json
import os

employee = [

    {"id": 1, "name": "Emily", "age": 35, "salary": 500000},

    {"id": 2, "name": "Jack", "age": 46, "salary": 450000},

    {"id": 3, "name": "Tom", "age": 29, "salary": 350000},

    {"id": 4, "name": "Fin", "age": 31, "salary": 400000},

    {"id": 5, "name": "Amanda", "age": 24, "salary": 250000},

    {"id": 6, "name": "Kate", "age": 30, "salary": 340000}
]

file = open("emloyee.json", "w")
result = json.dump(employee, file)
file.close()
file=open("emloyee.json",'r')
file=json.load(file)
for i in file:
    if i['salary'] > 350000:
        print(i['salary'])

