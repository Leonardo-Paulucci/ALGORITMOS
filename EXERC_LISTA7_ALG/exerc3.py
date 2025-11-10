try:
   
    numero = float(input("Digite um número: "))

    if numero > 10:
        print("O número é válido pois é maior que 10.")
    else:
        print("O número não é maior que 10.")

except ValueError:
    print("Erro: Por favor, insira um número válido.")

else:
    print("Programa executado com sucesso!")

finally:
    print("Programa encerrado.")