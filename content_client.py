import socket
import tqdm
import os

def download_file(filename):
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 9090
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    filesize = os.path.getsize(filename)

    s = socket.socket()

    print(f"[+] Connecting to {SERVER_HOST}:{SERVER_PORT}")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))
    s.close()