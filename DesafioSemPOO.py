menu = ("""====SISTEMA BANCÁRIO====\n
Depósito[D]\nSaque[S]\nExtrato[E]\nSair[Q]""")

saldo = 0
limite = 500
LIMITE_SAQUES = 3
num_saques = 0
extrato = ""
print(f"Seu saldo é: {saldo}")

while True:

  opcao = input(menu)

  if opcao in "Dd":
    valor_depo = float(input("Qual valor gostaria de depositar? "))

    if valor_depo > 0:
      saldo += valor_depo
      extrato += f"Depósito: R$ {valor_depo:.2f}\n"
    else:
      print("Erro. Informe um valor válido.")

  elif opcao in "Ss":
    valor_saque = float(input("Qual valor gostaria de sacar? "))

    if num_saques < LIMITE_SAQUES:
      if limite > valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}"
        num_saques += 1
      else:
        print("Erro. verique o limite de valor.")
    else:
      print("Erro. verique o limite de operações.")
      
  elif opcao in "Ee":
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

 
  elif opcao in "Qq":
    break
  
  else:
    print("Erro. Selecione uma operação válida.")