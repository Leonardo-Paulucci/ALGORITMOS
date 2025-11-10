cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
   
    cor = input("Digite o nome de uma cor (vermelho, verde, azul): ").strip().lower()
    
    rgb = cores[cor]
    
except KeyError:
    
    print("Erro: Essa cor não está disponível no dicionário.")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
else:
    print(f"A cor '{cor}' tem o valor RGB: {rgb}")
    
finally:
    print("Programa encerrado.")