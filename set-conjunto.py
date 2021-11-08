# SET ou Conjunto

# add (adiciona)
# update (atualiza)
# clear (limpa)
# discart (descarta)
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5, 1000}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2000}
s3 = s1 | s2  # union
s4 = s1 & s2  # intersection
s5 = s1 - s2  # difference da esquerda
s6 = s2 - s1  # difference da esquerda
s7 = s1 ^ s2 # symmetric_difference

print(f'\n union |: {s3}')
print(f'\n intersection &: {s4}')
print(f'\n diferença da esquerda s1 - s2: {s5}')
print(f'\n diferença da esquerda s2 - s1: {s6}')
print(f'\n symmetric_difference ^: {s7}')
