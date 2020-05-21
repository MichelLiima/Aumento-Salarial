import time

nome = str(input('Olá, qual é o seu nome? '))
print('##############    \033[7;30;41mSEJA BEM VINDO(a) {}!!\033[m ##############'.format(nome.title())) 
time.sleep(1)
salário = float(input('DIGITE O SEU SÁLARIO ATUAL: R$'))
time.sleep(1)
aumento = float(input('DIGITE QUANTOS % VOCÊ GANHOU DE \033[7;30;41mR${:.2f}\033[m: '.format(salário)))
print('CALCULANDO ................')
time.sleep(3)

por = salário * aumento / 100
soma = salário+por
print('SEU AUMENTO:  \033[7;30;41mR${:.2f}\033[m'.format(por))
print('SEU SÁLARIO ATUAL:  \033[7;30;41mR${:.2f}\033[m'.format(soma))