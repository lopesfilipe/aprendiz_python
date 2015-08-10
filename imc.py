# coding=UTF-8
# Cálculo do IMC PESO/ALTURA²
#Condição 					  IMC em Mulheres		IMC em Homens
#abaixo do peso 				  < 19.1				< 20.7
#no peso normal			   	    19.1 - 25.8			  20.7 - 26.4
#marginalmente acima do peso    25.8 - 27.3    		  26.4 - 27.8
#acima do peso ideal			27.3 - 32.3 		  27.8 - 31.1
#obeso								> 32.3				> 31.1

while True : 

	print "Cálculo IMC"
	print "\nDigite o peso:"
	while True:
		try:
			peso = float(input())
			break
		except:
			print "Peso inválido"
	print "\nDigite altura:"
	while True:
		try:
			altura = float(input())
			break
		except:
			print "Altura inválido"
	print "\nEscolha seu gênero: \n 1. Masculino \n 2. Feminino"

	while True:
		try:
			genero = int(input())
			while genero < 1 or genero > 2: 
				genero = int(input())
			break
		except:
			print "Gênero inválido"

	imc = peso / altura**2

	if genero == 1:
		if imc < 20.7:
			condicao = "Abaixo do peso"
		elif imc >= 20.7 and imc < 26.4:
			condicao = "No peso normal"
		elif imc >= 26.4 and imc <  27.8:
			condicao = "Marginalmente acima do peso"
		elif imc >= 27.8 and imc < 31.1:
			condicao = "Acima do peso ideal"
		elif imc >= 31.1:
			condicao = "Obeso"
	else:
		if imc < 19.1:
			condicao = "Abaixo do peso"
		elif imc >= 19.1 and imc < 25.8:
			condicao = "No peso normal"
		elif imc >= 25.8 and imc < 27.3:
			condicao = "Marginalmente acima do peso"
		elif imc >= 27.3 and imc < 32.3:
			condicao = "Acima do peso ideal"
		elif imc >= 32.3:
			condicao = "Obeso"
	
	print "\nSeu IMC é: " + str(imc)
	print "Sua condição é considerada " + condicao  
	print "\n\n0. Para sair \n 1. Para calcular IMC novamente"
	while True:
		try:
			opcao = int(input())
			while opcao < 0 or opcao > 1: 
				opcao = int(input())
			break
		except:
			print "Opção inválida"
 
	if opcao == 0:
		break
