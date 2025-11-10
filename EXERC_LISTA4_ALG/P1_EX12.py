import random

def jogo_adivinhe_numero():
    numero = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo 'Adivinhe o Número'")
    print("Tente adivinhar um número entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if palpite == numero:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                break
            elif palpite < numero:
                print("O número é maior. Tente novamente.")
            else:
                print("O número é menor. Tente novamente.")
        
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

jogo_adivinhe_numero()