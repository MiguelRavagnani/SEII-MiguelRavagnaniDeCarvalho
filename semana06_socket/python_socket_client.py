import socket
import threading
import time

# Define porta para mounicação, formato 
# de decodificação da mensagem, endereço
# de IP e concatenaem formato para reali-
# zar o bind
PORT = 5050
FORMATO = 'utf-8'
SERVER = "192.168.0.109"
ADDR = (SERVER, PORT)

# Objeto de comunicação socket. Define,
# com AF_INET, um padrão de comunicação 
# Ethernet. SOCK_STREAM define o uso de 
# TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Função handler de tratamento de mensagem
def handle_mensagens():

    # Laço que decodifica a mensagem 
    # recebida a patir de =, e formata
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

# Envia  mensagem
def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))

# Recebe o input e chama a função
# enviar() com a mensagem formatada
# com o cabeçalho adequado para
# mensagens
def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)

# Recebe o input e chama a função
# enviar() com a mensagem formatada
# com o cabeçalho adequado para
# nome
def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

# Chama ambas as funções de envio
# de nome e mensagem
def iniciar_envio():
    enviar_nome()
    enviar_mensagem()

# Inicia threads com handler de recebi-
# mento de mensagens e envio
def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()

iniciar()