
dados_conta = []
historico_operacoes = []


def cadastro_conta():
  
  cont = 0
  
  conta = int(1010)
  dados_conta.append(conta)
  print('BANK - CADASTRO DE CONTA')
  print('================================')
  nome = input('Qual o seu nome completo?: ')
  while nome == '': #VALIDAÇÃO: NOME EM BRANCO
    print('Digite o seu nome para seguirmos o processo de cadastro ')
    nome = input('Qual o seu nome completo?: ')
    cont +=1
  dados_conta.append(nome)
    
  telefone = input('Digite o seu telefone: ')
  while telefone == '': #VALIDAÇÃO: TELEFONE
    print('Digite o seu número de telefone para seguirmos o processo de cadastro ')
    telefone = int(input('Digite o seu telefone: '))
    cont +=1
  dados_conta.append(telefone)


  validador_email = '@'
  email = input('Digite o seu email: ')
  while email == '' or validador_email not in email: #VALIDAÇÃO: EMAIL EM BRANCO OU SEM @ 
    print('Digite o seu email para seguirmos o processo de cadastro ')
    email = input('Digite o seu email: ')
    cont +=1
  dados_conta.append(email)
    
    
  saldo_inicial = int(input('Digite o saldo inicial: '))
  while saldo_inicial < 1000: #VALIDAÇÃO: SALDO INICIAL
    print('SALDO INVÁLIDO')
    saldo_inicial = int(input('Digite o saldo inicial: '))
    cont +=1
  dados_conta.append(saldo_inicial)

  
  limite_credito = int(input('Limite de Crédito disponibilizado: '))
  while limite_credito < 0: #VALIDAÇÃO: LIMITE DE CRÉDITO
    print('LIMITE INVÁLIDO')
    limite_credito = int(input('Limite de Crédito disponibilizado: '))
    cont +=1
  dados_conta.append(limite_credito)
    
  
  senha =  input('Digite a senha que deseja cadastrar: ')
  while len(senha) != 6:
    print('A senha precisa conter 6 dígitos')
    senha =  input('Digite a senha que deseja cadastrar: ')
    cont +=1
    
  validacao_senha = input('Digite novamente a senha cadastrada para validá-la: ')
  while validacao_senha != senha: #VALIDAÇÃO: SENHA CORRETA
      print('SENHAS NÃO SÃO IGUAIS, POR FAVOR DIGITE NOVAMENTE')
      validacao_senha = input('Digite novamente a senha cadastrada para validá-la: ')
      cont +=1
  dados_conta.append(senha)
    
  print("=======================================================")
  print('NÚMERO DA CONTA: ',conta, '\n' 'NOME DO CLIENTE: ',nome, '\n' 'TELEFONE: ',telefone, '\n' 'EMAIL: ',email, '\n' 'SALDO INICIAL: ',saldo_inicial, '\n' 'LIMITE DE CRÉDITO: ',limite_credito, '\n' 'SENHA: ',senha, '\n' 'SENHA VALIDADA: ',senha )
  print("=======================================================")
  print('CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...\n')
  


def deposito():

  cont = 0
  print('BANK - DEPÓSITO EM CONTA')
  print('================================')
  validacao_conta = int(input('Digite o número da sua conta: '))
  
  while validacao_conta != dados_conta[0] or (validacao_conta) == 0: # VALIDAÇÃO DO NÚMERO DA CONTA
    print('NÚMERO DE CONTA INCOMPATÍVEL')
    validacao_conta = int(input('Digite o número da sua conta: '))
    cont +=1
  print('NOME DO CLIENTE: ', dados_conta[1])
  
  valor_deposito = float(input('Qual o valor que deseja depositar: '))
  
  while valor_deposito <= 0: # VALIDAÇÃO DO VALOR DE DEPÓSITO
    print('VALOR INVÁLIDO \n DIGITE UM VALOR QUE SEJA MAIOR QUE 0')
    valor_deposito = float(input('Qual o valor que deseja depositar: '))
    
    cont +=1
  saldo = valor_deposito + dados_conta[4]
  print('O valor depositado foi de R$ %.2f\n Total em conta: R$ %.2f' %(valor_deposito,saldo))
  dados_conta[4] = saldo
  historico_operacoes.append(valor_deposito)
  print('\n')


