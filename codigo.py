import numpy as np

tipo = [] #Tipo, patente, marca y precio, multas (monto yfecha), fecha de registro del vehículo y nombre del dueño
patente= []
marca= []
precio = []
multa= []
fecharegistrovehiculo= []
nombredueño= []

bd=[[tipo],[patente],[marca,],[precio],[multa],[fecharegistrovehiculo],[nombredueño]]   

n=0
def grabar():
    gtipo=input('Ingresa tipo de auto')
    bd.append(gtipo)

    apatente=input('ingresa PATENTE')
    gpatente=apatente.upper()
    print(gpatente)
    patente.append(gpatente)
    
    gmarca=input('Ingresa la MARCA del auto')
    marca.append(gmarca)

    gprecio=int(input('Ingresa precio del auto'))
    precio.append(gprecio)

    gmulta=int(input('ingresa Multa(s) '))
    multa.append(gmulta)

    gfecharegistrovehiculo=int(input('Ingresa vecha de registro del vehiculo '))
    fecharegistrovehiculo.append(gfecharegistrovehiculo)

    gnombredueño=input('Ingresa nombre')
    nombredueño.append(gnombredueño)

    for listas in bd:
        print(listas)
       # for elemento in listas:
            #print(elemento)
def mostrar_patente():
    print()
while True:               
    print('Menu de Auto Seguro')
    print('1.-Grabar')
    print('2.-Buscar')
    print('3.-Imprimir certificados')
    print('4.-Salir')
    op=int(input('Selecciona una opcion del menu'))
    if op==1:
        print('GRABAR DATOS')
        grabar()
        

    elif op==2:
        buscar_patente=input('ingresa patente a buscar')
        
        
    elif op==3:
        print()
        
    elif op==4:
        break





    




aleatorio= np.random.randint(1,100,size=(2,2),)





#4letras y 2 digitos PARA PATENTE
