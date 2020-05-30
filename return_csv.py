import csv

def metadado_csv(file):
    with open(f'./{file}.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        c = 0

        lista = []

        metadado_tratado = []

        for line in csv_reader:
            if(c == 0):
                lista.append(line[0].split('|'))
            c += 1
        
        for item in lista[0]:
            if item:
                metadado_tratado.append(str(item).replace(" ",""))

        return metadado_tratado

def corpo_csv(file):
  with open(f'./{file}.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    c = 0

    lista = []

    corpo_tratado = []

    for line in csv_reader:
      if(c != 0):
        lista.append(line[0].split('|'))
      c += 1

    for item in lista:
      nova_lista = []
      for i in item:
        if(i):
          if '+--' not in i:
            nova_lista.append(i)            
          
          
      corpo_tratado.append(nova_lista)

    return corpo_tratado

def tuple_csv(file_to_run):
  data = corpo_csv(f'complemento/{file_to_run}')
  metadado = metadado_csv(f'complemento/{file_to_run}')

  data_tratado = []

  for i in data:
    cont = 0
    for z in i:
      data_tratado.append([])
      data_tratado[cont].append(z)
      cont += 1

  dicionario = dict(zip(metadado,data_tratado))

  return dicionario,metadado
