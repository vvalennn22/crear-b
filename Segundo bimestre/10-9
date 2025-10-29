from enum import Enum

class Rareza(Enum):
    COMUN = 1
    ESPECIAL = 2
    EPICA = 3
    LEGENDARIA = 4

class TipoCarta(Enum):
    TROPAS = 1
    ESTRUCTURAS = 2
    HECHIZOS = 3

class Carta:
    def __init__(self, nombre, daño, vida, alcance,velocidadDeAtaque, unidades,objetivo, velocidad, dañoATorres,tipo, rareza, elixir, nivel, experiencia):
        self.nombre = nombre
        self.daño = daño
        self.vida = vida
        self.alcance = alcance
        self.velocidadDeAtaque = velocidadDeAtaque
        self.unidades = unidades
        self.objetivo = objetivo
        self.velocidad = velocidad
        self.dañoATorres = dañoATorres
        self.tipo = tipo
        self.rareza = rareza
        self.elixir = elixir
        self.nivel = nivel
        self.experiencia = experiencia

class Mazo:
    maximoDeCartas = 8
    def __init__(self,nombre):
        self.cartas = []
        self.nombre=nombre
        self.victorias = 0
        self.derrotas = 0
    def ganar(self):
        self.victorias+=1
    def perder(self):
        self.derrotas+=1
    def agregarCarta(self,carta):
        if len(self.cartas)<self.maximoDeCartas:
            self.cartas.append(carta)
            return True
        return False
    def borrarCarta(self,nombreDeCarta):
        for contador,carta in self.cartas:
            if carta.nombre == nombreDeCarta:
                cartaEliminada = self.cartas.pop(contador)
                return cartaEliminada
        return None

    def elixirPromedio(self):
        if self.cartas:
            cantidad = len(self.cartas)
            sumaDeElixir = sum(carta.elixir for carta in self.cartas)
            promedio = sumaDeElixir / cantidad
            return promedio
        return 0
    def porcentajeDeVictorias(self):
        partidasJugadas = self.victorias + self.derrotas
        if partidasJugadas > 0:
            porcentaje = self.victorias / partidasJugadas * 100
            return porcentaje
        return 0

class Jugador:
    maximoDeMazos = 10
    def __init__(self, nombre,tag):
        self.nombre=nombre
        self.tag=tag
        self.mazos=[]
    def agregarMazo(self,mazo):
        if len(self.mazos)<self.maximoDeMazos:
            self.mazos.append(mazo)
            return True
        return False
    def borrarMazo(self,numeroDeMazo):
        if numeroDeMazo >= 0 and numeroDeMazo < len(self.mazos):
            mazo = self.mazos.pop(numeroDeMazo)
            return mazo
        return None