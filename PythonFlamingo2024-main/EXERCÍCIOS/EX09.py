# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. 
# Calcular e escrever o valor do novo salário.


salarioMensal = float(input('Digite o salário mensal do colaborador'))
percentualReajuste = float(input('E qual o percentual de reajuste do salário?'))
reajuste = (percentualReajuste/100)*salarioMensal
salarioFinal = salarioMensal + reajuste

print('O salário final do colaborador é de', salarioFinal)