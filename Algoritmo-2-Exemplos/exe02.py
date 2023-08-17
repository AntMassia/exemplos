def multiplica(matriz):
    result = 1

    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            if line == column:
                result = result * matriz[line][column]

    return result

def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    result = multiplica(matriz)
    print("Resultado: ", result)

main()