def sacar():

  cont = 0
  print('BANK - SAQUE DA CONTA')
  print('================================')
  validacao_conta = int(input('Digite o número da sua conta: '))

  while validacao_conta != dados_conta[0]: # VALIDAÇÃO DO NÚMERO DA CONTA
    print('NÚMERO DE CONTA INCOMPATÍVEL')
    validacao_conta = int(input('Digite o número da sua conta: '))
    cont +=1
  print('NOME DO CLIENTE: ', dados_conta[1])
  
  valicao_senha = input('Digite a sua senha: ')

  while valicao_senha != dados_conta[6]:
   print('SENHA INCOMPATÍVEL.\n''DIGITE UMA SENHA VÁLIDA')
   valicao_senha = input('Digite a sua senha: ')
   cont += 1
  
  valor_saque = float(input('Digite a quantidade que deseja sacar: '))

  while valor_saque <= 0:
    print('VALOR INVÁLIDO. O SAQUE PRECISA SER DE NO MÍNIMO R$ 1,00')
    valor_saque = float(input('Digite a quantidade que deseja sacar: '))
    cont += 1

  if dados_conta[4] > 0:
     saque_com_valor_em_conta = dados_conta[4] - valor_saque
     dados_conta[4] = saque_com_valor_em_conta
     historico_operacoes.append(valor_saque) 
     print('VALOR DO SAQUE: %.2f' %(valor_saque)) 
     print('\n') 


  else:
     
     valor_saldo = dados_conta[4] - valor_saque
     valor_limite = dados_conta[5] - valor_saque
     dados_conta[4] = valor_saldo
     dados_conta[5] = valor_limite
     historico_operacoes.append(valor_saque)
     print('VOÇÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')  
     print('SALDO: %.2f' %(dados_conta[4]))  
     print('LIMITE: %.2f' %(dados_conta[5])) 
     print('VALOR DO SAQUE: %.2f' %(valor_saque)) 

     print('\n') 
  





def consulta_saldo():
  
  
   cont = 0
   print('BANK - CONSULTA SALDO')
   print('================================')
   validacao_conta = int(input('Digite o número da sua conta: '))

   while validacao_conta != dados_conta[0]: # VALIDAÇÃO DO NÚMERO DA CONTA
     print('NÚMERO DE CONTA INCOMPATÍVEL')
     validacao_conta = int(input('Digite o número da sua conta: '))
     cont +=1
   print('NOME DO CLIENTE: ', dados_conta[1])
  


   senha =  input('Digite a sua senha do banco: ')
   while len(senha) != 6:
     print('A senha precisa conter 6 dígitos')
     senha =  input('Digite a sua senha do banco: ')
     cont +=1
  
   validacao_senha = input('Digite novamente a senha para validar a entrada: ')
   while validacao_senha != senha: 
       print('SENHAS NÃO SÃO IGUAIS, POR FAVOR DIGITE NOVAMENTE')
       validacao_senha = input('Digite novamente a senha para validar a entrada: ')
   cont +=1
   print('SALDO: %.2f' %(dados_conta[4]))  
   print('LIMITE DE CRÉDITO: %.2f' %(dados_conta[5]))
   print('\n')










def extrato():

  cont = 0

  print('BANK - EXTRATO DA CONTA')
  print('================================')
  
  validacao_conta = int(input('Digite o número da sua conta: '))

  while validacao_conta != dados_conta[0]: # VALIDAÇÃO DO NÚMERO DA CONTA
     print('NÚMERO DE CONTA INCOMPATÍVEL')
     validacao_conta = int(input('Digite o número da sua conta: '))
     cont +=1
     print('NOME DO CLIENTE: ', dados_conta[1])

   
  senha =  input('Digite a sua senha do banco: ')
  while len(senha) != 6:
     print('A senha precisa conter 6 dígitos')
     senha =  input('Digite a sua senha do banco: ')
     cont +=1

  validacao_senha = input('Digite novamente a senha para validar a entrada: ')
  while validacao_senha != senha: 
       print('SENHAS NÃO SÃO IGUAIS, POR FAVOR DIGITE NOVAMENTE')
       validacao_senha = input('Digite novamente a senha para validar a entrada: ')
       cont +=1

  print('LIMITE DE CRÉDITO: %.2f' %(dados_conta[5]))
  print('HISTÓRICO DE OPERAÇÕES: ', historico_operacoes)
  print('SALDO EM CONTA: %.2f' %(dados_conta[4]))
  print('\n')















def menu():

  cont = 0
  
  print('BANK - ESCOLHA UMA OPÇÃO')
  print('=======================================================')
  print('(1) CADASTRAR CONTA')
  print('(2) DEPOSITAR')
  print('(3) SACAR')
  print('(4) CONSULTAR SALDO')
  print('(5) CONSULTAR EXTRATO')
  print('(6) FINALIZAR')
  print('=======================================================')
  menu = int(input('Digite a opção desejada: '))

  

def main():

  
    menu()
    cadastro_conta()
    deposito()
    sacar()
    consulta_saldo()
    extrato()
  
    print('BANK - SOBRE \n')
    print('ESTE PROGRAMA FOI DESENVOLVIDO POR:\n KAYQUE MATIAS FERREIRA')

main()
