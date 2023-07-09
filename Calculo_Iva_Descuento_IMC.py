'''
Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
   1. Calcular_Iva
   2. Descuento (30% sobre la Total compra)
   3. Calcular_Imc (Leer peso y altura)

Las cuales deben ser desarrolladas en funciones (métodos).

Además se debe mostrar el estado de la persona de acuerdo a la siguiente tabla:

  < 18.5       Bajo Peso
  18.5 - 24.9  Adecuado
  25.0 - 29.9  Sobrepeso
  30.0 - 34.9  Obesidad grado 1
  35.0 - 39.9  Obesidad grado 2
  > 40         Obesidad grado 3
'''

#Función calcular el IVA
def calcular_iva(totalCompra):
    resultado=totalCompra*0.19;
    print(f"El IVA de la compra es: {resultado}");

def descuento_compra(totalCompra):
    descuento=totalCompra*0.3;
    resultado=totalCompra-descuento;
    print("--------Boleta---------\n");
    print(f"Total-----------------{totalCompra}");
    print(f"Descuento-------------{descuento}");
    print(f"TOTAL dscto.----------{resultado}");

def calcular_imc(peso,altura):
    resultado=round((peso/(altura**2)),1);
    return resultado;

def estado_imc(imc):
    if imc<18.5:
        print("ESTADO: Bajo peso");
    elif imc>=18.5 and imc<24.9:
        print("ESTADO: Adecuado");
    elif imc>=25. and imc<29.9:
        print("ESTADO: Sobrepeso");
    elif imc>=30.0 and imc<24.9:
        print("ESTADO: Abesidad grado 1");
    elif imc>=35.0 and imc<9.9:
        print("ESTADO: Obesidad grado 2");
    elif imc>40.0:
        print("ESTADO: Obesidad grado 3");


def menu():
    print("------Menu------");
    print("1.- Calcular IVA")
    print("2.- Calcular decuento")
    print("3.- Calcular IMC")


while True:
    menu();
    opcion=int(input("Ingrese una opción: "));
    if opcion==1:
        totalCompra=int(input("Ingrese su compra: "));
        calcular_iva(totalCompra);
    elif opcion==2:
        totalCompra=int(input("Ingrese su compra: "));
        descuento_compra(totalCompra);
    elif opcion==3:
        peso1=int(input("Ingrese su peso: "));
        altura1=float(input("Ingrese su altura: "));
        imc=calcular_imc(peso1,altura1);
        print(f"El IMC es de: {imc}");
        estado_imc(imc);




