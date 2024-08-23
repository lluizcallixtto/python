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
    num =+ i
    print(f"O {i}° é {num}")

