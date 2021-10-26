
# def imprimir_mensaje(): # COMO DECLARAR UNA FUNCIÓN
#     print ("Mensaje Especial")
#     print("Aprendo a usar funciones")


# imprimir_mensaje()#SE LLAMA A LA FUNCIÓN PARA QUE IMPRIMA UNA VEZ EL MENSAJE 

def conversacion (mesanje):
    print("Hola, "+ mesanje +", adios")

opcion = int(input("Escoja un numero: 1 / 2 / 3 :"))

if opcion ==1:
    conversacion(" Opcion 1 SAPO PERRO")

elif opcion ==2:
    conversacion (" Opcion 2 BB")

elif opcion ==3:
    conversacion("opcion 3 WUAPO" )        

else:
    conversacion ("Escriba la opcion correcta")