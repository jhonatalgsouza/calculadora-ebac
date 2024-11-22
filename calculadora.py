operacao = 0
while operacao != 5:
  num1 = int(input('Insira um número: '))
  num2 = int(input('Insira outro número: '))

  operacao = int(input('Escolha a operação desejada: \n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Sair\n'))

  if operacao == 1:
    print('A adição de', num1, 'e', num2, 'é', num1 + num2)
  elif operacao == 2:
    print('A subtração de', num1, 'e', num2, 'é', num1 - num2)
  elif operacao == 3:
    print('A multiplicação de', num1, 'e', num2, 'é', num * num2)
  elif operacao == 4:
    print('A divisão de', num1, 'e', num2, 'é', num1 / num2)
  elif operacao == 5:
    print('Saindo...')
  else: 
    operacao = int(input('Comando inválido! Insira novamente: '))