import xlrd
import matplotlib.pyplot as plt

def retornarDict(file):
    newFile = xlrd.open_workbook(f'./{file}.xlsx')
    newFile_sh = newFile.sheet_by_index(0)
    namesRow = []
    dictRow = []

    for column in range(newFile_sh.ncols):
        namesRow.append(str(newFile_sh.row(0)[column]).replace("text:", "").replace("'", ""))
        dictRow.append([])
        for line in range(newFile_sh.nrows):
            if line != 0:
                if 'text' in str(newFile_sh.row(line)[column]):
                    dictRow[column].append(str(newFile_sh.row(line)[column]).replace("text:", "").replace("'", ""))
                else:
                    
                    dictRow[column].append(str(newFile_sh.row(line)[column]).replace("number:", "").replace(".0", ""))

    newDict = dict(zip(namesRow, dictRow))
    return newDict, namesRow

def contRepetidos(var):
    cont = 0
    unico = 0
    for i in var:
        if var.count(i) != 1:
            cont += 1
        else:
            unico += 1
    contVazios = var.count("empty:''")
    contDuplicados = cont - contVazios

    return [ unico, contDuplicados, contVazios ]

def gerarGrafico(file,fileDict):

    nomenclaturas = ['Unicos','Duplicados','Vazios']
    
    valoresBrutos = []
    
    matrizDeValores = []

    soma100porCento = 0

    valores = []
    
    for i in fileDict[1]:
        valoresBrutos.append(contRepetidos(fileDict[0][i]))

    for i in range(len(valoresBrutos)):
        soma = 0
        for j in valoresBrutos[i]:
            soma += j
        
        for z in range(0,3):
            valores.append([])
            valores[z].append(int(valoresBrutos[i][z] * 100 / soma))
        
    valores100porCento = [valores[0] + valores[1] + valores[2]]

    for valor in valores100porCento:
        for j in valor:
            soma100porCento += j

    for y in range(0,3):
        soma = 0
        matrizDeValores.append([])

        for z in valores[y]:
            soma += z

        matrizDeValores[y].append(int(soma * 100 / soma100porCento))

    labels = (nomenclaturas)
    sizes = [matrizDeValores[0],matrizDeValores[1],matrizDeValores[2]]

    fig1,ax1 = plt.subplots()
    ax1.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
    ax1.axis('equal')
    ax1.set_title(f'Tabela {file}')
    plt.show()


def verificarNullById (var,id):
    verified = []
    cont = []
    for i in range(len(var)):
        if var[i] == "empty:''":
            verified.append(var[i].replace("empty:''", "Id:")+id[i])
        else:
            if var.count(var[i]) != 1:
                cont.append(f'Id:{id[i]}  Item:{var[i]}')
            pass
    return verified,cont

def chamarNullID(file,funcDict):
    newDict = funcDict[0] 
    newNomes = funcDict[1]

    for i in newNomes:
        print(f'\nIdentificador {i}\nVazios:')
        print(verificarNullById(newDict[i],newDict[newNomes[0]])[0])
        print('Repetidos')
        print(verificarNullById(newDict[i], newDict[newNomes[0]])[1])


def chamarRelatorio(file,funcDict):
    print(f'\n\nTabela"{file}"\n')
    for i in funcDict[1]:
        print(f'\n{i}')
        valores = contRepetidos(funcDict[0][i])
        print(f'({valores[0]}) Campos com valores unicos\n({valores[1]}) Duplicados\n({valores[2]}) Campos vazios')


def main():
    file = ['STG_MVT_CRD','STG_FNT_ITT','STG_MDL','STG_OPR_ITT','STG_PGT']
    print("=-"*24)
    print("(1)Fazer Relatorio\n(2)Visualizar IDs nulos e repetidos\n(3)Visualizar Grafico")
    print('=-'*24)
    escolha = int(input("Escolha:"))
    if escolha == 1:
        for i in file:
            chamarRelatorio(i,retornarDict(i))

    elif escolha == 2:
        for i in file:
            chamarNullID(i,retornarDict(i))
            
    else:
        for i in file:
            gerarGrafico(i,retornarDict(i))

if __name__ == "__main__":
    main()