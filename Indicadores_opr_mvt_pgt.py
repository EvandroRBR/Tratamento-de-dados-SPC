import xlrd
from datetime import date

operacao = xlrd.open_workbook('STG_OPR_ITT.xlsx')
pagamento = xlrd.open_workbook('STG_PGT.xlsx')
movimento = xlrd.open_workbook('STG_MVT_CRD.xlsx')

opr_sh = operacao.sheet_by_index(0)
pgt_sh = pagamento.sheet_by_index(0)
mvt_sh = movimento.sheet_by_index(0)


#Verificação da ultima atualização dos dados - Indicador Recência
array_dbo_pgt = []
array_dbo_opr = []
array_dbo_mvt = []

for o in range(pgt_sh.nrows):
    if o == 0:
        pass
    else:
        array_dbo_pgt.append(str(pgt_sh.row(o)[-2]).replace("text:","")[1:11])

for o in range(opr_sh.nrows):
    if o == 0:
        pass
    else:
        array_dbo_opr.append(str(opr_sh.row(o)[-2]).replace("text:","")[1:11])

for o in range(mvt_sh.nrows):
    if o == 0:
        pass
    else:
        array_dbo_mvt.append(str(mvt_sh.row(o)[-2]).replace("text:","")[1:11])

atualizacaoPgt = sorted(array_dbo_pgt)[-1]
atualizacaoOpr = sorted(array_dbo_opr)[-1]
atualizacaoMvt = sorted(array_dbo_mvt)[-1]


#Indicador Operação
valorContratado = 0
quantidadeParcelas= 0
saldoDevedor = 0
quantidadeOperacao = 0

for i in range(opr_sh.ncols):
    for linhas in range(opr_sh.nrows):
        if str(opr_sh.row(linhas)[i]) == "empty:''" or linhas == 0:
            pass
        else:
            if i == 1:
                valorContratado += int(str(opr_sh.row(linhas)[1]).replace('text:', '').replace("'",""))
            if i == 2:
                quantidadeParcelas += int(str(opr_sh.row(linhas)[2]).replace('text:', '').replace("'", ""))
            if i == 3:
                saldoDevedor += int(str(opr_sh.row(linhas)[3]).replace('text:', '').replace("'", ""))
            if i == 5:
                quantidadeOperacao += int(str(opr_sh.row(linhas)[5]).replace('text:', '').replace("'", ""))

print("\nIndicadores Operação.")
print(f'Valor Total contrarado: {valorContratado}\n'
      f'Quantidade total de parcelas: {quantidadeParcelas}\n'
      f'Saldo Devedor: {saldoDevedor}\n'
      f'Quantidade total de Operação: {quantidadeOperacao}\n'
      f'Valor pago: {valorContratado - saldoDevedor}\n'
      f'Data da ultima atualização dos dados: {atualizacaoOpr}')


#Indicador Movimentação
valorTotalFatura = 0
valorMinFatura = 0
valorTotalParcela = 0
valorCrdRotativo = 0
quantidadeMovimentacao = 0

for i in range(mvt_sh.ncols):
    for linhas in range(mvt_sh.nrows):
        if str(mvt_sh.row(linhas)[i]) == "empty:''" or linhas == 0:
            pass
        else:
            if i == 1:
                valorCrdRotativo += int(str(mvt_sh.row(linhas)[1]).replace('text:', '').replace("'",""))
            if i == 2:
                valorTotalFatura += int(str(mvt_sh.row(linhas)[2]).replace('text:', '').replace("'", ""))
            if i == 3:
                valorMinFatura += int(str(mvt_sh.row(linhas)[3]).replace('text:', '').replace("'", ""))
            if i == 4:
                valorTotalParcela += int(str(mvt_sh.row(linhas)[4]).replace('text:', '').replace("'", ""))
            if i == 6:
                quantidadeMovimentacao += int(str(mvt_sh.row(linhas)[6]).replace('text:', '').replace("'", ""))

valorTotalUtilizado = valorCrdRotativo + valorTotalFatura + valorTotalParcela

print("\n\nIndicadores Movimentação.")
print(f'Valor total utilizado por remessa: {valorTotalUtilizado}\n'
      f'Valor total da fatura: {valorTotalFatura}\n'
      f'Valor mínimo da fatura: {valorMinFatura}\n'
      f'Valor total de parcelas: {valorTotalParcela}\n'
      f'Quantidade de movimentação: {quantidadeMovimentacao}\n'
      f'Data da ultima atualização dos dados: {atualizacaoMvt}')


#Indicador Pagamento
valorTotalPgt = 0
quantidadeVencido = 0
quantidadePgt = 0

for i in range(pgt_sh.ncols):
    for linhas in range(pgt_sh.nrows):
        if str(pgt_sh.row(linhas)[i]) == "empty:''" or linhas == 0:
            pass
        else:
            if i == 1:
                valorTotalPgt += int(str(pgt_sh.row(linhas)[1]).replace('text:', '').replace("'", ""))
            if i == 5:
                quantidadePgt += int(str(pgt_sh.row(linhas)[5]).replace('text:', '').replace("'", ""))

#Verificação de registros vencidos
data = date.today()
dataAtual = str(data)
dataVencimento = ''
quantidadeVencida = 0

for i in range(pgt_sh.nrows):
    y = str(pgt_sh.row(i)[2]).replace('text:', '').replace("'","")
    dataVencimento = y[4:] + '-' + y[2:4] + '-' + y[:2]
    if dataVencimento < dataAtual:
        quantidadeVencida += 1

print("\n\nIndicadores Pagamemto.")
print(f'Valor total pagamento: {valorTotalPgt}\n'
      f'Quantidade de pagamento: {quantidadePgt}\n'
      f'Quantidade de registros vencidos {quantidadeVencida}\n'
      f'Data da ultima atualização dos dados: {atualizacaoPgt}')
