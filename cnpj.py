import xlrd

#Função para abrir todas as tabelas e montar um dicionário
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


#Verificação de CNPJs válidos
novo_dict_fnt = retornarDict("STG_FNT_ITT")[0]
cnpjCorreto = []
complementoInvalido = []
cnpjInvalido = []
contCorreto = 0
contComplementoInvalido = 0
contInvalido = 0

for cnpj1 in range(len(novo_dict_fnt["NUM_CNPJ"])):
    if len(novo_dict_fnt["NUM_CNPJ"][cnpj1]) == 8:
        contCorreto += 1
        if len(novo_dict_fnt["NUM_CMP_CNPJ"][cnpj1]) <= 6:
            cnpjCorreto.append(f'ID: {novo_dict_fnt["ID_STG_FNT_ITT"][cnpj1]} {novo_dict_fnt["NUM_CNPJ"][cnpj1][:2]}.{novo_dict_fnt["NUM_CNPJ"][cnpj1][2:5]}'
                               f'.{novo_dict_fnt["NUM_CNPJ"][cnpj1][5:]}/{"0" * (6 -len(novo_dict_fnt["NUM_CMP_CNPJ"][cnpj1])) + novo_dict_fnt["NUM_CMP_CNPJ"][cnpj1][:-2]}-'
                               f'{novo_dict_fnt["NUM_CMP_CNPJ"][cnpj1][-2:]}')
        else:
            complementoInvalido.append(f'ID: {novo_dict_fnt["ID_STG_FNT_ITT"][cnpj1]} {novo_dict_fnt["NUM_CNPJ"][cnpj1]} {novo_dict_fnt["NUM_CMP_CNPJ"][cnpj1]}')
            contComplementoInvalido += 1
    else:
        cnpjInvalido.append(f'ID: {novo_dict_fnt["ID_STG_FNT_ITT"][cnpj1]} {novo_dict_fnt["NUM_CNPJ"][cnpj1]} {novo_dict_fnt["NUM_CMP_CNPJ"][cnpj1]}')
        contInvalido += 1

if len(cnpjCorreto) != 0:
    print(f'CNPJs Corretos:\n{cnpjCorreto}\n'
          f'Quantidade de CNPJs corretos {contCorreto}\n')

if len(complementoInvalido) != 0:
    print(f'CNPJs corretos com complementos errados (mais de 6 Dígitos) \n{complementoInvalido}\n'
          f'Quantidade de CNPJs com complementos inválidos {contComplementoInvalido}\n')

if len(cnpjInvalido) != 0:
    print(f'CNPJs inválidos (com mais ou menos de 8 dígitos) \n{cnpjInvalido}\n'
          f'Quantidade de CNPJs inválidos: {contInvalido}\n')


ultimaAtualizacao = sorted(novo_dict_fnt["DAT_INC_DBO"])
print(f'Data da ultima atualização {ultimaAtualizacao[-1][0:11]}')