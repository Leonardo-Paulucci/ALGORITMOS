print("VIAGEM ECONÔMICA - SISTEMA DE DESCONTOS")

# Escolha do destino
print("\nDestinos disponíveis:")
print("1 - Rio de Janeiro (R$ 500)")
print("2 - São Paulo (R$ 450)")
print("3 - Salvador (R$ 600)")

opcao = int(input("Escolha o destino (1, 2 ou 3): "))

if opcao == 1:
    preco = 500
    destino = "Rio de Janeiro"
elif opcao == 2:
    preco = 450
    destino = "São Paulo"
elif opcao == 3:
    preco = 600
    destino = "Salvador"
else:
    print("Opção inválida! Encerrando programa.")
    exit()

# Descontos de perfil
estudante = input("É estudante? (s/n): ").lower()
idoso = input("É idoso? (s/n): ").lower()
fidelidade = input("Possui programa de fidelidade? (s/n): ").lower()

if estudante == "s":
    preco *= 0.90
if idoso == "s":
    preco *= 0.85
if fidelidade == "s":
    preco *= 0.95

# Forma de pagamento
print("\nFormas de pagamento:")
print("1 - Cartão (sem desconto)")
print("2 - Dinheiro (-3%)")
print("3 - Pix (-5%)")
pagamento = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

if pagamento == 2:
    preco *= 0.97
elif pagamento == 3:
    preco *= 0.95

# Etapa extra A - Antecedência
dias = int(input("\nQuantos dias antes da viagem você está comprando? "))

if dias >= 60:
    preco *= 0.92 
elif 30 <= dias < 60:
    preco *= 0.95  

# Etapa extra B - Cupom
cupom = input("\nDigite o cupom promocional (ou deixe vazio): ").upper()

if cupom == "PROMO10":
    preco *= 0.90
elif cupom == "PROMO5":
    preco *= 0.95


print("\n RESUMO DA COMPRA")
print(f"Destino: {destino}")
print(f"Valor final da passagem: R$ {preco:.2f}")
