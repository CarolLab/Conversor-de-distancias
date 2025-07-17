import tkinter as tk

def converter(distancia):
    global unidade_lstb1
    global unidade_lstb2


    unit_1 = int(distancia.get())
    distancia_2["text"] = unit_1 * 1000

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
posicao_x = round(largura_ecra/2 - largura_window/2)
posicao_y = round(altura_ecra/2 - altura_window/2) - 30

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


#Título - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
titulo = tk.Label(frame_1, text = "Conversor de Distâncias",bg = "#76b4b5", font = "Roboto 18 bold")
titulo.place(relx = 0.5, rely = 0.5, anchor = "center")




#Distâncias - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
distancia_1 = tk.Entry(frame_2, relief = "solid", bd = 1,
                       font = "Calibri 13")
distancia_2 = tk.Label(frame_2, text = "", bd = 2, relief = "solid", bg = "White",
                       font = "Calibri 13")

distancia_1.place(relx = 0.05, rely = 0.25, relwidth = 0.30, relheight = 0.12)
distancia_2.place(relx = 0.65, rely = 0.25, relwidth = 0.30, relheight = 0.12)


#Unidades - - - - - - - - - - - - - - - - - - - - - - - - - - - -
unidades = ["Km", "m"] #Unidades disponíveis

lista_1 = tk.Listbox(frame_2,bd = 2, relief = "solid",font = ("Arial", 13),justify = "center",
                     selectmode = "browse", state="disabled")
lista_2 = tk.Listbox(frame_2,bd = 2, relief = "solid", font = ("Arial", 13), justify = "center",
                     selectmode = "browse", state = "disabled")


#Inserir as unidades
lista_1.insert(tk.END, *unidades)
lista_2.insert(tk.END, *unidades)


#Posicionamentos das Listbox
lista_1.place(relx = 0.19, rely = 0.47, relwidth = 0.1, relheight = 0.20,anchor = "n")
lista_2.place(relx = 0.80, rely = 0.47,relwidth = 0.1,relheight = 0.20, anchor = "n")

#Botão - - - - - - - - - - - - - - - - - - - - - - - - -  - - -
botao = tk.Button(frame_2, width=15, height = 1, cursor = "hand2",
                  text="Converter", font="Roboto 11",fg = "White",
                  activebackground= "#6e7370", activeforeground= "#ccc9be",
                  bg = "#3b3d3c", bd = 3,
                  relief = "solid", overrelief="flat",
                  command = lambda: converter(distancia_1))
botao.place(relx = 0.50, rely = 0.80, anchor = "center")



#Seta - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
seta = tk.Label(frame_2, text = "➜", font = "Arial 16")
seta.place(relx = 0.48, rely = 0.25)

#Loop
window.mainloop()