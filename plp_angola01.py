#Crie um programa Python simples que peça ao usuário para inserir dois números e uma operação matemática (adição, subtração, multiplicação ou divisão).
nome = str(input('Inserir o seu nome: '))
ano_nasc = int(input('Inserir o seu ano de nascimento: '))
ano_act = int(input('Inserir o ano actual: '))

idade = ano_act - ano_nasc

print(' Nome: {}, idade: {}'.format(nome, idade))
