# consigna: Crea una función dentro de una clase que reciba dos números y devuelva el mayor. Escribe el código y un ejemplo de uso mostrando el resultado por pantalla
# calcular masa atomica de la molecula de dioxido de carbono

# Clase que representa un átomo con nombre, masa y cantidad
class Atomo:
    def __init__(self,nombre,masa,cantidad=1):
        self.masa = masa           # Masa atómica
        self.nombre = nombre       # Nombre del átomo
        self.cantidad=cantidad     # Cantidad disponible o requerida

# Clase que representa una molécula formada por átomos
class Molecula:
    def __init__(self,nombre,atomos):
        self.nombre = nombre       # Nombre de la molécula
        self.atomos = atomos       # Lista de átomos que la componen
    def calcularMasaMolecular(self):
        masa = 0
        for atomo in self.atomos:  # Suma la masa de cada átomo por su cantidad
            masa += (atomo.masa * atomo.cantidad)
        return masa                # Devuelve la masa molecular total


# Función que determina el reactivo limitante para formar una molécula
# Recibe la molécula (con cantidades requeridas) y los átomos disponibles
def reactivo_limitante(molecula, atomos_disponibles):
    """
    molecula: objeto Molecula con atomos requeridos y cantidades
    atomos_disponibles: lista de objetos Atomo con cantidades disponibles
    Devuelve el nombre del reactivo limitante o 'ninguno (proporción exacta)'
    """
    min_producciones = float('inf')   # Inicializa el mínimo de producciones posibles
    limitante = None                  # Guardará el nombre del reactivo limitante
    for atomo_necesario in molecula.atomos:
        # Busca el átomo disponible correspondiente
        disponible = next((a for a in atomos_disponibles if a.nombre == atomo_necesario.nombre), None)
        if not disponible:
            return atomo_necesario.nombre  # Si no hay, es el limitante
        # Calcula cuántas veces se puede formar la molécula con ese átomo
        producciones = disponible.cantidad // atomo_necesario.cantidad
        if producciones < min_producciones:
            min_producciones = producciones
            limitante = atomo_necesario.nombre
    # Si todos permiten la misma cantidad, no hay limitante
    # Calcula cuántas veces se puede formar la molécula con cada átomo disponible
    cantidades = []
    for atomo_necesario in molecula.atomos:
        for disponible in atomos_disponibles:
            if disponible.nombre == atomo_necesario.nombre:
                cantidad = disponible.cantidad // atomo_necesario.cantidad
                cantidades.append(cantidad)
    # Si todos permiten la misma cantidad, no hay limitante
    if len(set(cantidades)) == 1:
        return "ninguno (proporción exacta)"
    return limitante

# Crea átomos y molécula de dióxido de carbono para calcular su masa molecular
oxigeno = Atomo("oxigeno", 15.99, 2)           # 2 átomos de oxígeno
carbono = Atomo("carbono",  12.01)             # 1 átomo de carbono
dioxidoDeCarbono = Molecula("dioxido de carbono",[oxigeno,carbono]) # CO2
print(dioxidoDeCarbono.calcularMasaMolecular()) # Imprime la masa molecular de CO2



# Ejemplo general para agua
hidrogeno = Atomo("hidrogeno", 2.02, 6)  # 6 moléculas de H2 disponibles
oxigeno = Atomo("oxigeno", 15.99, 3)     # 3 moléculas de O2 disponibles
agua = Molecula("agua", [Atomo("hidrogeno", 2.02, 2), Atomo("oxigeno", 15.99, 1)]) # H2O requiere 2 H y 1 O
limitante = reactivo_limitante(agua, [hidrogeno, oxigeno]) # Calcula el reactivo limitante para agua
print(f"El reactivo limitante para agua es: {limitante}")   # Muestra el resultado


# Ejemplo para dióxido de carbono (CO2): requiere 1 C y 2 O
carbono_disp = Atomo("carbono", 12.01, 2)   # 2 átomos de C disponibles
oxigeno_disp = Atomo("oxigeno", 15.99, 3)   # 3 átomos de O disponibles
co2 = Molecula("dioxido de carbono", [Atomo("carbono", 12.01, 1), Atomo("oxigeno", 15.99, 2)]) # CO2 requiere 1 C y 2 O
limitante_co2 = reactivo_limitante(co2, [carbono_disp, oxigeno_disp]) # Calcula el reactivo limitante para CO2
print(f"El reactivo limitante para CO2 es: {limitante_co2}")         # Muestra el resultado