def Q2A (matriz):
    detA = matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]
    if(detA == 0):
        retorno = None
    else:
        retorno = [0]*2
        retorno[1] = [0]*2
        retorno[0] = [0]*2
        retorno[0][0] = matriz[1][1]/detA
        retorno[1][1] = matriz[0][0]/detA
        retorno[1][0] = matriz[1][0]*(-1)/detA
        retorno[0][1] = matriz[0][1]*(-1)/detA
    return retorno
def main():
    matriz = [0]*2
    matriz[1] = [0]*2
    matriz[0] = [0]*2
    matriz[0][0] = float(input("a: "))
    matriz[0][1] = float(input("b: "))
    matriz[1][0] = float(input("c: "))
    matriz[1][1] = float(input("d: "))
    print(str(matriz[0][0]) + "\t" + str(matriz[0][1]) + "\n" + str(matriz[1][0]) + "\t" + str(matriz[1][1]))
    nova = Q2A(matriz)
    print()
    if(nova == None):
        print("None")
    else:
        print(str(nova[0][0]) + "\t" + str(nova[0][1]) + "\n" + str(nova[1][0]) + "\t" + str(nova[1][1]))

main()


    
