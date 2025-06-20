CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario * bonus

# 5) Imprima cálculo do KPI para o usuário
# print("KPI: " + str(kpi))

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
# print(nome + " recebeu R$ " + str(salario) + " de salário e " + str(bonus) + " de bônus.") # minha solução
print(f"O usuário {nome} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?