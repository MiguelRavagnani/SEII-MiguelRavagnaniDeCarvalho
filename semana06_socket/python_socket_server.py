# Importando socket, threading e time
import socket
import threading
import time

# Define SERVER_IP como o endereço
# localhost, ou seja, 127.0.01
SERVER_IP = socket.gethostbyname(socket.gethostname())

# Porta escolhida para conexão
PORT = 5050

# Endereço completo formatado para
# realzar o bind
ADDR = (SERVER_IP, PORT)

# Formato utilizado para decodificar
# a mensagem
FORMATO = 'utf-8'

# Objeto de comunicação socket. Define,
# com AF_INET, um padrão de comunicação 
# Ethernet. SOCK_STREAM define o uso de 
# TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Designando o endereço ao objeto socket
# criado anteriormente
server.bind(ADDR)

conexoes = []
mensagens = []

# Enviando mensagens 
def enviar_mensagem_individual(connection):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        
        # Envia a mensagem o formato estabelecido
        # para leitura msg={msg}
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao["conn"].send[mensagem_de_envio]
        conexao["last"] = i + 1
        time.sleep(0.2)


# Itera pelas conexoes e envia
# as mensagens indiviualmente
def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexoes)

# Função handler chamada quando
# novas requisições de conexão são
# aceitas
def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    nome = False

    # Laço que espera por uma mensagem
    while (True):

        # Recebe uma mensagem de tamanho
        # máximo 1024
        msg = conn.recv(1024).decode(FORMATO)

        # Verifica se a mensaem não é nula
        if(msg):

            # Se a mensagem se iniciar com
            # nome={nome}, recupera o nome 
            if(msg.startswith("nome=")):
                mensagem_separada = msg.split("=")
                
                # Nome recebe a string após =
                nome = mensagem_separada[1]
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": last}

                conexoes.append(mapa_da_conexao)
                enviar_mensagem_individual(mapa_da_conexao)
            
            # Verifica se a mensagem
            # se inicia com msg={msg},
            # e recuepra a mensagem
            elif(msg.startswith("msg=")):
                mensagem_separada = msg.split("=")
                mensagem = mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos()

# Função para iiciar socket
def start():
    print("[INICIANDO] Iniciando")

    # Estabelece conexção com socket e
    # espera por uma mensagem
    server.listen()

    # Laço que espera a conexão de um cliente
    while(True):

        # Espera a requisição de conexão
        # de um cliente, e então aceita
        conn, addr = server.accept()

        # Cria uma thread de conexão com 
        # o handler de clientes, utilizando
        # a última requisição de conexão
        # aceita
        thread = threading.Thread(
            target=handle_clientes,
            args=(conn, addr))

        # Inicia a thread
        thread.start()


start()