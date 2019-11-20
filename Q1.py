def Q1A (data):
    retorno = {"Ano": int(data[0] + data[1] + data[2] + data[3]), "Mes": int(data[5] + data[6]), "Dia": int(data[8] + data[9])}
    return (retorno)
def Q1B (ativo):
    if(len(ativo) == 4):
        ativo = ativo[0] + ativo[1] + ativo[2]
    retorno = (ativo == "SIM")
    return retorno
def Q1C (String):
    retorno = list(String.split(":"))
    return retorno
def Q1D (descritor):
    descritor.seek(0)
    linhas = list(descritor.readlines())
    return (linhas)
def main():
    arquivo = open("cadastro.txt", "r")
    linhas = Q1D(arquivo)
    arquivo.close()
    Info = {
        "CPF":"",
        "NOME":"",
        "DATA_DE_NASCIMENTO":"",
        "DATA_DO_CADASTRO":"",
        "ATIVO":True
        }
    Dic_list = [" "]*len(linhas)
    for i in range (len(linhas)):
        dados = Q1C(linhas[i])
        cadastro = Info.copy()
        cadastro["CPF"] = dados[0]
        cadastro["NOME"] = dados[1]
        cadastro["DATA_DE_NASCIMENTO"] = Q1A(dados[2])
        cadastro["DATA_DO_CADASTRO"] = Q1A(dados[3])
        cadastro["ATIVO"] = Q1B(dados[4])
        Dic_list[i] = cadastro
        
    print(Dic_list)

main()
