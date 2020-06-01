![image](https://user-images.githubusercontent.com/57918707/81295850-6e8c7d00-9047-11ea-98ea-f68549174851.png)


# Projeto Integrador - Fatec São José dos Campos - SPC Brasil

## SPRINT 3

Nessa sprint focamos em entregar o código de acordo com o seguinte card:

![card_3](https://user-images.githubusercontent.com/55189046/83446994-14a08c80-a426-11ea-9658-5f8a51e55476.jpeg)

## Objetivo

De acordo com pesquisas realizadas e informações coletadas com o SPC, determinamos quais são os dados confidenciais.

Acreditamos que é de grande valor para o SPC analisar a confidencialidade dos dados neste momento, para que assim tenham ciência dos níveís de confidencialidade de cada dado antes de processá-los.

### Base de dados

Nesta entrega é necessário que a base de dados seja inserida no diretório **database**. Não disponibilizamos a base de dados por conter informações confidenciais.

## Funcionalidades do código.

Elaboramos um algoritmo para inserir, excluir e listar os dados confidenciais, que podem ser acessados por um menu e mudados a qualquer momento pelo usuário, de acordo com a sua necessidade.

O algoritmo é capaz de ler as extensões ```xlsx``` e ```csv``` da base de dados enviadas pelo SPC e fazer a verificação em todas as tabelas.

### 1ª Funcionalidade:
Verifica os dados cadastrados pelo usuário como confidenciais e informa qual o nível de restrição: **_Baixo, Médio_** ou **_Alto_**.

![sprint_3_opc_1_1](https://user-images.githubusercontent.com/57918707/83317345-302b4d80-a202-11ea-8b2c-ba5d8db5ce37.gif)

### 2ª Funcionalidade:
Remove um metadado específico da configuração, marcado pelo usuário, para ser analisado como confidencial.

![sprint_3_opc_2_1](https://user-images.githubusercontent.com/57918707/83317359-594bde00-a202-11ea-9b2d-041e2bda4adb.gif)

### 3ª Funcionalidade:
Adiciona o metadado, escolhido pelo usuário, na configuração e marca para ser analisado como confidencial.

![sprint_3_opc_2_2](https://user-images.githubusercontent.com/57918707/83317378-78e30680-a202-11ea-803a-a9d7c16fc75e.gif)


### 4ª Funcionalidade:
Lista todos os metadados marcados como confidenciais pelo usuário.

![sprint_3_opc_2_3](https://user-images.githubusercontent.com/57918707/83317393-a2039700-a202-11ea-8704-ab287e6b240f.gif)

