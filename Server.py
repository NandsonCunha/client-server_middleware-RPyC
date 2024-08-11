import rpyc
import os
import time


class MyService(rpyc.Service):
    def __init__(self):
        self.arquivos = {}
        self.interesses = {}

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_upload_file(self, file, data):
        with open(file, "w") as f:
            f.write(data)
        self.arquivos[file] = os.path.getsize(file)
        return f"Arquivo {file} carregado com sucesso."

    def exposed_list_files(self):
        return list(self.arquivos.keys())

    def exposed_download_file(self, file):
        if file in self.arquivos:
            with open(file, "r") as f:
                return f.read()
        else:
            return f"{file} não encontrado"

    def exposed_register_interest(self, file, client_ref, duration):
        if file not in self.interesses:
            self.interesses[file] = []
        expiry_time = time.time() + duration
        self.interesses[file].append((client_ref, expiry_time))
        return f"Interesse registrado em {file} por {duration} segundos."

    def exposed_cancel_interest(self, file, client_ref):
        if file in self.interesses:
            self.interesses[file] = [i for i in self.interesses[file] if i[0] != client_ref]
        return f"Interesse cancelado para o arquivo {file}."


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    server = ThreadedServer(MyService, port=12345)
    server.start()
