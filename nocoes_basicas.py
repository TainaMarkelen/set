# criando um Set normal
animais = set(["cavalo", "coruja", "cachorro"])
print(animais)

# criando um Frozenset, que é imutável
nomes = frozenset(["ana", "joao", "maria"])
print(nomes)

# Set vazio
set_vazio = set()
print(set_vazio)

# adicionando algo
animais.add("gato")
print(animais)

# adicionando usando iteração
for i in range(1, 5):
    animais.add(i)
print(animais)

# união de dois sets
pessoas = {"Ana", "Marina", "Carla"}

# usando a função union()
seres_vivos = animais.union(pessoas)
print(seres_vivos)

# usando o operador |
seres_vivos = animais | pessoas
print(seres_vivos)

# interseção de dois sets, seleciona apenas os elementos comuns
set1 = set()
set2 = set()
for i in range(1, 4):
    set1.add(i)   
for i in range(2, 8):
    set2.add(i)
# usando a função intersection()   
set3 = set1.intersection(set2)
print(set3)

# usando o operador &
frutas = {"banana", "caju", "tomate", "taperebá"}
legumes = {"alface", "rucula", "pepino", "tomate"}
saudavel = frutas & legumes
print (saudavel)

# encontrando diferenças entre sets
lanche = {"hamburguer", "pizza", "pastel"}
almoco = {"carne", "hamburguer", "churrasco"}
# usando a função difference()
comida = lanche.difference(almoco) # Contem em lanche, mas não contem em almoço
print(comida)

# usando o operador -
comida = lanche - almoco
print(comida)

# esvaziando sets
set_x = {1, 2, 3, 4, 5}
set_x.clear()
print(set_x)