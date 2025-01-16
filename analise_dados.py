# Python Insights - Analisando Dados com Python

### Case - Cancelamento de Clientes

# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link




# !pip install pandas numpy openpyxl nbformat ipykernel plotly

# Passo a passo
# Passo 1: Importar a base de dados

import pandas as pd

tabela = pd.read_csv("cancelamentos.csv");

# Passo 2: Visualizar a base de dados (entender a base + identificar problemas)

display(tabela); # em arquivos ipynb use o display ao em vez do prit, é mais fácil de visualizar

# Informações que não te ajudam, te atrapalham

tabela = tabela.drop(columns="CustomerID"); #drop(tire) da tabela a coluna CustomerId

display(tabela);

# Passo 3: Corrigir os problemas da base de dados (tratamento de dados)
# Passo 3.1: Eliminar valores vazios e colunas inúteis(colunas que não vão me ajudar nessa tarefa)
display(tabela.info()); # verificar as infomações das colunas para saber se tem algum valor vazio

# Analisando temos alguns valores vazios nas colunas (tempo_como_cliente, frequencia_uso, assinatura, duracao_contrato  )
# valores vazio -> deletar essas linhas

tabela = tabela.dropna(); #NaN - Not a Number = valores vazioa, ou seja, dropna(tire os vazios)

display(tabela.info()); 

# Passo 4: Análise Inicial -> quantos clientes cancelaram e qual a % de clientes
# contar na coluna cancelou os valores
display(tabela["cancelou"].value_counts());

# porcentual
display(tabela["cancelou"].value_counts(normalize=True)); # calculando a proporcão(normalize)

# Passo 5: Análise da causa de cancelamentos dos clientes
# comparar as outras colunas da tabela com a coluna de cancelamento
import plotly.express as px # o .express traz gráficos prontos, visuais

# gráficos - sempre que eu for criar um gráfico eu faço em duas etapas

for coluna in tabela.columns:   
    # Etapa 1: criar o gráfico
    grafico = px.histogram(tabela, x= coluna, color = "cancelou", text_auto = True);
    
    # Etapa 2: exibir o gráfico
    grafico.show();

# 1- Usuários do contrato Mensal SEMPRE cancelam
#     - Evitar o contrato mensal e incentivar(com desconto) os contratos anuais e trimestais

# 2- Todos Usuários acima de 50 anos cancelaram o seviço

# 3- Todos os usuários que ligaram mais de 5x no call center cancelaram o serviço
#     - Criar um processo que quando um usuário bater 3x ligações para o call center, ligar alerta vemelho

# 4- Usuários que atrasaram o pagamento mais de 20 dias cancelaram
#     - Criar um alerta para quando o atraso do pagamento bater 15 dias, entrar em contato

# duracao_contrato -> diferente de mensal

condicao = tabela["duracao_contrato"] != "Monthly";

tabela = tabela[condicao];

# porcentual
display(tabela["cancelou"].value_counts(normalize=True)); # calculando a proporcão(normalize)


# ligacoes_callcenter -> menor ou igual a 5

condicao = tabela["ligacoes_callcenter"] <= 5;

tabela = tabela[condicao];

display(tabela["cancelou"].value_counts(normalize=True));


# atraso_pagamento <= 20 dias

condicao = tabela["dias_atraso"] <= 20;

tabela = tabela[condicao];

display(tabela["cancelou"].value_counts(normalize=True));

# Resolvendo esses três problemas da base da dados o porcentual de cancelamentos cairia de:

# 56.71%  -> 21.86% 


