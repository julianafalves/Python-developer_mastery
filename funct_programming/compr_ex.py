some_list = ['a','b','c','b','d','m','n','n']

lista1 = list({char for char in some_list if some_list.count(char) > 1})
print(lista1)