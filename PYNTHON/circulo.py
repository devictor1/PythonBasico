# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler as dimensões de um circulo, calcular e escrever a área. 

from math import pi

raio = float(input('Insira abaixo o valor do raio do circulo'))
area = pi * raio * raio
print("A área do seu círculo é", area)