import socket
import time
import sys

# Definindo o endereço de IP para o valor 
# de localhost / loopback
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1]

# Objeto de comunicação socket. Define, com 
# AF_INET, um padrão de comunicação Ethernet.
# SOCK_DGRAM define o uso de udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define umd estino e envia um pacote por UDP
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

# Abre o arquivo com o nome definido
f = open(file_name, "r")

# Data recebe o conteúdo do arquivo
data = f.read(buf)

# Enquanto mensagem não é nula, envia pacotes
# por UDP 
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()