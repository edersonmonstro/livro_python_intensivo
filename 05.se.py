carros = ['audi', 'bmw', 'subaru', 'toyota']

for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())

sabor_solicitado = 'cogumelos'
if sabor_solicitado != 'anchovas':
    print("segura as anchovas")

coberturas_solicitadas = ['cogumelos','cebolas','abacaxi']
if 'cogumelos' in coberturas_solicitadas:
    print('cogumelos solicitados')
else:
    print('cogumelos nao foram solicitados')

if 'peperoni' not in coberturas_solicitadas:
    print('peperoni nao foi solicitado')
else:
    print('peperoni foi solicitado')

idade = 42

if idade < 4:
    print("seu ingresso é gratuito")
elif idade < 18:
    print("seu ingresso custa R$5")
else:
    print("seu ingresso custa R$10")