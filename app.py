# Entrada de dados do usuário
nomeObjeto = input("Digite o nome do aparelho: ")
potencia = int(input("Potência (W): "))
usoHoras = int(input("Tempo diário de consumo (horas): "))

# Cálculo do consumo mensal
consumoMensal = (potencia * usoHoras * 30) / 1000

# Exibição dos resultados
print(f"Aparelho: {nomeObjeto}")
print(f"Consumo mensal: {consumoMensal}")

