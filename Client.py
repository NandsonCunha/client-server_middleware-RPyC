import rpyc
import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import customtkinter
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import string
import shutil
'''
def upload_file(remote_service, file_name, data):
    response = remote_service.upload_file(file_name, data)
    print(response)


if __name__ == "__main__":
    conn = rpyc.connect("localhost", 12345)
    remote_service = conn.root
    functions = conn.root.get_functions()

    conn.close()
'''

def input_register_interest():
    textDialog = customtkinter.CTkInputDialog(text="Digite O Nome do Arquivo de Interesse",title="Marcar Interesse")
    print("Arquivo",textDialog.get_input())

# setPreviewFile --> mostra o caminho do arquivo no input
def setPreviewFile(filepath):
    path_entry.insert(0,filepath)


# selectFile --> abre uma tela que possiilita a escolha do arquivo
def selectFile():
    global filename
    filename=filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select File",
    )
    setPreviewFile(filename)

# saveFile --> pega o arquivo escolhido e guardar na pasta de arquivos,acho que essa função fica melhor no server
def saveFile():
    filenameSplitted=filename.split('.')
    randomText = ''.join((random.choice(string.ascii_lowercase) for x in range (12)))
    shutil.copy(filename,f"./arquivos/{randomText}.{filenameSplitted[1]}")
    setPreviewFile("")
    messagebox.showinfo("Sucesso","Upload Feito Com Sucesso")


root = customtkinter.CTk()

root.title("Gerenciador Arquivos")

root.geometry("650x400")

root.config(background="#2F3136")

frame = customtkinter.CTkLabel(root,text="")


frame.place(relx=0.83,rely=0.3,anchor=CENTER) # type: ignore

button_upload = customtkinter.CTkButton(master=root,text="Escolher Arquivo",command=selectFile)

path_entry = customtkinter.CTkEntry(master=root,width=200)

saveBtn = customtkinter.CTkButton(master=root,text="Upload",width=50,command=saveFile)



button_query_file = customtkinter.CTkButton(master=root,text="Mostrar Arquivos")

button_mark_interest = customtkinter.CTkButton(master=root,text="Marcar Interesse",command=input_register_interest)

button_show_file_interest = customtkinter.CTkButton(master=root,text="Mostrar Arquivos com interesse")



path_entry.place(relx=0.55,rely=0.3,anchor=CENTER) # type: ignore

saveBtn.place(relx=0.75,rely=0.3,anchor=CENTER) # type: ignore

button_upload.place(relx=0.3,rely=0.3,anchor=CENTER) # type: ignore

button_query_file.place(relx=0.5,rely=0.4,anchor=CENTER) # type: ignore

button_mark_interest.place(relx=0.5,rely=0.5,anchor=CENTER) # type: ignore

button_show_file_interest.place(relx=0.5,rely=0.6,anchor=CENTER) # type: ignore


root.mainloop()
