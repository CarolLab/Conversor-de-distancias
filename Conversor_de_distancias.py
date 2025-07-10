import tkinter as tk


#Janela
window = tk.Tk()
window.geometry("650x350")


#Frames
frame_1 = tk.Frame(window)
frame_2 = tk.Frame(window)


#Configuração dos frames
frame_1.config(bg = "#76b4b5")
frame_2.config()


#Exibit os Frames
frame_1.place(relx = 0, rely = 0,
              relwidth = 1, relheight = 0.15)

frame_2.place(relx = 0, rely = 0.15,
              relwidth = 1, relheight = 0.85)


#Título
titulo = tk.Label(frame_1, text = "Conversor de Distâncias",bg = "#76b4b5", font = "Roboto 15 bold")
titulo.place(relx = 0.5, rely = 0.5, anchor = "center")




#Distâncias
distancia_1 = tk.Entry(frame_2, relief = "solid", bd = 1,
                       font = "Calibri 13")
distancia_2 = tk.Label(frame_2, text = "", bd = 2, relief = "solid", bg = "White",
                       font = "Calibri 13")

distancia_1.place(relx = 0.05, rely = 0.25, relwidth = 0.30, relheight = 0.12)
distancia_2.place(relx = 0.65, rely = 0.25, relwidth = 0.30, relheight = 0.12)


#Unidades
km = tk.Label(frame_2, text = "Unidade1", font = "Times")
m = tk.Label(frame_2, text = "Unidade2", font = "Times")


km.place(relx = 0.19, rely = 0.47, anchor = "center")
m.place(relx = 0.80, rely = 0.47, anchor = "center")


#Botão
botao = tk.Button(frame_2, width=15, height = 1, cursor = "hand2",
                  text="Converter", font="Roboto 11",fg = "White",
                  activebackground= "#6e7370", activeforeground= "#ccc9be",
                  bg = "#3b3d3c", bd = 3,
                  relief = "solid", overrelief="flat")
botao.place(relx = 0.51, rely = 0.75, anchor = "n")



#Seta
seta = tk.Label(frame_2, text = "➜", font = "Arial 16")
seta.place(relx = 0.49, rely = 0.25)

#Loop
window.mainloop()