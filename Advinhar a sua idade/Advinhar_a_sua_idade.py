import time

def linha():
    print("=========================================================")

linha()

print("Vou advinhar a sua idade atraves de quatro simples perguntas...")
linha()
time.sleep(3)
ale = int(input("Informe um numero entre 1 e 10!:" '\n'))
time.sleep(3)
ano = int(input("Informe o ano do seu nascimento!:" '\n'))
time.sleep(3)
ani = str(input("Você fez aniversario este ano? [S/N]" '\n'))
if ani.lower() ==("S" and "s"):
    print("Você fez aniversario este ano!")
    linha()
    print("Vou multiplicar por 2 o numero que você pensou!")
    linha()
    time.sleep(5)
    print("Vou adicionar mais 5 ao resultado!")
    linha()
    time.sleep(5)
    print("Vou multiplicar por 50!")
    linha()
    time.sleep(5)
    print("Vou somar 1772 ao resultado parcial")
    linha()
    time.sleep(5)
    print("Agora vou subtrair pelo ano do seu nascimento!")
    linha()
    idade=((ale * 2 + 5)* 50 + 1772 - ano)
    time.sleep(5)
    print("Aguarde estou calculando...")
    linha()
    time.sleep(5)
    print("Certo já sei a sua idade!")
    linha()
    time.sleep(5)
    print("O resultado final deu:" , idade)
    linha()
    time.sleep(5)
    print("O primeiro numero é o que voce escolheu, e os dois ultimos e a sua idade atual!")

elif ani.lower() ==("N" and "n"):
    print("Você não fez aniversario este ano!")
    linha()
    print("Vou multiplicar por 2 o numero que você pensou!")
    linha()
    time.sleep(5)
    print("Vou adicionar mais 5 ao resultado!")
    linha()
    time.sleep(5)
    print("Vou  multiplicar por 50!")
    linha()
    time.sleep(5)
    print("Agora vou somar 1771 ao resultado parcial")
    linha()
    time.sleep(5)
    print("Agora vou subtrair pelo ano do seu nascimento!")
    linha()
    idade=((ale * 2 + 5)* 50 + 1771 - ano)
    time.sleep(5)
    print("Aguarde estou calculando...")
    linha()
    time.sleep(5)
    print("Certo já sei a sua idade!")
    linha()
    time.sleep(5)
    print("O resultado final deu:" , idade)
    linha()
    time.sleep(5)
    print("O primeiro numero é o que voce escolheu, e os dois ultimos e a sua idade atual!")

else:
    print("Voce digitou um numero invalido. Favor informar o numero corretamente!")