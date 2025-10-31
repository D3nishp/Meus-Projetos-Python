lista_de_compras = []
item = ""
while item != "fim":
    item = input('O que deseja adicionar à lista? (Digite "fim" para parar) ')
    if item != "fim":
      lista_de_compras.append(item)
print(lista_de_compras)