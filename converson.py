
def conversion (tipo_pesos, valor_dolar):

 
    pesos = input("¿Pesos " + tipo_pesos+ "?")
    pesos = float(pesos)
    dolar=3875
    dolares=pesos/valor_dolar
    dolares=round(dolares, 2)
    dolares=str(dolares)
    print ("Tienes $" + dolares + " Dolares")


menu = """

Bienvenido al conversor de monedas 🤑

    1. Pesos colombianos
    2. Pesos argentinos
    3. Pesos mexicanos
    4. Pesos colombianos a dolares


Elige una opcion:"""

opcion = int(input(menu))

if opcion ==1:
  
    conversion("Colombianos", 3875)
elif opcion ==2: 
    conversion("Mexicanos", 65)

elif opcion ==3:
    conversion("argentinos",24)

elif opcion ==4:
    dolares = input("¿Cuántos dolares tienes? ")
    dolares = float(dolares)
    valor_pesos = 3875
    pesos = dolares *valor_pesos 
    pesos = round(pesos, 2)
    pesos = str(pesos)

    print("Tienes $" + pesos + "pesos")
else:
    print ("Digite un valor aceptado")











