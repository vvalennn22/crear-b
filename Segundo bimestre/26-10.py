# Programa para calcular el área de un círculo a partir de su diámetro

# Pide al usuario que ingrese el diámetro del círculo en centimetros
diametro = float(input("Ingrese el diámetro del círculo: "))

# Calcula el radio (la mitad del diámetro)
radio = diametro / 2

# Calcula el área con la fórmula: área = π * r²
pi = 3.1416
area = pi * (radio ** 2)

# Muestra el resultado
print("El área del círculo es:", area)