class Persona:
    def hablar(self):
        pass
class Padre(Persona):
    apellido=''
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self):
        return self.nombre+" "+self.apellido
    def hablar(self):
        print("hola soy",self.nombre,self.apellido)

class Hijo(Padre):
    def __init__(self,nombre,lenguajesDeProgramacion):
        super().__init__(nombre)
        self.lenguajesDeProgramacion=lenguajesDeProgramacion
    def hablar(self):
        print("hola soy",self.nombre,self.apellido,"y me gusta",self.lenguajesDeProgramacion)

class Hija(Padre):
    def __init__(self,nombre,artistaMusical):
        super().__init__(nombre)
        self.artistaMusical=artistaMusical
    def hablar(self):
        print("hola soy",self.nombre,self.apellido,"y me gusta",self.artistaMusical)

padre = Padre('nombre del padre')
Padre.apellido='apellido del padre'
hijo = Hijo('nombre del hijo','python')
hijo.hablar()
hija = Hija('nombre del hija','nombre de banda')
hija.hablar()