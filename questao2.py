# Questão 2
def fibonacci(a: int, b: int, number: int):
    result = a + b

    if result < number:
        return fibonacci(b, result, number)
    elif result == number:
        return True
    
    return False


number = int(input("Informe um número: "))

if fibonacci(0, 1, number):
    print(f"O número {number} pertence à sequência!")
else:
    print(f"O número {number} não pertence à sequência!")