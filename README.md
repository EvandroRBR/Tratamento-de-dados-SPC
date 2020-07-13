![topo-readME](https://user-images.githubusercontent.com/57918707/87258458-08bed600-c47a-11ea-9d5e-df9bfb8f4631.png)


# Projeto Integrador - Fatec São José dos Campos

## SPRINT 6 

A Sprint final é a entrega do produto finalizado, com otimizações, como descrito no card abaixo:

![Card_6](https://user-images.githubusercontent.com/56441214/87236836-57aa3400-c3c4-11ea-86dd-6e4b32ff3be0.png)

## - DP Standardize


![marketing_PI_11111](https://user-images.githubusercontent.com/57918707/87260544-dbc5ef80-c488-11ea-8987-faec80939a8b.png)


Pensando na facilitação do dia a dia de um Analista, desenvolvemos o DP Standardize. Com uma interface intuitiva e objetiva que permite ao Analista a padronização dos dados, poupará muito tempo na fase do Data Preparation.

A aplicação permite a personalização dos campos de tabelas em formato ```xlsx``` e ```csv```, o que será explicado com mais detalhes posteriormente, gerando assim, uma tabela com seus dados padronizados ou uma tabela com dados errados para serem devolvidos à fonte e consertados, para só depois serem utilizados em um futuro projeto.

## - Personalização dos campos

Um Analista com conhecimento nos arquivos poderá personalizar os campos, de forma que, a padronização dos seus dados seja de acordo com o necessitado.

As formas de personalização são simples: ele deverá escolher se aquele campo é requerido, único, se contém apenas caracteres numéricos, alfanuméricos ou apenas letras; poderão ser selecionadas mais de uma opção.

Posteriormente, será indicado em qual metadado essas configurações serão atribuídas, e em quais condições.

**Ex.: O Analista seleciona as checkbox requerido, alfanumérico, quando o metadado for id_mdl, sob a condição de C01.**

Feita a padronização, esses novos dados poderão ser enviados às equipes de Gestão, Marketing e Engenharia de Software, para que o desenvolvimento do produto seja colocado em prática.


## - Funcionamento

O cliente irá dispor de uma aplicação segura, onde cada Analista possuirá seu cadastro com login e senha.

A padronização das tabelas é feita de forma rápida, devendo somente arrastar a tabela ao local indicado.

GIF

A página seguinte já contará com seus metadados, que ao serem clicados, abrirão uma nova janela para inserção da personalização já citada no tópico acima.

Após a escolha das opções, clique em Confirmar. Faça o mesmo para todos os metadados que deseja padronizar.

GIF

Ao final, sua nova tabela será gerada e salva automaticamente na pasta **Database** para tomar o destino conveniente.
