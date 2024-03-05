import calculadora
def menu():
    a = 1
    b = 2
    print("Menu","\n","1. Somar","\n","2. Subtrair","\n","3. Multiplicar","\n","4. Dividir", "\n","0. Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
       soma = calculadora.somar(a,b)
       print(f'{a} + {b} = {soma}')
    if opcao == 2:
       subtracao = calculadora.subtrair(a,b)
       print(f'{a} - {b} = {subtracao}')      
    if opcao == 3:
       produto = calculadora.multiplicar(a,b)
       print(f'{a} * {b} = {produto}')   
    if opcao == 4:
       quociente = calculadora.dividir(a,b)
       print(f'{a} / {b} = {quociente}')  
    if opcao == 0:
       print('Aplicacao encerrada') 

# Chamando a funcao Menu             
menu()