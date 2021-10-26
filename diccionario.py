def run ():
    mi_diccionario ={

        "llave1": 1,
        "llave2": 2,
        "llave3": 3,

    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises={

        "Argentina": 44938712,
        "Brazil": 21014725,
        "Colombia": 50372424,

    }

    # print(poblacion_paises["Argentina"])
    # print(poblacion_paises["Brazil"]) # IMPRIMIR EL NOMBRE DE LAS LLAVES
    # print(poblacion_paises["Colombia"])

    # for pais in poblacion_paises.keys(): #MOSTRAR LOS VALORES DE LAS LLAVES
    #     print(pais)

    # for pais in poblacion_paises.values(): #MOSTRAR LOS VALORES DE LOS VALORES
    #     print(pais)

    for pais, poblacion in poblacion_paises.items(): #MOSTRAR LOS VALORES TANTO DE LAS LLAVES COMO DE LOS VALORES
        print(pais + " tiene " + str(poblacion) + " habitantes")



if __name__== "__main__":
    run()