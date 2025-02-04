from tkinter import *
from tkinter import ttk


cor1="#080808" #preto
cor2="#f7f7fa" #branco
cor3="#2f32eb" #azul
cor4="#73b4ff" #cinza
cor5="#b30505" #vermelho
cor6="#c5cdd6"
janela=Tk()
janela.title("calculadora")
janela.geometry("235x320")
janela.config(bg=cor1)



frame_tela=Frame(janela,width=235,height=60, bg=cor6)
frame_tela.grid(row=0,column=0)

frame_corpo=Frame(janela,width=235,height=260)
frame_corpo.grid(row=1 ,column=0)



#criando label
valor_texto=StringVar()

#variavel todos valores

todos_valores=""

#criando funçã0
def entrada_usuario(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

  
    valor_texto.set(todos_valores)

#função calcular
def calcular():
    global todos_valores
    resultado=eval(todos_valores)
    
    valor_texto.set(str(resultado))

#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")



app_label= Label(frame_tela, textvariable=valor_texto,width=16, height=2,padx=7,relief=FLAT,anchor='e', justify=RIGHT, font=("Ivy 18 "),bg=cor6,fg=cor1)
app_label.place(x=0,y=0)



#criando botões

b_1=Button(frame_corpo,command=limpar_tela, text="C", width=12,height=2,bg=cor1 ,fg=cor2, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=0)

b_2=Button(frame_corpo, command=lambda:entrada_usuario("%"),text="%", width=6,height=2,bg=cor4 , fg=cor1 ,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_2.place(x=118,y=0)

b_3=Button(frame_corpo, command=lambda:entrada_usuario("/"),text="/", width=6,height=2,bg=cor1,fg=cor2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_3.place(x=179,y=0)

b_4=Button(frame_corpo, command=lambda:entrada_usuario("7"),text="7", width=6,height=2,bg=cor4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=52)

b_5=Button(frame_corpo,command=lambda:entrada_usuario("8"), text="8", width=6,height=2,bg=cor4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_5.place(x=59,y=52)

b_6=Button(frame_corpo, command=lambda:entrada_usuario("9"),text="9", width=6,height=2,bg=cor4,fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_6.place(x=118,y=52)

b_7=Button(frame_corpo, command=lambda:entrada_usuario("*"),text="*", width=6,height=2,bg=cor1,fg=cor2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_7.place(x=179,y=52)

b_8=Button(frame_corpo, command=lambda:entrada_usuario("4"),text="4", width=6,height=2,bg=cor4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_8.place(x=0,y=104)

b_9=Button(frame_corpo, command=lambda:entrada_usuario("5"),text="5", width=6,height=2,bg=cor4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_9.place(x=59,y=104)

b_10=Button(frame_corpo, command=lambda:entrada_usuario("6"),text="6", width=6,height=2,bg=cor4,fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_10.place(x=118,y=104)

b_11=Button(frame_corpo,command=lambda:entrada_usuario("-"), text="-", width=6,height=2,bg=cor1,fg=cor2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_11.place(x=179,y=104)

b_12=Button(frame_corpo,command=lambda:entrada_usuario("1"), text="1", width=6,height=2,bg=cor4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_12.place(x=0,y=156)

b_13=Button(frame_corpo,command=lambda:entrada_usuario("2"), text="2", width=6,height=2,bg=cor4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_13.place(x=59,y=156)

b_14=Button(frame_corpo, command=lambda:entrada_usuario("3"),text="3", width=6,height=2,bg=cor4,fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_14.place(x=118,y=156)

b_15=Button(frame_corpo, command=lambda:entrada_usuario("+"),text="+", width=6,height=2,bg=cor1,fg=cor2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_15.place(x=179,y=156)

b_16=Button(frame_corpo,command=lambda:entrada_usuario("0"), text="0", width=12,height=2,bg=cor4 ,fg=cor1, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_16.place(x=0,y=208)

b_18=Button(frame_corpo, command=lambda:entrada_usuario("."),text=".", width=6,height=2,bg=cor4,fg= cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_18.place(x=118,y=208)

b_19=Button(frame_corpo, command=calcular,text="=", width=6,height=2,bg=cor1,fg=cor2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_19.place(x=179,y=208)


janela.mainloop()

