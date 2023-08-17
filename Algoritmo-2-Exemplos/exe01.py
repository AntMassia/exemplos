matriz = [[1,2,3], [4,5,6], [7,8,9]] 

for line in range(len(matriz)):
    print(line, "==>", matriz [line])
    for colunm in range(len(matriz[line])):
        print(f"matriz[{line}][{colunm}] ==>", matriz [line][colunm])


