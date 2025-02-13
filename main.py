# Lógica de Programação
# Passo 0 - Entender o problema
# Passo 1 - Percorrer a pasta Vendas para acessar os dados
import os

data_list = os.listdir("./Vendas")
#print(data_list)

# Step 2 - Import sells database
for data in data_list:
    if "Vendas" in data:
        print(f"./Vendas/{data}")
    else :
        print("Return file")

# Step 3 - Treat the databases



# Passo 4 - Calcular o produto mais vendido em quantidade
# Passo 5 - Calcular o produto que mais faturou
# Passo 6 - Calcular a loja/cidade que mais vendeu (faturamento)
# Passo 7 - Criar um dashboard
