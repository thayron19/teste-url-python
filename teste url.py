import urllib.request
import tkinter


# ---------------------------------------------------------------------------------------------------------------------
def linha(x):
    linha1 = tkinter.Label(janela, text="-" * 100)
    linha1.place(x=10, y=x)


# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Cálculos')

largura_janela = 325
altura_janela = 250

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicaol = float(largura_janela / 2 - largura_tela / 2)
posicaoa = float(altura_janela / 2 - altura_tela / 2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posicaol, posicaoa))
janela.resizable(width=False, height=False)


# ---------------------------------------------------------------------------------------------------------------------
def funcao_teste_url():
    lista_url = ['', '', '', '', '']
    lista_url[0] = url_var.get()
    lista_url[1] = url_var1.get()
    lista_url[2] = url_var2.get()
    lista_url[3] = url_var3.get()
    lista_url[4] = url_var4.get()

    try:
        urllib.request.urlopen(lista_url[0])
        url_result_var.set('Site OKAY')
    except:
        url_result_var.set('Site fora!')

    try:
        urllib.request.urlopen(lista_url[1])
        url_result_var1.set('Site OKAY')
    except:
        url_result_var1.set('Site fora!')

    try:
        urllib.request.urlopen(lista_url[2])
        url_result_var2.set('Site OKAY')
    except:
        url_result_var2.set('Site fora!')

    try:
        urllib.request.urlopen(lista_url[3])
        url_result_var3.set('Site OKAY')
    except:
        url_result_var3.set('Site fora!')

    try:
        urllib.request.urlopen(lista_url[4])
        url_result_var4.set('Site OKAY')
    except:
        url_result_var4.set('Site fora!')


# ---------------------------------------------------------------------------------------------------------------------
url_texto = tkinter.Label(janela, text='URL: Exemplo \"https://www.tsainfo.com.br/\"', font=('', 12))
url_texto.place(x=10, y=10)
# ---------------------------------------------------------------------------------------------------------------------
url_var = tkinter.StringVar()
url_var.set('http://www.tsainfo.com.br')
url_entry = tkinter.Entry(janela, textvariable=url_var)
url_entry.place(x=10, y=44, width=200)

url_result_var = tkinter.StringVar()
url_result_texto = tkinter.Label(janela, textvariable=url_result_var, font=('', 10))
url_result_texto.place(x=220, y=42)
# ---------------------------------------------------------------------------------------------------------------------
url_var1 = tkinter.StringVar()
url_var1.set('http://www.doenglish.com.br')
url_entry1 = tkinter.Entry(janela, textvariable=url_var1)
url_entry1.place(x=10, y=74, width=200)

url_result_var1 = tkinter.StringVar()
url_result_texto1 = tkinter.Label(janela, textvariable=url_result_var1, font=('', 10))
url_result_texto1.place(x=220, y=72)
# ---------------------------------------------------------------------------------------------------------------------
url_var2 = tkinter.StringVar()
url_var2.set('http://www.google.com.br')
url_entry2 = tkinter.Entry(janela, textvariable=url_var2)
url_entry2.place(x=10, y=104, width=200)

url_result_var2 = tkinter.StringVar()
url_result_texto2 = tkinter.Label(janela, textvariable=url_result_var2, font=('', 10))
url_result_texto2.place(x=220, y=102)
# ---------------------------------------------------------------------------------------------------------------------
url_var3 = tkinter.StringVar()
url_var3.set('http://www.twitter.com')
url_entry3 = tkinter.Entry(janela, textvariable=url_var3)
url_entry3.place(x=10, y=134, width=200)

url_result_var3 = tkinter.StringVar()
url_result_texto3 = tkinter.Label(janela, textvariable=url_result_var3, font=('', 10))
url_result_texto3.place(x=220, y=132)
# ---------------------------------------------------------------------------------------------------------------------
url_var4 = tkinter.StringVar()
url_var4.set('https://www.python.org/')
url_entry4 = tkinter.Entry(janela, textvariable=url_var4)
url_entry4.place(x=10, y=164, width=200)

url_result_var4 = tkinter.StringVar()
url_result_texto4 = tkinter.Label(janela, textvariable=url_result_var4, font=('', 10))
url_result_texto4.place(x=220, y=162)
# ---------------------------------------------------------------------------------------------------------------------
url_btn = tkinter.Button(janela, text='Verificar URL', command=lambda: funcao_teste_url())
url_btn.place(x=10, y=204, width=300)

janela.mainloop()
