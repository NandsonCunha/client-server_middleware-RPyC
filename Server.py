import rpyc
import os

arquivos = {}


def upload_files(file, data):
    with open(file, "w") as f:
        f.write(data)
    arquivos[file] = os.path.getsize(file)
    return f"Arquivo {file} carregado com sucesso."


def list_files(f):
    return f.keys()


def download_files(file):
    if file in arquivos:
        with open(file, "r") as f:
            return f.read()
    else:
        print(f"{file} não encontrado")


def register_interest(file, duration, tempo):
