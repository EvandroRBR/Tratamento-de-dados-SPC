![image](https://user-images.githubusercontent.com/57918707/81295850-6e8c7d00-9047-11ea-98ea-f68549174851.png)

# Projeto Integrador Fatec São José dos Campos junto ao SPC Brasil

## - Disciplinas integradas
* ### Engenharia de Software 
  Prof. Me. Giuliano Araujo Bertoti
* ### Sistemas de Informações 
  Prof. Me. José Walmyr Gonçalves Duque
* ### Linguagem de Programação
  Profª. Ma. Juliana Forin Pasquini Martiniz

## - Time
* Evandro Braga - PO
* Leonardo Messias - Scrum Master
* Fabrício Rodrigues - DEV Team
* Mateus Prestes - DEV Team
* Pedro Mendonça - DEV Team
* Raquel Ribeiro - DEV Team

## - Objetivo

Uma parceria da Fatec São José dos Campos - Prof. Jessen Vidal com o SPC Brasil para um Projeto Integrador, onde nós alunos tivemos a oportunidade de trabalhar com uma empresa real, com problemas reais, buscar soluções e implantá-las através da metodologia SCRUM.

Recebemos do SPC Brasil uma remessa de dados juntamente com indicadores a serem alcançados.

## Cards das Sprints

![CARD'S-1e2](https://user-images.githubusercontent.com/56441214/82007549-e4dd4080-9640-11ea-980a-57477da5d7e7.png)

![CARD'S-3e4](https://user-images.githubusercontent.com/56441214/82007561-ee66a880-9640-11ea-94db-9fa764787218.png)

![CARD'S-5e6](https://user-images.githubusercontent.com/56441214/82007582-f6bee380-9640-11ea-83bf-eec28dd75058.png)

## Requisitos necessários para o funcionamento do código
* Python 3 ou superior
* pip 3

  Em ambientes ![linux231](https://user-images.githubusercontent.com/56441214/82009828-c11cf900-9646-11ea-8167-d60ff9696b25.jpg)
 é necessário rodar o comando para instalação:

  ```sudo apt install python3-pip``` 
  
  No Windows ![ruindows](https://user-images.githubusercontent.com/56441214/82010155-aa2ad680-9647-11ea-942e-1195bcb956be.jpg) quando instalado o python, o pip é automaticamente instalado em suas dependências.
  
* Bibliotecas xlrd e matplotlib

  Em qualquer sistema operacional, os comandos para instalar as bibliotecas xlrd e matplotlib, são respectivamente:
  
  ```pip3 install xlrd```
  
  ```pip3 install matplotlib```
  
  A biblioteca datatime já vem instalado por padrão.

Após levantamento de requisitos, desenvolvemos um algoritmo para tratamento dos dados.

## - O que o nosso algoritmo pode fazer até o momento

### Tabela Fonte

Analisar a validade dos CNPJs de acordo com as seguintes regras:
O primeiro campo do CNPJ deve conter 8 dígitos e o segundo campo no máximo 6, se tiver menos, o algorítmo completa com zeros à esquerda até que estejam com 6 dígitos contando os CNPJs válidos e os inválidos. 

![WhatsApp-Video-2020-05-07-at-08 57 31](https://user-images.githubusercontent.com/57918707/81297010-19516b00-9049-11ea-88c6-dc0d3d72e9cf.gif)

### Tabela Operação
Verificar o valor contratado, quantidade de parcelas, valor total do saldo devedor e quantidade de operação por remessa.

### Tabela Movimentação
Verificar total utilizado, valor total fatura, valor total mínimo da fatura, valor total da parcela e quantidade de movimentações por remessa.

### Tabela Pagamento 
Verificar o valor total pagamento, quantidade de registros vencidos e quantidade de pagamentos por remessa.

![WhatsApp-Video-2020-05-07-at-08 58 03](https://user-images.githubusercontent.com/57918707/81297260-65041480-9049-11ea-98a6-171cdb9a05ab.gif)

* Em todas as tabelas o algorítmo verifica a data da última atualização que o atributo foi alterado.

* As tabelas e os indicadores não estão disponíveis por conter dados sigilosos.

