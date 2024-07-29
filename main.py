from tkinter import *

result = ''
op = ''

def tem_casas_decimais(numero):
    if isinstance(numero, float):
        return not numero.is_integer()
    return False

def botao(x):
    global result
    global op

    x = str(x)
    result += x

    try:
        x = float(x)
    except:
        op=x
    resultado.config(text=result)
    
def calcular():

    global result
    global op

    Deuruim = 0

    print(op)

    valores = []

    x = 0

    if op == 'X':
        valores = result.strip().split('X')
        try:
            v1 = float(valores[0])
            v2 = float(valores[1])
            x = v1 * v2
        except:
            Deuruim = 1

    elif op == '/':
        valores = result.strip().split('/')
        try:
            v1 = float(valores[0])
            v2 = float(valores[1])
            x = v1 / v2
        except:
            Deuruim = 1
        

    elif op == '-':
        # Lidar com números negativos
        if result[0] == '-':
            valores = result[1:].split('-')
            valores[0] = '-' + valores[0]
        else:
            valores = result.split('-')

            try:
                v1 = float(valores[0])
                v2 = float(valores[1])
                x = v1 - v2
            except:
                Deuruim = 1

        

    elif op == '+':
        valores = result.strip().split('+')
        try:
            v1 = float(valores[0])
            v2 = float(valores[1])
            x = v1 + v2
        except:
            Deuruim = 1
        

    if Deuruim==1:
        resultado.config(text='Informe uma conta processável')
    else:
        x = float(x)
        decimal = tem_casas_decimais(x)
        if not decimal:
            try:
                x = int(x)
            except:
                pass

        x = str(x)
        result = x

        resultado.config(text=result)

def apagar():
    global result
    result = ''
    resultado.config(text=result)

def decimal():
    global result
    result += '.'
    resultado.config(text=result)

def removerUltimo():
    global result
    result = result[:-1]
    resultado.config(text=result)

janela = Tk()

janela.title('calculadora braba')
resultado = Label(janela, text=result, font=('Arial', 20))
resultado.grid(row=0, column=0)

# Numeros
botao1 = Button(janela, text='1', command=lambda: botao(1), padx=40, pady=20)
botao2 = Button(janela, text='2', command=lambda: botao(2), padx=40, pady=20)
botao3 = Button(janela, text='3', command=lambda: botao(3), padx=40, pady=20)
botao4 = Button(janela, text='4', command=lambda: botao(4), padx=40, pady=20)
botao5 = Button(janela, text='5', command=lambda: botao(5), padx=40, pady=20)
botao6 = Button(janela, text='6', command=lambda: botao(6), padx=40, pady=20)
botao7 = Button(janela, text='7', command=lambda: botao(7), padx=40, pady=20)
botao8 = Button(janela, text='8', command=lambda: botao(8), padx=40, pady=20)
botao9 = Button(janela, text='9', command=lambda: botao(9), padx=40, pady=20)
botao0 = Button(janela, text='0', command=lambda: botao(0), padx=40, pady=20)

# Operações
mult = Button(janela, text='X', command=lambda: botao('X'), padx=40, pady=20)
div = Button(janela, text='/', command=lambda: botao('/'), padx=40, pady=20)
soma = Button(janela, text='+', command=lambda: botao('+'), padx=40, pady=20)
sub = Button(janela, text='-', command=lambda: botao('-'), padx=40, pady=20)

# Ações
igual = Button(janela, text='=', command=calcular, padx=40, pady=20)
virgula = Button(janela, text=',', command=decimal, padx=40, pady=20)
delete = Button(janela, text='CE', command=apagar, padx=40, pady=20)
removeUltimo = Button(janela, text='<-', command=removerUltimo, padx=40, pady=20)

# Mostrar os botões na tela
delete.grid(row=0, column=2)
removeUltimo.grid(row=0, column=3)
botao7.grid(row=1, column=0)
botao8.grid(row=1, column=1)
botao9.grid(row=1, column=2)
mult.grid(row=1, column=3)
botao4.grid(row=2, column=0)
botao5.grid(row=2, column=1)
botao6.grid(row=2, column=2)
sub.grid(row=2, column=3)
botao1.grid(row=3, column=0)
botao2.grid(row=3, column=1)
botao3.grid(row=3, column=2)
soma.grid(row=3, column=3)
virgula.grid(row=4, column=0)
botao0.grid(row=4, column=1)
igual.grid(row=4, column=2)
div.grid(row=4, column=3)

janela.mainloop()