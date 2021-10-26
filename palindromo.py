# def palindromo(palabra):
#     palabra= palabra.replace(' ', '')
#     palabra=palabra.lower()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False


# def run():
#     palabra = input("Escribe una palabra: ")
#     es_palindromo= palindromo(palabra)

#     if es_palindromo==True:
#         print ("Es palindromo")
#     else:
#         print("No es palindromo")    


# if __name__=="__main__":
#     run() 

def run(num, rept):
    if num <= rept:
        cont = num
        print(str(2 ** cont) )
        run(num+1, rept)
    else:
        print("Fin!")

if __name__ == "__main__":
    repeticiones = int(input("Cuantas potencias: "))
    run(0, repeticiones)