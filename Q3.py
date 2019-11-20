R1 = {
    "bottomLeft" : [0.0, 0.0],
    "topRight" : [0.0, 0.0]
    }
R2 = {
    "bottomLeft" : [0.0, 0.0],
    "topRight" : [0.0, 0.0]
    }

def isCollisionDetected():
    R1Tx = R1["topRight"][0]
    R1Ty = R1["topRight"][1]
    R1Bx = R1["bottomLeft"][0]
    R1By = R1["bottomLeft"][1]
    R2Tx = R2["topRight"][0]
    R2Ty = R2["topRight"][1]
    R2Bx = R2["bottomLeft"][0]
    R2By = R2["bottomLeft"][1]
    if(R1Bx < R2Tx and R1Tx > R2Bx and R1By < R2Ty and R1Ty > R2By):
        retorno = True
    else:
        retorno = False
    return retorno
def main():
    R1["bottomLeft"][0] = float(input("Entre com o valor de BLx do 1° retângulo: "))
    R1["bottomLeft"][1] = float(input("Entre com o valor de BLy do 1° retângulo: "))
    R1["topRight"][0] = float(input("Entre com o valor de TRx do 1° retângulo: "))
    R1["topRight"][1] = float(input("Entre com o valor de TRy do 1° retângulo: "))
    R2["bottomLeft"][0] = float(input("Entre com o valor de BLx do 2° retângulo: "))
    R2["bottomLeft"][1] = float(input("Entre com o valor de BLy do 2° retângulo: "))
    R2["topRight"][0] = float(input("Entre com o valor de TRx do 2° retângulo: "))
    R2["topRight"][1] = float(input("Entre com o valor de TRy do 2° retângulo: "))
    if(isCollisionDetected()):
        print("Colisão detectada")
    else:
        print("Colisão não detectada")

main()
