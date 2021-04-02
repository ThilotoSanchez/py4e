import socket

# validation for valid URL
while True:
    try:
        page = input('Enter URL: ')
        if len(page) < 1: page = 'http://data.pr4e.org/intro-short.txt'
        sp = page.split('/')
        host = sp[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((f'{host}', 80))
        break
    except:
        print('URL not valid. Please enter complete URL.')
        continue

cmd = f'GET {page} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
