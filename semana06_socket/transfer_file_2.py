import socket

# Definindo o endereço de IP para o valor 
# de localhost / loopback
TCP_IP = "127.0.0.1"

# Porta definida para envio do nome do arquivo
FILE_PORT = 5005

# Porta definida para envio do conteúdo do 
# arquivo
DATA_PORT = 5006

# Tempo de espera para disparar evento de
# timeout
timeout = 3
buf = 1024

# Objeto de comunicação socket. Define, com 
# AF_INET, um padrão de comunicação Ethernet.
# SOCK_STREAM define o uso de TCP
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT))

# Estabelece conexção com socket e
# espera por uma mensagem
sock_f.listen(1)

# Objeto de comunicação socket. Define, com 
# AF_INET, um padrão de comunicação Ethernet.
# SOCK_STREAM define o uso de TCP
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))

# Estabelece conexção com socket e
# espera por uma mensagem
sock_d.listen(1)


while True:
    # Espera a requisição de conexão
    # de um cliente, e então aceita
    conn, addr = sock_f.accept()

    # Data recebe o conteúdo de
    # conn para o buffer definido

    # Se o dado não for nulo, printa
    # o conteúdo no terminal
    data = conn.recv(buf)
    if data:
        print "File name:", data
        file_name = data.strip()

    # Abre o arquivo com o nome definido
    f = open(file_name, 'wb')

    # Espera a requisição de conexão
    # de um cliente, e então aceita
    conn, addr = sock_d.accept()

    # Recebe o arquivo e escreve seu
    # conseúdo se não for nulo
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data)

    print "%s Finish!" % file_name
    f.close()