# 1. Lendo os dados do arquivo externo
vendas = []
with open('.py/exercícios/vendas.txt', 'r') as arquivo:
    for linha in arquivo:
        # Transformamos o texto da linha em número decimal
        vendas.append(float(linha.strip()))

print("--- RELATÓRIO DE ANÁLISE DE DADOS (ARQUIVO) ---")

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
print (f"Quantidade que bateu a meta: {len(acima_da_meta)}")

# Verificação de desempenho global
print("-" * 35)
if media_vendas >= 1000:
    print("STATUS FINAL: Meta Batida! O dia foi lucrativo.")
else:
    print("STATUS FINAL: Alerta! Desempenho abaixo do esperado.")

# Criando um arquivo de relatório final
with open('.py/exercícios/relatorio_final.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write("--- RESULTADO DA ANALISE ---\n")
    relatorio.write(f"Total: R$ {total_vendas}\n")
    relatorio.write(f"Media: R$ {media_vendas}\n")
    relatorio.write(f"Status: {'Lucrativo' if media_vendas >= 1000 else 'Alerta'}")

print("Relatorio gerado com sucesso!")
