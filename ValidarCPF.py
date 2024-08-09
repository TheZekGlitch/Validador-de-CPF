import re

entrada = input("Digite seu CPF: ")

#Primeiro digito
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada,
)
novedigitos = cpf[:9]

i = 10
soma = 0
resultado = ...
digito = ...

for digito in novedigitos:

    resultado = int(digito) * int(i)
    soma = resultado + soma
    i -= 1

digito = ((soma*10) % 11)
digito = digito if digito <= 9 else 0
#Segundo digito

i2 = 11
digito2 = ...

for digito2 in novedigitos:

    resultado2 = int(digito2) * int(i2)
    soma2 = resultado2 + soma
    i2 -= 1

digito2 = ((soma2*10) % 11)
digito2 = digito2 if digito >= 9 else 0
#Formatação do CPF

novo_cpf = (f'{novedigitos}{digito}{digito2}')
if novo_cpf == cpf:
    print('O seu CPF é válido!')
else:
    print('O seu CPF é inválido!')