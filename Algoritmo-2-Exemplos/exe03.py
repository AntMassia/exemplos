def scale(matriz, scale_number):
    result = []

    for line in range(len(matriz)):
        temp_list = []
        for column in range(len(matriz[line])):
            temp_list.append(matriz[line][column] * scale_number)

        result.append(temp_list )
    return result

def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    result = scale(matriz, 5)
    print("Result: ", result)

main()
