R1 = {
    "bottomLeft" : 0.0 , 0.0,
    "topRight" : 0.0 , 0.0
    }
R2 = {
    "bottomLeft" : 0.0 , 0.0,
    "topRight" : 0.0 , 0.0
    }

def isCollisionDetected()
    if(((R1["topRight"[0]] > R2 ["topRight"[0]] > R1["bottonLeft"[0]]) or
        (R1["topRight"[0]] < R2 ["topRight"[0]] < R1["bottonLeft"[0]]) or
        (R1["topRight"[0]] > R2 ["bottonLeft"[0]] > R1["bottonLeft"[0]]) or
        (R1["topRight"[0]] < R2 ["bottonLeft"[0]] < R1["bottonLeft"[0]])) and
       ((R1["topRight"[1]] > R2 ["topRight"[1]] > R1["bottonLeft"[1]]) or
        (R1["topRight"[1]] < R2 ["topRight"[1]] < R1["bottonLeft"[1]]) or
        (R1["topRight"[1]] > R2 ["bottonLeft"[1]] > R1["bottonLeft"[1]]) or
        (R1["topRight"[1]] < R2 ["bottonLeft"[1]] < R1["bottonLeft"[1]])))
        retorno = True
    else
        retorno = False
    return retorno
def main()
    R1["bottonLeft"[0]] = float(input("Entre com o valor de BLx do 1° retângulo"))
    R1["bottonLeft"[1]] = float(input("Entre com o valor de BLy do 1° retângulo"))
    R1["topRight"[0]] = float(input("Entre com o valor de TRx do 1° retângulo"))
    R1["topRight"[1]] = float(input("Entre com o valor de TRy do 1° retângulo"))
    R2["bottonLeft"[0]] = float(input("Entre com o valor de BLx do 2° retângulo"))
    R2["bottonLeft"[1]] = float(input("Entre com o valor de BLy do 2° retângulo"))
    R2["topRight"[0]] = float(input("Entre com o valor de TRx do 2° retângulo"))
    R2["topRight"[1]] = float(input("Entre com o valor de TRy do 2° retângulo"))
    if(isCollisionDetected)
        print("Colisão detectada")
    else
        print("Colisão não detectada")

main()
