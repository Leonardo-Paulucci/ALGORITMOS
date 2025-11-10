def transferencia(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    print("Transferência realizada com sucesso!")

try:
    saldo = float(input("Digite o saldo da conta: "))
    valor = float(input("Digite o valor da transferência: "))
    transferencia(saldo, valor)
except ValueError as e:
    print(f"Erro: {e}")