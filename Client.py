import rpyc
import os
from tkinter import *
import customtkinter


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


root = customtkinter.CTk()


root.geometry("500x400")

root.config(background="#2F3136")

button_upload = customtkinter.CTkButton(master=root,text="Escolher Arquivo")

button_query_file = customtkinter.CTkButton(master=root,text="Mostrar Arquivos")

button_mark_interest = customtkinter.CTkButton(master=root,text="Marcar Interesse",command=input_register_interest)

button_show_file_interest = customtkinter.CTkButton(master=root,text="Mostrar Arquivos com interesse")


button_upload.place(relx=0.5,rely=0.3,anchor=CENTER)

button_query_file.place(relx=0.5,rely=0.4,anchor=CENTER)

button_mark_interest.place(relx=0.5,rely=0.5,anchor=CENTER)

button_show_file_interest.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()
