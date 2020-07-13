![topo-readME](https://user-images.githubusercontent.com/56441214/87261187-ae2e7580-c48b-11ea-91de-e2bad8f5b938.png)

# Projeto Integrador - Fatec São José dos Campos 

## SPRINT 4

Após feedback da empresa e uma breve conversa sobre entrega de valor para essa sprint, acordamos junto ao cliente que seria priorizado o card abaixo:


![Card_4](https://user-images.githubusercontent.com/56441214/87236813-14e85c00-c3c4-11ea-8733-102d125fb978.png)



Desenvolvemos uma ferramenta para ser utilizada como *_Data Preparation_*, ou seja, uma estrutura de análise delineáveis para que futuras remessas de dados sejam facilmente verificados.

Além disso, essa ferramenta é utilizada de forma intuitiva, onde podem ser adicionados e/ou retirados campos para análise de acordo com a necessidade do usuário. 

## Objetivo

Apresentação de um **Aplicativo Desktop** versão beta, onde iremos verificar os valores nulos e repetidos; acreditamos ser de grande valor para a empresa a capacidade de analisar a movimentação dos consumidores.

**Mas o que isso tem a ver com a verificação de dados nulos ou repetidos?**

Pense que você consumidor, pode dispor de várias formas de pagamento, financiamento, empréstimos, ou seja, diversas modalidades. Se você contratou um empréstimo e fez uma compra parcelada com seu cartão de crédito, o seu CPF será exibido duas vezes, ou seja, será um campo repetido, porém, não será um dado incorreto. 

O mesmo ocorre com campos nulos: pense agora que você fez uma compra com seu cartão de crédito, porém não parcelou sua compra; o seu CPF será exibido para essa compra, porém no campo Quantidade de Parcelas será exibido o valor nulo, pois não há parcelamento, e mais uma vez, isso não será um dado incorreto.

Voltando ao valor dessa entrega: esse é um cenário reduzido do que pode ser realizado com o auxílio dessa ferramenta. Optamos por analisar dados que já possuímos o algoritmo pronto, para demonstrar o funcionamento do **Aplicativo Desktop**, porém posteriormente podem ser adicionadas novas camadas para o desenvolvimento de uma **“Plataforma para Preparação e Governança dos Dados da Empresa”**.

## Como funciona?

Primeiramente é selecionada a opção desejada para verificação dos dados. Feito isso, irá aparecer um submenu com as opções das tabelas a serem analisadas:

![simplescreenrecorder-2020-06-14](https://user-images.githubusercontent.com/55189046/84605937-da001080-ae77-11ea-93aa-b476fe1aa4a4.gif)

Após escolha da tabela, as informações serão descritas no campo lateral.

Esta foi uma solução para entrega de um **Aplicativo Desktop** versão beta; reconhecemos as limitações, que serão tratadas em sprints posteriores.
