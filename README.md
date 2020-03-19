# Tratamento-de-dados-SPC

-Objetivo

Analisar os dados recebidos pelo SPC e fazer o tratamento dos mesmos seguindo os indicadores propostos.

##O que o nosso algorítmo pode fazer até o momento

### Tabela fonte
Analisar a validade dos CPNJs de acordo com as seguintes regras:
O primeiro campo do CNPJ deve conter 8 dígitos e o segundo campo no máximo 6, se tiver menos, o algorítmo completa com zeros à esquerda até que estejam com 6 dígitos contando os CNPJs válidos e os inválidos. 

###Tabela Operação
Verificar o valor contratado, quantidade de parcelas, valor total do saldo devedor e quantidade de operação por remessa.

###Tabela Movimentação
Verificar total utilizado, valor total fatura, valor total mínimo da fatura, valor total da parcela e quantidade de movimentações por remessa.

###Tabela pagamento 
Verificar o valor total pagamento, quantidade de registros vencidos e quantidade de pagamentos por remessa.

###Em todas as tabelas o algorítmo verifica a data da última atualização que o atributo foi alterado.
