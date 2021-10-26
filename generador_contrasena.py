import random


def generar_contraseña():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minsuculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    caracteres = mayusculas+minsuculas+simbolos+numeros

    contraseña = []

    for i in range(15):
        caracter_ramdom = random.choice(caracteres) # choice sirve para elegir un caracter al azar de toda la lista de caracteres
        contraseña.append(caracter_ramdom)
    contraseña = "".join(contraseña)# se generara un string de la lista original, es decir tener todos los caracteres en una sola cadena de texto
    return contraseña
def run():
    contraseña=generar_contraseña()
    print("Tu nueva contraseña es: " + contraseña)






if __name__ == "__main__":
    run()
