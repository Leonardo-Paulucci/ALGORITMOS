atletas = [
    {
        "nome": "Ana",
        "idade": 20,
        "modalidades": ["natação", "corrida"],
        "treinos": {"natação": 10, "corrida": 5}
    },
    {
        "nome": "Bruno",
        "idade": 25,
        "modalidades": ["futebol", "musculação", "corrida"],
        "treinos": {"futebol": 12, "musculação": 7, "corrida": 4}
    },
    {
        "nome": "Carla",
        "idade": 22,
        "modalidades": ["musculação"],
        "treinos": {"musculação": 15}
    }
]

def media_idade_por_esporte(atletas, esporte):
    idades = [a["idade"] for a in atletas if esporte in a["modalidades"]]
    if idades:
        return sum(idades) / len(idades)
    return None

def esporte_mais_treinado(atleta):
    if not atleta["treinos"]:
        return None
    return max(atleta["treinos"], key=atleta["treinos"].get)

def atletas_multiesporte(atletas):
    return [a["nome"] for a in atletas if len(a["modalidades"]) > 2]

print("Média de idade (corrida):", media_idade_por_esporte(atletas, "corrida"))
print("Esporte mais treinado de Bruno:", esporte_mais_treinado(atletas[1]))
print("Atletas com mais de 2 modalidades:", atletas_multiesporte(atletas))