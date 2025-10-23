import socket
from time import sleep
from threading import Thread

port = 16671
TMP_FILE_NAME = "./tmp.file"

def receive_file(save_path, port):
    global RECEIVER_STARTED
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print("Listening")
    conn, accept = s.accept()
    source_ip = accept[0]
    print(f"Receiving file from {source_ip}")
    with open(save_path, 'wb') as f:
        while chunk := conn.recv(1024): f.write(chunk)
    conn.close()
    s.close()
    print("Received " + save_path)
    RECEIVER_STARTED = False

RECEIVER_STARTED = False

i = 0
while True:
    if(not RECEIVER_STARTED):
        RECEIVER_STARTED = True
        i += 1
        receiver = Thread(target=receive_file, name=f"Receiver {i}", args=[TMP_FILE_NAME, port], daemon=True)
        receiver.start()
    # print("Waiting")
    sleep(1)