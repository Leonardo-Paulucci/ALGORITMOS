agenda = {
    "Maria": "99999-1234",
    "João": "98888-1234",
    "Ana": "97777-1234"
}

agenda["Leonardo"] = "96666-1234"
print("Agenda após adicionar Leonardo:", agenda)

del agenda["Ana"]
print("Agenda após remover Ana:", agenda)

print("Todos os contatos da agenda:")
for nome, telefone in agenda.items():
    print(f"{nome}: {telefone}")