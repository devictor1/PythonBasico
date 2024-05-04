# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos 
# brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total 
# de eleitores.

eleitoresTotal = int(input('Seja bem-vindo! Digite o total de eleitores desse município'))
votosBrancos = int(input('Desses eleitores, quantos votaram em Branco?'))
votosNulos = int(input('E quantos votaram nulo?'))
votosValidos = int(input('Logo, a quantidade de votos válidos foi de quanto?'))

percentualBrancos = (100*votosBrancos)/eleitoresTotal
percentualNulos = (100*votosNulos)/eleitoresTotal
percentualValidos = (100*votosValidos)/eleitoresTotal

print('O percentual de votos brancos foi de' , percentualBrancos, '%')
print('O percentual de votos nulos foi de', percentualNulos, '%')
print('O percentual de votos válidos foi de', percentualValidos, '%')