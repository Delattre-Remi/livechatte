import socket

def send_file(file_path):
    s = socket.socket()
    s.connect(('127.0.0.1', 16671))
    with open(file_path, 'rb') as f:
        s.sendfile(f)
    s.close()

send_file('test.file')