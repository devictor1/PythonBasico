# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler as dimensões de um hexagono, calcular e escrever a área. 

lado = float(input('Insira o valor de um dos lados do hexágono'))
apotema = float(input('Agora, escreva o valor da apótema do hexágono'))
area = ((lado*apotema)/2)*6
print("A área do seu hexágono é", area)