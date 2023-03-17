frutas = []


for i in range(2):
    fruta = {}
    fruta['nombre'] = input('Digite el nombre de la fruta: ')
    fruta['color'] = input('Digite el color de la fruta: ')
    fruta['precio'] = input('Digite el precio de la fruta: ')

    frutas.append(fruta)

    print(frutas)
    
    print(frutas[::-1])
