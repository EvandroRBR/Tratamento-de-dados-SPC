![image](https://user-images.githubusercontent.com/57918707/81295850-6e8c7d00-9047-11ea-98ea-f68549174851.png)

# Projeto Integrador - Fatec São José dos Campos - SPC Brasil

Uma parceria da Fatec São José dos Campos - Prof. Jessen Vidal com o SPC Brasil para um Projeto Integrador, onde nós alunos tivemos a oportunidade de trabalhar com uma empresa real, com problemas reais, buscar soluções e implantá-las através da metodologia SCRUM.

## - Disciplinas integradas
* ### Engenharia de Software 
  Prof. Me. Giuliano Araujo Bertoti
* ### Sistemas de Informações 
  Prof. Me. José Walmir Gonçalves Duque
* ### Linguagem de Programação
  Profª. Ma. Juliana Forin Pasquini Martiniz


## - Time
* Evandro Braga - PO
* Leonardo Messias - Scrum Master
* Fabrício Rodrigues - DEV Team
* Guilherme Madeira - DEV Team
* Mateus Prestes - DEV Team
* Pedro Mendonça - DEV Team
* Raquel Ribeiro - DEV Team


## - Objetivo

Desenvolvimento de um Aplicativo Desktop com o intuito de ser utilizado como *_Data Preparation_*, ou seja, uma estrutura de análise delineáveis para que futuras remessas de dados sejam facilmente verificadas.

O produto final contará com uma plataforma intuitiva onde podem ser adicionados e/ou retirados campos para análise de acordo com a necessidade do usuário.

Ainda pretendemos implementar um *Data Cleaning* em alguns campos, para serem tratados e corrigidos no momento da análise de dados sem que a remessa precise voltar à fonte devido somente a este campo, como no caso do CNPJ, por exemplo.

## - DP Standardize

![WhatsApp Image 2020-06-28 at 21 18 01](https://user-images.githubusercontent.com/57918707/85962066-e9f21700-b984-11ea-8e24-2506a4884541.jpeg)

Você sabia que a parte mais importante e trabalhosa de um processo de Data Science é o Data Preparation?

É nessa etapa que os dados serão coletados, tratados e consolidados para que sua análise seja precisa, afinal uma má análise significa más decisões de negócios.

DP Standardize é a ferramenta ideal para sua padronização de dados, sendo capaz de analisar qualquer tabela ```xlsx``` e ```csv``` e permitindo a personalização dos campos, ou seja, informando quais tipos de dados não podem conter em cada coluna.

Ao final você pode ter gerado novas tabelas, com seus dados padronizados, prontos para a continuação da elaboração de seu futuro projeto, ou ainda dados fora dos padrões desejados, para ser devolvido à fonte e corrigidos, antes de serem usados em seu projeto.


## - Diagrama de Casos de Uso


![Caso de uso 1](https://user-images.githubusercontent.com/55189046/84602740-ed9f7d00-ae5f-11ea-8f59-99080058b775.png)



## - Cards das Sprints

![CARD'S-1e2](https://user-images.githubusercontent.com/56441214/82007549-e4dd4080-9640-11ea-980a-57477da5d7e7.png)

![CARD'S-3e4](https://user-images.githubusercontent.com/57918707/85963433-0d6c9000-b98c-11ea-9573-080b98e95092.png)

![CARD'S-5e6](https://user-images.githubusercontent.com/57918707/85963435-0fceea00-b98c-11ea-8834-7c1331f6f83a.png)



 ## - Entregas 
   
  <a href='https://github.com/EvandroRBR/Tratamento-de-dados-SPC/tree/sprint-1'> Branch 1 </a>- 16/03/2020 a 20/03/2020
  
  <a href='https://github.com/EvandroRBR/Tratamento-de-dados-SPC/tree/sprint-2'> Branch 2 </a>- 11/05/2020 a 15/05/2020
  
  <a href='https://github.com/EvandroRBR/Tratamento-de-dados-SPC/tree/sprint-3'> Branch 3 </a>- 25/05/2020 a 29/06/2020
  
  <a href='https://github.com/EvandroRBR/Tratamento-de-dados-SPC/tree/sprint-4'> Branch 4 </a>- 08/06/2020 a 14/06/2020
  
  <a href='https://github.com/EvandroRBR/Tratamento-de-dados-SPC/tree/sprint-5'> Branch 5 </a>- 22/06/2020 a 26/06/2020
  
  <a href='https://github.com/EvandroRBR/Tratamento-de-dados-SPC/tree/sprint-6'> Branch 6 </a>- 06/07/2020 a 10/07/2020
  
## - Requisitos necessários para o funcionamento do código
* IDE **Python 3** ou superior;
* Gerenciador de pacotes **Pip 3**;

* IDE **NODEJS 12.18.0v** ou superior;
* Gerenciador de pacotes **npm**;

* Framework **Electron 8.3.1v** ou superior;

  Para instalação em ambientes  ![linux231](https://user-images.githubusercontent.com/56441214/82009828-c11cf900-9646-11ea-8167-d60ff9696b25.jpg)
  é necessário inserir o comando:
  
  
  **Python3**
  ```
    sudo apt install python3-pip
  ``` 
  
  **NODEJS**
  
  ```
     # Using Ubuntu
     curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
     sudo apt-get install -y nodejs
  
     # Using Debian, as root
     curl -sL https://deb.nodesource.com/setup_12.x | bash -
     apt-get install -y nodejs
  ```
  
  **Electron**
  ```
    npm install --save-dev electron
  ```
       
  
  No Windows  ![ruindows](https://user-images.githubusercontent.com/56441214/82010155-aa2ad680-9647-11ea-942e-1195bcb956be.jpg)   assim que instalada a IDE do Python, o pip é adicionado por padrão.
  
  
  **NODEJS**
  
  ```
    https://nodejs.org/en/download/
  ```
  
  **Electron**
  ```
    npm install --save-dev electron
  ```
  
* Bibliotecas **xlrd**, **csv**, **matplotlib** e **sys** .

  Em qualquer sistema operacional, os comandos para instalar as bibliotecas xlrd e matplotlib são, respectivamente:
  
  ```pip3 install xlrd```
  
  ```pip3 install matplotlib```
  
  
  As bibliotecas **datatime**, **csv** e **sys** já vem instaladas por padrão.
