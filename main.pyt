print ("🔴 Exercício | Aula 1")

# Intrudução
print("\n \033[1;35;40m Hello world! \033[0m") 
# Explicando a estilização de um texto no terminal
# Começa com  \033[x; y; z m TEXTO \033[0m (Isso para fechar)
# x pode ser 1 = negrito, 2 = itálico e 3 = sublinhado ; y é a cor do texto ; z é a cor do background (para saber a cor basta consultar a tabela) 

# Questão 1
print("\n ◾ Questão 1\n") # \n serve para pular a linha.
print("Digite um número para verificar se ele é positivo, negativo ou zero\n")
num = int(input("Digite um número: "))
print()

if num > 0: 
    print ("\033[1m Número Positivo \033[0m 👍")
elif num < 0:
    print ("\033[1m Número Negativo \033[0m")
else: 
    print("\033[1m Número é zero \033[0m")

# Limpar variável
num = 0

# Questão 2
print("\n ◾ Questão 2\n")
print("Digite um número para verificar se ele é par ou ímpar\n")
num = int(input("Digite um número: "))
print()

if num%2 == 0:
    print("\033[1m Número é par \033[0m 👍")
elif num%2 != 0:
    print("\033[1m Número é ímpar \033[0m")
else: 
    print("\033[1m Número é zero \033[0m")

# Limpar variável
num = 0

# Questão 3
print("\n ◾ Questão 3\n")
print("Digite um número para verificar se ele é divisível por 3\n")
num = int(input("Digite um número: "))
print()

if num%3 == 0:
    print("\033[1m Número é divisível por 3 \033[0m 👍")
elif num%3 != 0:
    print("\033[1m Número não é divisível por 3 \033[0m")
else: 
    print("\033[1m Número é zero \033[0m")

# Limpar variável
num = 0

# Questão 4
print("\n ◾ Questão 4\n")
print("Digite um número para verificar se ele é maior que 10\n")
num = int(input("Digite um número: "))
print()

if num > 10:
    print("\033[1m O Número é maior que 10 \033[0m 👍")
else: 
    print("\033[1m O Número é menor que 10 \033[0m")

# Limpar variável
num = 0  

# Questão 5
print("\n ◾ Questão 5\n")
print("Digite uma letra para verificar se ele é vogal ou não\n")
letra = input("Digite uma letra: ").lower()
print()

if letra in "aeiou": 
    print("\033[1m A letra é vogal \033[0m 👍")
else: 
    print("\033[1m A letra é consoante \033[0m")

# Limpar variável

# Questão 6
print("\n ◾ Questão 6\n")
print("Digite um número e iremos mostrar o seu triplo\n")
num = int(input("Digite um número: "))
print()

triplo = num * 3

print(f"\033[1m O triplo de {num} é {triplo} \033[0m")

# Limpar variável
num = 0

# Questão 7
print("\n ◾ Questão 7\n")
print("Digite um número e iremos mostrar o seu antecessor e sucessor\n")
num = int(input("Digite um número: "))
print()

antecessor = num - 1
sucessor = num + 1

print(f"\033[1m O antecessor e sucessor do número {num} são {antecessor} e {sucessor}, respectivamente \033[0m")

# Limpar variável
num = 0

# Questão 8
print("\n ◾ Questão 8\n")
print("Digite seu \033[2m nome \033[0m e sua \033[2m idade \033[0m\n")
nome = input("Digite seu nome: ")
idade = int(input("Digite um número: "))
print()

print(f"Usuário \n NOME: {nome} \n IDADE: {idade}")

# Questão 9
print("\n ◾ Questão 9\n")
print("Digite um número que iremos mostrar seus 10 números sucessores")
num = int(input("Digite um número: "))
print()

# FÓRMULA: for i in range(0, 10):
for i in range(1, 11):
    num = num + 1
    print(f"O {i}° é {num}")


# Questão 10
print("\n ◾ Questão 10\n")
print("Digite um número que iremos mostrar seus 10 números ímpares sucessores")
num = int(input("Digite um número: "))
print()

# FÓRMULA: for i in range(0, 10):
for i in range(1, 11):
    
    if num%2 ==0:
        num = num + 1
        print(f"O {i}° é {num}")

    else:
       num = num + 2
       print(f"O {i}° é {num}") 


# Questão 11
print("\n ◾ Questão 11\n")
print("Vamos calcular a média de sua nota!")
nota1 = int(input("Digite a 1° Nota: "))
nota2 = int(input("Digite a 2° Nota: "))
nota3 = int(input("Digite a 3° Nota: "))
print()

media = (nota1 + nota2 + nota3)/3

print(f"A sua média é {media}")

# Limpar variável
num = 0

# Questão 12
print("\n ◾ Questão 12\n")
print("Digite um número que iremos mostrar a tabuada desse número")
num = int(input("Digite um número: "))
print()

resul = 0

# FÓRMULA: for i in range(0, 10):
for i in range(1, 11):
    result = num * i
    print(f"{i} * {num} = {result}")

# Limpar variável
num = 0

# Questão 13
print("\n ◾ Questão 13\n")
print("Digite um número que iremos verificar se ele é divisível por 2 e 3 ao mesmo tempo")
num = int(input("Digite um número: "))
print()

if num%2 == 0 and num%3 == 0:
    print(f"O {num} é divisível por 2 e 3 ao mesmo tempo")
