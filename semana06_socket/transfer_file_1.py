import socket
import sys

# Definindo o endereço de IP para o valor 
# de localhost / loopback
TCP_IP = "127.0.0.1"

# Porta definida para envio do nome do arquivo
FILE_PORT = 5005

# Porta definida para envio do conteúdo do 
# arquivo
DATA_PORT = 5006

buf = 1024

# Recebe o nome do arquivo como argumento da linha
# de comando do temrinal
file_name = sys.argv[1]

# Trata exceções no escopo try:
try:
    # Objeto de comunicação socket. Define, com 
    # AF_INET, um padrão de comunicação Ethernet.
    # SOCK_STREAM define o uso de TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Estabelece comunicação utilizando o método
    # connect() do objeto sock, da classe socket
    # por TCP, para a porta definida para envio 
    # nome de arquivos
    sock.connect((TCP_IP, FILE_PORT))

    # Através do método send(), realiza a 
    # transferência de file_name
    sock.send(file_name)

    # Encerra a comunicação fechando o socket
    sock.close()

    # Comunica por terminal o envio de file_name
    print ("Sending %s ..." % file_name)

    # Abre o arquivo de nome file_name
    f = open(file_name, "rb")

    # Cria o objeto de comunicação socket. Define, com 
    # AF_INET, um padrão de comunicação Ethernet.
    # SOCK_STREAM define o uso de TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Estabelece comunicação utilizando o método
    # connect() do objeto sock, da classe socket
    # por TCP, para a porta definida para envio 
    # de dados do arquivo
    sock.connect((TCP_IP, DATA_PORT))

    # Recupera informações do arquivo lido
    # e atribui à variável data
    data = f.read()

    # Envia os dados do arquivo
    sock.send(data)

finally:
    # Finaliza a última coneção aberta
    # no escopo try: antes de entrar
    # no escopo finaly:
    sock.close()

    # Fecha o arquivo aberto
    f.close()