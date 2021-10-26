
def run():
  #LIM=1000000

 # potencia=1000000

  # while potencia<LIM:
  #     print("Potencia:" + str(potencia)) #Se le agrega str para que pueda imprimir un dato numerico en una cadena de texto, si no, habra error
  #     cont=cont+1
  #     potencia=2**cont

  i = 1
  while i <= 50:
      
      if i ==13:
        continue
      print(i)
      i = 3 * i + 1
  print("Programa terminado")


if __name__ == "__main__":
    
    run()