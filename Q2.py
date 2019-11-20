def Q2A (matriz)
    detA = matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]
    if(detA == 0)
        retorno = "none"
    else
        retorno = list(matriz)
        retorno[0][0] = matriz[1][1]/detA
        retorno[1][1] = matriz[0][0]/detA
        retorno[1][0] = matriz[1][0]*(-1)/detA
        retorno[0][1] = matriz[0][1]*(-1)/detA
    return retorno
def main()
    matriz = [" "]*2
    matriz[1] = [" "]*2
    matriz[0] = [" "]*2
    matriz[0][0] = int(input("a"))
    matriz[0][1] = int(input("b"))
    matriz[1][0] = int(input("c"))
    matriz[1][1] = int(input("d"))
    nova = Q2A(matriz)
    print(matriz[0][0] + "\t" + matriz[0][1] + "\n" + matriz[1][0] + "\t" + matriz[1][1])
    print()
    print(nova[0][0] + "\t" + nova[0][1] + "\n" + nova[1][0] + "\t" + nova[1][1])

main()


    
