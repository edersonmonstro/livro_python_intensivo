bandas = ['pink floyd', 'daft punk', 'prodigy', 'chemical brothers']
for banda in bandas:
    print(banda)

for valor in range(1,10):
    print(valor)

d12 = list(range(1,13))
print(d12)

d10_pares = list(range(2,11,2))
print(d10_pares)

# quadrados perfeitos
quadrados = []
for valor in range(1,11):
    quadrado = valor ** 2
    quadrados.append(quadrado)
print(quadrados)

# list comprehensions
quadrados = [valor ** 2 for valor in range(1,11)]
print(quadrados)

# estatisticas simples
digitos = [1,2,3,4,5,6,7,8,9,0]
print(min(digitos))
print(max(digitos))
print(sum(digitos))

#fatia de lista
print(digitos[0:4])
print(digitos[:5])
print(digitos[6:])

for digito in digitos[:5]:
    print(digito)

# copiando lista pra outra independente
digitos_copiado = digitos[:]
print(digitos_copiado)