# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler as dimensões de um hexagono, calcular e escrever a área. 

import math

lado = float(input('Insira o valor de um dos lados do hexágono'))
area = ((3*pow(lado,2)*math.sqrt(3))/2)
print("A área do seu hexágono é", round(area, 2))
