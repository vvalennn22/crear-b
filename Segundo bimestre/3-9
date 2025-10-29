import csv
import json
class Persona:
    def __init__(self,name,age,isStudent):
        self.name=name
        self.age=age
        self.isStudent=isStudent
    def __str__(self):
        return "nombre: "+self.name + ",edad: " + self.age + ",es estudiante: " + self.isStudent
personas = []

with open('data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        persona = Persona(row[0],row[1],row[2])
        personas.append(persona)
personas.pop(0)
for persona in personas:
    print(persona.__str__())
'''
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false
}

name,age,isStudent
John Doe,30,false
'''