#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Criado por Rhuann Kael Souza Nascimento - 11/10/2017 - 15:36
Atualização 18/10/2017 - 10:38
Atualização 06/11/2017 - 10:07
Atualização 31/10/2022 - 18:06
"""
import separador as sp
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox as mBox
import os

#GUI - Organizador de Fotos
raiz = Tk()
raiz.iconbitmap("organizador.ico")
raiz.geometry("300x300+610+153")
raiz.iconbitmap(default="organizador.ico")
raiz.resizable(width=1, height=1)

# Variáveis Globais
navegar = ""
btn_upload = PhotoImage(file="btn_upload.png")
btn_ok = PhotoImage(file="btn_ok.png")
imagem = tkinter.PhotoImage(file="main.png")

# GUI Widgets
class Janela:
    def __init__(self, janela1):
        janela1.title("OrganizaFiles")
        self.navegar = ""
        self.container1 = Frame(janela1)
        self.container1.pack()


        self.imagemtitulo = Label(self.container1, image=imagem)
        self.imagemtitulo.pack()

        self.lugar = Label(self.container1, text=navegar)
        self.lugar.place(width=252, height=90, x=24, y=150)

        self.diret = Button(self.container1,bd=2, image=btn_upload, command=self.file_objeto)
        self.diret.place(width=252, height=30, x=24, y=95)

        self.botao2 = Button(self.container1, bd=1, image=btn_ok, command=self.ok)
        self.botao2.place(width=252, height=30, x=24, y=245)

        tkinter.messagebox.showinfo("Tutorial","Organize seus arquivos rapidamente:\n\n\tColoque todos os arquivos "
                                               "em um diretório\nLogo após rodar o programa os arquivos se "
                                               "organizaram por data num piscar de olhos")
# Funções

    def ok(self):
        """Botão de OK Verificação"""
        LUGAR = self.file_objeto
        os.chdir(LUGAR)
        sp.lendo_arquivos_movendo()
        try:
            for _, _, arquivo in os.walk("."):
                distino = os.path.realpath(str(arquivo))
                print(distino, file=open("organizador.log", "a"))
        except:
            print("caminho muito longo", file=open("organizador.log", "a"))
        mBox._show("ARQUIVOS MOVIDOS","SUCESSO")

    def cancelar(self):
        """Cancelar operação"""
        raiz.quit()

    def file_objeto(self):
        """navegar e escolher pasta"""
        navegar = tkinter.filedialog.askdirectory(initialdir=".")
        os.chdir(navegar)
        self.lugar["text"] = "\n o arquivo mais antigo é de: " + str(sp.arquivo_mais_antigo())
        self.file_objeto = navegar
Janela(raiz)
raiz.mainloop()
