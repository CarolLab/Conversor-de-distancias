import tkinter as tk

#Funções - - - - -  - - - - - - - - - - - - - - - - - - - - - - - -
def obter_unidade_lstb2():#Obter as unidades selecionadas da listbox 2
    posicao = listbx_2.curselection() #Posição da unidade na listbox2
    if posicao: #se há algum item selecionado
        unidade_label2["text"] = listbx_2.get(posicao) #Obtem a unidade selecionada e
        # muda o texto da label para a unidade


def obter_unidade_lstb1(): #Obter as unidades selecionadas da listbox 1
    posicao = listbx_1.curselection() #Recebe a posição da unidade na listbox1 em tupla
    if posicao: #se há algum item selecionado
        unidade_label1["text"] = listbx_1.get(posicao)#Obtém a unidade selecionada e
        #muda o texto da label para a unidade



def converter(distancia): #Converter unidade 1
    global unidade_label1  # Unidade 1 escolhida
    global unidade_label2  # Unidade 2 escolhida


    try:
        num_converter = float(distancia.get()) #Obter o número a converter
        unidade1 = unidade_label1.cget("text") #Obter a unidade selecionada a ser convertido
        unidade2 = unidade_label2.cget("text")

        label_erro.config(text = "")

        #Dicionário com as fórmulas correspondestes para converter
        formulas_para_converter = {"Km": 1000,#1km == 1000 metros
                                "hm": 100,
                                "dam": 10,
                                "m": 1,
                                "dm": 0.1,
                                "cm": 0.01,
                                "mm": 0.001}


        #Km  (x10 ->)  hm  (x10 ->) dam  (x10->) m  (x10->)  dm  (x10->) cm  (x10->)  mm
        #    (<-x0.1)      (<-x0.1)      (<-x0.1)   (<-x0.1)     (<-x0.1)    (<-x0.1)

        if unidade1 and unidade2: #Se tiver alguma unidade escolhida
            if unidade1 == unidade2:
                distancia_2["text"] = num_converter#Se as unidades forem iguais o número é o mesmo
            else:#Se forem distintas
                #Converter o número da unidade1 para metro
                valor_em_metro = num_converter * formulas_para_converter[unidade1]
                #Número para converter multiplicado pela fómula correspondente para metro

                #Converter de metro para a unidade2 escolhida
                valor_final = valor_em_metro / formulas_para_converter[unidade2]

                distancia_2["text"] = valor_final


        else:
            label_erro["text"] = "Escolha as unidades"

    except ValueError:
        label_erro["text"] = "Insira um número"

#Janela - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
window = tk.Tk()
window.title("Conversor de distâncias")
window.minsize(500, 250)

#Centralizar a janela
#Obter a largura e altura do ecrã
largura_ecra = window.winfo_screenwidth() #Largura do ecrã
altura_ecra = window.winfo_screenheight() #Altura do ecrã

#Largura e altura da janela
largura_window = 650
altura_window = 350

#Calcular as posições x e y
posicao_x = round(largura_ecra/2 - largura_window/2)#Obter a posição x
posicao_y = round(altura_ecra/2 - altura_window/2) - 30 #Obter a posição y

#Configurar geometria da janela
window.geometry(f"{largura_window}x{altura_window}+{posicao_x}+{posicao_y}") #(widthxheight+x+y)



#Frames - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_1 = tk.Frame(window)
frame_2 = tk.Frame(window)

#Configuração dos frames
frame_1.config(bg = "#76b4b5")

#Exibir os Frames
frame_1.place(relx = 0, rely = 0,
              relwidth = 1, relheight = 0.15)

frame_2.place(relx = 0, rely = 0.15,
              relwidth = 1, relheight = 0.85)

#Label_Erro - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
label_erro = tk.Label(frame_2, text = "", fg = "OrangeRed3", font = ("Roboto", 11, "bold"))
label_erro.place(relx = 0.50, rely = 0.92, anchor = "center")

#Título - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
titulo = tk.Label(frame_1, text = "Conversor de Distâncias",bg = "#76b4b5", font = "Roboto 18 bold")
titulo.place(relx = 0.5, rely = 0.5, anchor = "center")



#Distâncias - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Entrys
distancia_1 = tk.Entry(frame_2, relief = "solid", bd = 1,
                       font = "Arial 13") #Número para converter
distancia_2 = tk.Label(frame_2, text = "", bd = 2, relief = "solid", bg = "White",
                       font = "Calibri 13")#Número convertido

distancia_1.place(relx = 0.05, rely = 0.25, relwidth = 0.30, relheight = 0.12)
distancia_2.place(relx = 0.65, rely = 0.25, relwidth = 0.30, relheight = 0.12)


#Unidades - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Listboxs
unidades = ["Km","hm","dam","m","dm", "cm", "mm"] #Unidades disponíveis

listbx_1 = tk.Listbox(frame_2,bd = 2, relief = "solid",font = ("Arial", 13),justify = "center",
                     selectmode = "browse")
listbx_2 = tk.Listbox(frame_2,bd = 2, relief = "solid", font = ("Arial", 13), justify = "center",
                     selectmode = "browse")

#Labels
unidade_label1 = tk.Label(frame_2, text = "", font = "Tahoma") #Label da unidade 1 (lista_1)
unidade_label2 = tk.Label(frame_2, text = "", font = "Tahoma") #Label da unidade 2 (lista_2)


#Inserir as unidades
listbx_1.insert(tk.END, *unidades)
listbx_2.insert(tk.END, *unidades)


#Obter as unidades selecionadas
listbx_1.bind("<<ListboxSelect>>", lambda event: obter_unidade_lstb1())
listbx_2.bind("<<ListboxSelect>>", lambda event: obter_unidade_lstb2())

#Posicionamentos das Listbox e Labels
listbx_1.place(relx = 0.19, rely = 0.47, relwidth = 0.1, relheight = 0.20,anchor = "n")
listbx_2.place(relx = 0.80, rely = 0.47,relwidth = 0.1,relheight = 0.20, anchor = "n")

unidade_label1.place(relx = 0.19, rely = 0.15, anchor = "center")
unidade_label2.place(relx = 0.80, rely = 0.15, anchor = "center")

#Botão - - - - - - - - - - - - - - - - - - - - - - - - -  - - -
botao = tk.Button(frame_2, width=15, height = 1, cursor = "hand2",
                  text="Converter", font="Roboto 11",fg = "White",
                  activebackground= "#6e7370", activeforeground= "#ccc9be",
                  bg = "#3b3d3c", bd = 3,
                  relief = "solid", overrelief="flat",
                  command = lambda: converter(distancia_1))
botao.place(relx = 0.50, rely = 0.80, anchor = "center")

#Scrollbars - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
scrollbar_1 = tk.Scrollbar(listbx_1, relief = "flat")
scrollbar_2 = tk.Scrollbar(listbx_2, relief = "flat")
#Seta - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
seta = tk.Label(frame_2, text = "➜", font = "Arial 16")
seta.place(relx = 0.48, rely = 0.25)

#Loop
window.mainloop()