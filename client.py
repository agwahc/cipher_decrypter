import socket


def rand_tmp(self):
    print('arrived')
    host = 'agwahchigozirim'
    s = socket.socket()
    port = 8080
    s.connect((host, port))
    print('Connected to receive rand_tmp.txt...')
    file1 = open('rand_tmp.txt', 'wb')
    file_data1 = s.recv(999999)
    file1.write(file_data1)
    file1.close()
    print('rand_tmp.txt is set up successfully on client end! ')
    fill_tmp(1)


def fill_tmp(self):
    host = 'agwahchigozirim'
    s = socket.socket()
    port = 8081
    s.connect((host, port))
    print('Connected to receive fill_tmp.txt...')
    file2 = open('fill_tmp.txt', 'wb')
    file_data2 = s.recv(999999)
    file2.write(file_data2)
    file2.close()
    print('fill_tmp.txt is set up successfully on client end! ')