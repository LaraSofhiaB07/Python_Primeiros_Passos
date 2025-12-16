nome = input("Qual Seu nome? ")
idade = int(input("Qual a sua idade? "))
altura = float(input("Qual a sua altura?"))
peso = float(input("Qual seu peso? "))
imc = peso/altura

if idade >= 18:
    print("Você é de maior")
else:
    print("Você é de menor")

if imc < 18.5:
    print(f"Seu peso é {imc} e está Abaixo do peso")

elif imc > 18.5 < 24.9:
    print(f"Seu peso é {imc} e está normal")

