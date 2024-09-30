import math

# Fatorial
def fatorial(x):
    if x < 0:
        return "Erro: Fatorial de número negativo!"
    return math.factorial(x)

# Soma
def adicionar(x, y):
    return x + y

# Subtração
def subtrair(x, y):
    return x - y

# Multiplicação
def multiplicar(x, y):
    return x * y

# Divisão
def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y
    

def calculadora():
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5 - Fatorial")  # Adicionando a opção de fatorial
    
    while True:
        escolha = input("Digite a opção (1/2/3/4/5): ")

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

        if escolha == '5':  # Se a escolha for fatorial, não precisamos usar num2
            print(f"{num1}! = {fatorial(num1)}")
        else:
            num2 = float(input("Digite o segundo número: ")) # mas se não for a escolha fatorial num2 é adicionado aqui para realizar o restante das operações
            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

            # Pergunta ao usuário se deseja realizar outra operação
            outra_operacao = input("Deseja fazer outra operação? (s/n): ")
            if outra_operacao.lower() != 's':
                break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()
