# https://github.com/AdrianoMatilde/conversor_tkinter_completo/blob/main/conversor_tkinter_completo.py

import tkinter as tk

def converter_temperatura():
    temperatura = float(entrada_temperatura.get())
    entrada_unidade = entrada.get()
    saida_unidade = saida.get()

    if entrada_unidade == saida_unidade:
        resultado['text'] = 'Por favor, escolha unidades de temperatura diferentes.'
        return

    if opcao.get() == 1: # Celsius para Fahrenheit
        temperatura_convertida = (temperatura * 1.8) + 32
    elif opcao.get() == 2: # Fahrenheit para Celsius
        temperatura_convertida = (temperatura - 32) / 1.8
    else: # Celsius para Kelvin
        temperatura_convertida = temperatura + 273.15

    resultado['text'] = f'{temperatura:.2f} {unidades[entrada_unidade]} equivalem a {temperatura_convertida:.2f} {unidades[saida_unidade]}'

# Cria a interface gráfica do usuário
janela = tk.Tk()
janela.title('Conversor de temperatura')

# Adiciona os elementos da interface gráfica
tk.Label(janela, text='Temperatura:').grid(row=0, column=0, padx=10, pady=10)
entrada_temperatura = tk.Entry(janela)
entrada_temperatura.grid(row=0, column=1)

tk.Label(janela, text='De:').grid(row=1, column=0, padx=10, pady=10)
entrada = tk.StringVar(value='Celsius')

menu_entrada = tk.OptionMenu(janela, entrada, 'Celsius', 'Fahrenheit', 'Kelvin')
menu_entrada.grid(row=1, column=1)

tk.Label(janela, text='Para:').grid(row=2, column=0, padx=10, pady=10)
saida = tk.StringVar(value='Fahrenheit')
menu_saida = tk.OptionMenu(janela, saida, 'Celsius', 'Fahrenheit', 'Kelvin')
menu_saida.grid(row=2, column=1)

opcao = tk.IntVar(value=1)
rb1 = tk.Radiobutton(janela, text='Celsius para Fahrenheit', variable=opcao, value=1)
rb1.grid(row=3, column=0)

rb2 = tk.Radiobutton(janela, text='Fahrenheit para Celsius', variable=opcao, value=2)
rb2.grid(row=3, column=1)

rb3 = tk.Radiobutton(janela, text='Celsius para Kelvin', variable=opcao, value=3)
rb3.grid(row=4, column=0)

resultado = tk.Label(janela, text='', font=('Arial', 14), fg='blue')
resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

btn_converter = tk.Button(janela, text='Converter', command=converter_temperatura)
btn_converter.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Define as unidades de temperatura
unidades = {
    'Celsius': '°C',
    'Fahrenheit': '°F',
    'Kelvin': 'K'
}

janela.mainloop()