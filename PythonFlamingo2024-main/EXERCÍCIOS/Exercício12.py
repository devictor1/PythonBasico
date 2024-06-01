# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler as dimensões de um trapézio (base amior, base menor e altura),
# calcular e escrever a área do trapézio. a=(B+b).h/2

baseMaior = float(print("Insira o valor da base maior do seu trapézio"))
baseMenor = float(print("Agora, escreva o valor da base menor do seu trapézio"))
altura = float(print("Por último, insira o valor da altura do seu trapézio"))
area = (baseMaior+baseMenor)*altura/2
print("A área do seu trapézio é de ", area, " m²")