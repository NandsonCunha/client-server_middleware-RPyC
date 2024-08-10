import rpyc
import os
import time

arquivos = {}
interesses = {}


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


def register_interest(file, duration):
    if file not in arquivos:
        interesses[file] = []
        expiry_time = time.time() + duration
        interesses[file].append(expiry_time)
        return f"Interesse registrado em {file} por {duration} segundos."
    