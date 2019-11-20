Data = {
    "Ano" : 1111
    "Mes" : 11
    "Dia" : 11
    }
def Q1A (data)
    Data["Ano"] = Toint(data[0] + data[1] + data[2] + data[3])
    Data["Mes"] = Toint(data[5] + data[6])
    Data["Dia"] = Toint(data[8] + data[8])
    retorno = Data
    return (retorno)
def Q1B (Ativo)
    if(len(ativo) == 4)
        ativo.pop()
        ativo.pop()
    retorno = (ativo == "SIM")
    return retorno
def Q1C (String)
    retorno = list(String.split(":"))
    return retorno
def Q1D (descritor)
    descritor.seek(0)
    lista = list(descritor.readlines())
    return (lista)
def main()
    arquivo = open("cadastro.txt", "r")
    lista = Q1D(arquivo)
    for i in range (len(lista))
        lista_cad = Q1C(lista[i])

main()
