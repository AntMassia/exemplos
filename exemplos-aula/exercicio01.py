def menu():
    print(" 1 - Inserir Média ")
    print(" 2 - Mostrar Média ")
    print(" 3 - Sair ")
    opc = int(input("Escolha uma Opção: "))
    return opc 

def lerNotas(numero1,numero2):
    numero1 = float(input("Digite uma Nota: "))
    numero2 = float(input("Digite Outra Nota: "))
    return numero1,numero2

def cadastroVetor():
    media = (numero1 + numero 2) / 2
    medias.append(media)
    return medias
    
def mostrarMedias(medias):
    print("Médias:", medias)

def main():
    opc = 0
    medias = []
    numero1 = numero2 = 0
    
    while opc !=3:
        opc = menu()
        if opc == 1:
            numero1,numero2 = lerNotas(numero1,numero2)
        
        elif opc == 2:
            mostrarMedias(medias)
        
main()
    
