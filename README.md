# 📊 Analisador de Vendas Automatizado (Python)

Este projeto simula um sistema real de análise de dados onde o script processa informações de fontes externas, realiza cálculos estatísticos e gera um relatório final de desempenho.

## 🚀 Funcionalidades
* **Ingestão de Dados**: Leitura dinâmica de arquivos `.txt` (vendas.txt).
* **Processamento Matemático**: Cálculo automático de Soma, Média, Máximos e Mínimos.
* **Lógica de Metas**: Filtragem inteligente de vendedores que atingiram metas específicas usando *List Comprehension*.
* **Exportação de Relatórios**: Geração automática de um arquivo `relatorio_final.txt` com os resultados da análise.

## 🛠️ Habilidades Técnicas Aplicadas
* **Manipulação de Arquivos (I/O)**: Uso de `with open()` para leitura e escrita segura de dados.
* **Tratamento de Codificação**: Implementação de `UTF-8` para suporte a caracteres especiais.
* **Debugging**: Resolução de erros de sintaxe, caminhos de diretório e encoding de terminal.
* **Versionamento**: Fluxo completo de trabalho com Git (add, commit, push).

## 📁 Estrutura do Projeto
.py/
└── exercícios/
    ├── analise_dados.py    # Script principal
    ├── vendas.txt          # Fonte de dados (Input)
    └── relatorio_final.txt # Relatório gerado (Output)