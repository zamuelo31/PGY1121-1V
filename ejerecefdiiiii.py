def calcularIVA(precio):
    precio = precio*0.19
    return precio

def descuento(precio,desc):
    precio = (precio - (precio*(desc/100)))
    print("El precio final con descuento ",desc,"% es: $",precio)

def calculoIMC(peso,estatura):
    imc = (peso/(estatura**2))
    if imc < 18.5 :
        print("Bajo Peso")
    else:
        if imc >= 18.5 and imc<= 24.9 :
            print("Peso adecuado")
        else:
            if imc >=25 and imc <= 29.9 :
                print("Sobrepeso")
            else:
                if imc >=30 and imc <= 34.9:
                    print("Obesidad grado 1")
                else:
                    if imc >=35 and imc <= 39.9:
                        print("Obesidad grado 2")
                    else:
                        if imc >= 40:
                            print("Obesidad grado 3")

op = 3

while op != 4:
    print("     MENU    ")
    print("*"*20)
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op = int(input("Seleccione su opción (1-4): "))
    if op == 1:
        precio = int(input("Ingrese precio del producto: "))
        iva  = calcularIVA(precio)
        print("El IVA de $",precio," es: $",iva)
    if op == 2:
        precio = int(input("Ingrese precio del producto: "))
        desc = int(input("Ingrese descuento (0-100)%: "))
        descuento(precio,desc)
    if op == 3:
        peso = int(input("Ingrese su peso en Kg: "))
        estatura = float(input("Ingrese su estatura en m: "))
        calculoIMC(peso,estatura)

print("fin del semestre")