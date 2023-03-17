cantidadNum=int(input("ingrese la cantidad de numeros: "))

cantmul2=0
cantmul3=0

for i in range(cantidadNum):
    numero=int(input("Digite el numero: "))
    if (numero%2==0):
        cantmul2+=1
    if(numero%3==0):
        cantmul3+=1
        
print(f'los multiplos de 2 son {cantmul2} ' )
print(f'los multiplos de 3 son {cantmul3}')