import rpyc
import os


def upload_file(remote_service, file_name, data):
    response = remote_service.upload_file(file_name, data)
    print(response)


if __name__ == "__main__":
    conn = rpyc.connect("localhost", 12345)
    remote_service = conn.root
    functions = conn.root.get_functions()

    conn.close()
