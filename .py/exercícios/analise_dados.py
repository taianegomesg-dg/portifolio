# Lista de vendas (simulando uma coluna de uma planilha)
vendas = [1200, 300, 400, 550, 2030, 350, 890, 456]

print ("--- RELATÓRIO DE ANÁLISE DE DADOS ---")

# 1. Cálculos básicos
total_vendas = sum(vendas)
quantidade_vendas = len(vendas)
media_vendas = total_vendas / quantidade_vendas

# 2. Identificando extremos
melhor_venda = max(vendas)
pior_vendas = min(vendas)

# 3. Filtragem de metas
meta = 1200
acima_da_meta = [v for v in vendas if v >= meta]

# Exibindo os resultados
print (f"Total vendido: R$ {total_vendas}")
print (f"Média de vendas: R$ {media_vendas}")
print (f"Melhor venda: R$ {melhor_venda}")
print (f"Pior venda: R$ {pior_vendas}")
print (f"Meta: R$ {meta}")
print (f"Quantidade que bateu a meta: R$ {len(acima_da_meta)}")

# Verificação de desempenho global
print("-" * 35)
if media_vendas >= 1000:
    print("STATUS FINAL: Meta Batida! O dia foi lucrativo. 🚀")
else:
    print("STATUS FINAL: Alerta! Desempenho abaixo do esperado. 📉")

