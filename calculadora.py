def calculadora():
    valor1 = float(input("digite o primeiro valor "))
    valor2 = float(input("digite o segundo valor "))
    operacao = input("digite 'sum' para somar,\n 'sub' para subtrair,\n 'mult' para multiplicar\n ou 'div' para dividir \n")
    if operacao == 'sum':
        #soma
        print('{} + {} = '.format(valor1, valor2))
        print(valor1 + valor2)
    elif operacao == 'sub':
        #subtração
        print('{} - {} = '.format(valor1,valor2))
        print(valor1 - valor2)
    elif operacao == 'mult':
        #multipicação
        print('{} x {} = '.format(valor1, valor2))
        print(valor1*valor2)
    elif operacao == 'div':
        #divisão
        print('{} / {} = '.format(valor1,valor2))
        print(valor1/valor2)
    else:
        print('você não digitou uma operação, por favor tente novamente!')
    return

calculadora()