else: 
    print(f"O {num} não é divisível por 2 e 3 ao mesmo tempo")

# Questão 14
print("\n ◾ Questão 14\n")
print("Conversor de temperatura de graus Celsius para Fahrenheit")
temp = int(input("Digite a temperatura atual: "))
print()

tempF = (1.8 * temp) + 32

print(f"A {temp}°C é {tempF}°F")

# Limpar variável
num = 0

# Questão 15
print("\n ◾ Questão 15\n")
print("Digite um número mostraremos todos seus 10 números antecessores")
num = int(input("Digite o número: "))
print()

# FÓRMULA: for i in range(0, 10):
for i in range(1, 11):
    num = num - 1
    print(f"O {i}° é {num}")

print("\n \033[1;32;47m Bem-vindo ao curso de back-end com Python \033[0m")
print("\n \033[2;34;40m Exercício complementar \033[0m \n")

# Limpar variável
num = 0

# Questão 16
print("\n ◾ Questão 16\n")
print("Digite um número mostraremos o quadrado dele")
num = int(input("Digite o número: "))
print()

result = num ** 2

print(f"O quadrado de {num} é {result}")

# Questão 17
print("\n ◾ Questão 17\n")
print("Vamos multiplicar números!")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print()

produto = num1 * num2

print(f"{num1} * {num2} = {produto}")

# Questão 18
print("\n ◾ Questão 18\n")
print("Digite as seguites informações abaixo")
nome = input("Insira seu nome: ")
cidade = input("Insira sua cidade: ")
print()

print(f"USUÁRIO: {nome} \nCIDADE: {cidade}")

# Questão 19
print("\n ◾ Questão 19\n")
print("Digite um número e mostraremos todos seus 20 números pares sucessores")
num = int(input("Digite o número: "))
print()

# FÓRMULA: for i in range(0, 10):
for i in range(1, 21): 
    if num%2 == 0:
        num += 2
        print(f"O {i}° é {num}")
    else: 
        num += 1
        print(f"O {i}° é {num}")

# Questão 20
print("\n ◾ Questão 20\n")
print("Vamos calcular a média do ano")
nota1 = int(input("Nota 1° Unidade: "))
nota2 = int(input("Nota 2° Unidade: "))
nota3 = int(input("Nota 3° Unidade: "))
nota4 = int(input("Nota 4° Unidade: "))
print()

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"A média do ano é {media}")


# Questão 21
print("\n ◾ Questão 21\n")
print("Vamos calcular a tabuada dos números")
num = int(input("Digite um número: "))
print()

result = 0

#FÓRMULA: for i in range(0, 10):
for i in range(1, 13): 
    result = num * i
    print(f"{num} * {i} = {result}")

# Questão 22
print("\n ◾ Questão 22\n")
print("Digite um número e verificaremos se ele é divisível por 5 ou 7")
num = int(input("Digite o número: "))
print()

if num%5 == 0 and num%7 == 0: 
    print(f"O {num} é divisível por 5 e por 7")
else: 
    print(f"O {num} não é divisível por 5 e por 7")

# Questão 23
print("\n ◾ Questão 23\n")
print("Convesor de temperatura de Fahrenheit para Celsius")
tempF = int(input("Digite a tempetura atual(°F): "))
print()

tempC = (tempF - 32)/1.8

print(f"{tempF}°F é {tempC}°C")


# Questão 24
print("\n ◾ Questão 24\n")
print("Digite um número e mostreremos seus 10 antecessores")
num = int(input("Digite o número: ")) #Número inicial
print()

# FÓRMULA:
# contador = 10
#   while contador < 10
#       print(contador)
#       contador -= 1
#   print("Fim!")

contador = 1 #Inicialização do contador
while contador < 11: #Definir a quantidade de números que existe na contagem, no caso aqui são 10
    print(f"O {contador}° é {num}")
    num -= 1 # Usado para decrementar o valor do número inicial
    contador += 1 #Usado para fazer contagem dos números 

# Questão 25
print("\n ◾ Questão 25\n")
print("Digite um número para verfirificarmos se é primo ou não")
def is_prime(num):
    """Verifica se um número é primo."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Solicita um número ao usuário
try:
    number = int(input("Digite um número: "))
    if is_prime(number):
        print(f"{number} é um número primo.")
    else:
        print(f"{number} não é um número primo.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")

# Questão 26
print("\n ◾ Questão 26\n")
print("Digite um número para verificarmos se ele é par ou ímpar")
num = int(input("Digite o número: "))
print()

if num%2 == 0:
    print(f"O número {num} é par")
else: 
    print(f"O número {num} é ímpar")

# Questão 27
print("\n ◾ Questão 27\n")
print("Digite um número para varificarmos se ele é divisível por 3 e 5")
num = int(input("Digite o número: "))
print()

if num%3 == 0 and num%5 == 0: 
    print(f"O N° {num} ele é divisível por 3 e por 5")
else: 
    print(f"O N° {num} não divisível")

# Questão 27
print("\n ◾ Questão 27\n")
print("Digite dois números para comparmos qual é maior ")
num1 = int(input("Digite o número: "))
num2 = int(input("Digite o número: "))
print()

if num1 > num2:
    print(f"{num1} > {num2}")
elif num2 > num1:
    print(f"{num2} > {num1}")
elif num1 == num2:
    print(f"Os números são iguais")