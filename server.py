import socket
import os
#import thread
import random
from threading import Thread
from multiprocessing import Process,Lock
from worker import workerr
HOST = "10.0.0.109"              # Endereco IP do Servidor
PORT = 65440          # Porta que o Servidor esta

def conectado(con, cliente):
    try:
        while True:
            msg = con.recv(1024)
            if not msg: break
            print("msg: "+str(msg, "utf-8"))

            id=str(msg,"utf-8").split("=")[1]
            path=str(msg, "utf-8").split("id=")[0]
            print(path)
            print (cliente, str(msg,"utf-8").split("id=")[0]+" o id é: "+str(id))
            rand=random.randint(1,8)
            while(True):
                if(rand==1):
                    a = Process(
                    target=workerr, args=("filho1", Lock)
                    ).start()
                    a.kill()
                    if(a.is_alive()):
                        rand+=1
                    else:
                        a.start()
                        break
                if (rand == 2):
                    b = Process(target=workerr, args=("filho2", Lock)).start()
                    b.kill()
                    if(b.is_alive()):
                        rand +=1
                    else:
                        b.start()
                        break
                if (rand == 3):
                    c = Process(
                        target=workerr, args=("filho"+str(rand), Lock)
                    ).start()
                    if (c.is_alive()):
                        rand += 1
                    else:
                        c.start()
                        break
                if (rand == 4):
                    d = Process(
                        target=workerr, args=("filho"+str(rand), Lock)
                    )
                    d.kill()
                    if (d.is_alive()):
                        rand += 1
                    else:
                        d.start()
                        break
                if (rand == 5):
                    e = Process(
                        target=workerr, args=("filho"+str(rand), Lock)
                    ).start()
                    e.kill()
                    if (e.is_alive()):
                        rand += 1
                    else:
                        e.start()
                        break
                if (rand == 6):
                    f = Process(
                        target=workerr, args=("filho"+str(rand), Lock)
                    ).start()
                    f.kill()
                    if (f.is_alive()):
                        rand += 1
                    else:
                        f.start()
                        break
                if (rand == 7):
                    g = Process(
                        target=workerr, args=("filho"+str(rand), Lock)
                    ).start()
                    g.kill()
                    if (g.is_alive()):
                        rand += 1
                    else:
                        g.start()
                        break
                if (rand == 8):
                    h = Process(
                        target=workerr, args=("filho"+str(rand), Lock)
                    ).start()
                    h.kill()
                    if (h.is_alive()):
                        rand =1
                    else:
                        h.start()
                        break

            print ("Finalizando conexao do cliente", cliente)
            con.close()
            #thread.exit()
    except:
        conectado(con, cliente)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(4)

while True:
    con, cliente = tcp.accept()
    print(con, cliente)
    t = Thread(target=conectado, args=tuple([con,cliente]))
    #thread.start_new_thread(conectado, tuple([con, cliente]))
    t.start()
tcp.close()
'''p = multiprocessing.Process(
                        target=cone,
                    )
p.start()'''