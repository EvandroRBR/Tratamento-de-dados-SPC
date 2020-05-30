import conv_dict
import return_csv

files=['STG_FNT_ITT','STG_MDL','STG_MVT_CRD','STG_OPR_ITT','STG_PGT',
'fatec_pessoa_fisica','fatec_endereco_pessoa_fisica','fatec_opr','fatec_pgt','fatec_mvt']

confidental_array = []
nivel_restrição = []

def sep_conf():

  tuple_dic = []

  for i in range(len(files)):
    try:
      tuple_dic.append(conv_dict.return_tuple(f'database/{files[i]}'))
    except:
      tuple_dic.append(return_csv.tuple_csv(f'{files[i]}'))

  for j in range(len(tuple_dic)):
    print(f'\nTabela {files[j]}:')
    for z in tuple_dic[j][1]:
      for valor in range(len(confidental_array)):
        if confidental_array[valor] in z:
          print(f'Metadado: {z} confidencial - Nivel: {nivel_restrição[valor]}')


def escolha():
  print('=-'*20 + '\n   INDICADOR CONFIDENCIALIDADE\n' + '=-'*20)
  escolha_inicial = int(input('\n1 - Verificar valores confidenciais\n2 - Configuração\nEscolha :'))
  if(escolha_inicial == 1):
    sep_conf()

    clear()    
    restart = input('\nDeseja continuar ? S/N\n ')
    if(str(restart).lower() == 's'):
      main()
    else:
      return
  else:
    print('\n' + ('=-'*20))
    else_escolha = int(input('\nCONFIGURAÇÂO:\n1 - Remover Metadado Confidencial'+
      '\n2 - Adicionar Metadado Confidencial\n3 - Listar Metadados Existentes\nEscolha: '))
    
    if(else_escolha == 1):
      metadado_para_remover = input("\nDigite o nome do metadado que deseja remover da analise: \nmetadado: ")
      try:
        delete(metadado_para_remover)

      except:
        print('Metadado não encontrado, por favor tente novamente')
        return
      
      restart = input('\nDeseja continuar ?\nS/N: ')
      if(str(restart).lower() == 's'):
        main()
      else:
        return

    elif(else_escolha == 2):
      metadado_para_adicionar = input("\nDigite o nome do metadado que deseja adicionar: \nmetadado: ")
      nivel_restrição_adicionar = input("Digite o nivel de restrição desse atributo: \nnivel: ")
      try:
        adicionar(metadado_para_adicionar,nivel_restrição_adicionar)

      except:
        print("Ocorreu um erro durante o processo !")
        return
      
      restart = input('\nDeseja continuar ?\nS/N: ')
      if(str(restart).lower() == 's'):
        main()
      else:
        return

    elif(else_escolha == 3):
      print('Metadados marcados como confidenciais')
      for i in range(len(files)):
        print(f'\n{confidental_array[i]}: Nivel Restrição: {nivel_restrição[i]}')

      clear()
      
      restart = input('\nDeseja continuar ?\nS/N: ')
      if(str(restart).lower() == 's'):
        main()
      else:
        return

def write():

  conf_file = open('config/confidenciais.txt','w')
  for item in confidental_array:
    conf_file.write(f'{item}\n')
  conf_file.close()


  nivel_file = open('config/nivel_restrição.txt','w')
  for item in nivel_restrição:
    nivel_file.write(f'{item}\n')
  nivel_file.close()

  read()

  return

def read():

  arquivo = open('config/confidenciais.txt','r')
  for linha in arquivo:
      linha = linha.rstrip()
      confidental_array.append(linha)
  arquivo.close()

  arquivo = open('config/nivel_restrição.txt','r')
  for linha in arquivo:
      linha = linha.rstrip()
      nivel_restrição.append(linha)
  arquivo.close()

def adicionar(metadado,nivel):
  confidental_array.append(metadado)
  nivel_restrição.append(nivel)

  write()

  clear()


def delete(value):
  index = confidental_array.index(value)
  confidental_array.pop(index)
  nivel_restrição.pop(index)
  
  write()

  clear()

def clear():
  nivel_restrição.clear()
  confidental_array.clear()

def main():
  read()
  escolha()

if __name__ == "__main__":
  main()