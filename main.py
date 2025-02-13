import os
import pandas as pd
import plotly.express as px

data_list = os.listdir("./Vendas")
#print(data_list)

joined_table = pd.DataFrame()

for file in data_list:
    if "Vendas" in file:
        table = pd.read_csv(f"./Vendas/{file}")
        joined_table = joined_table._append(table)

#print(joined_table)
# Passo 4 - Calcular o produto mais vendido em quantidade
product_table = joined_table.groupby("Produto").sum()

## Select table to display
product_table = product_table[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(product_table)

# Passo 5 - Calcular o produto que mais faturou
joined_table["Faturamento"] = joined_table["Quantidade Vendida"] * joined_table["Preco Unitario"]
#print(joined_table)]
invoicing_table = joined_table.groupby("Produto").sum()
invoicing_table = invoicing_table[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(invoicing_table)

# Passo 6 - Calcular a loja/cidade que mais vendeu (faturamento)
store_table = joined_table.groupby("Loja").sum()
store_table = store_table[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(store_table)

# Passo 7 - Criar um dashboard
graphic = px.bar(store_table,x=store_table.index ,y="Faturamento")
graphic.show()