import sys
import socket
import threading

HEX_FILTER = ''.join([(len(repr(chr(i))) == 3 )and chr(i) or '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode('utf-8', errors='replace')
    result = []
    for i in range(0, len(src), length):
        word = src[i:i+length]
        printable = ''.join([HEX_FILTER[ord(c)] for c in word])
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length * 3
        result.append(f'{i:04x}  {hexa:<{hexwidth}}  {printable}')
    if show:
        for line in result:
            print(line)
    else:
        return result

def receive_form(connection):
    buffer = b""
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    return buffer

def request_handler(buffer):
    return buffer

def response_handler(buffer):
    return buffer

# def proxy_handler(client_socket,remote_host,remote_port,receive_first):
#     remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     remote_socket.connect((remote_host, remote_port))
#     if receive_first:
#         remote_buffer = receive_form(remote_socket)
#         hexdump(remote_buffer)
#     remote_buffer =response_handler(remote_buffer)
#     if len(remote_buffer):
#         print("[<==] Sending %d bytes to localhost ." %len(remote_buffer))
#         client_socket.send(remote_buffer)
    
