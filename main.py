import socket
#import thread
import random
from threading import Thread
import multiprocessing
import worker
HOST = "10.0.0.109"              # Endereco IP do Servidor
PORT = 65440         # Porta que o Servidor esta
from flask_restful import Resource
from flask import request, redirect, url_for, flash, render_template, make_response
from werkzeug.utils import secure_filename
import os
import multiprocessing

import time

ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg'])

UPLOAD_FOLDER = 'C:\\Users\\Nutes\\Desktop\\apiflask-master\\static\\img'
SAVE_FOLDER = 'C:\\Users\\Nutes\\Desktop\\apiflask-master\\static\\processed'

server_livre=0


def tent():
    global server_livre;
    print("recall")
    while(True):
        time.sleep(3)
        try:
            if(server_livre==4):
                PORT = int("6544"+str(server_livre))
                server_livre=0
            else:
                PORT = int("6544"+str(server_livre))
                server_livre += 1
        except:
            tent()
        else:
            try:
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dest = (HOST, PORT)
                tcp.connect(dest)
                id = "id=10"
                tcp.send(bytes("f.fileççççção", "utf-8"))
                tcp.close()
            except:
                tent()

tent()
if __name__ == '__main__':
    jobs = []
    p = multiprocessing.Process(
        target=worker,
    )
    jobs.append(p)
    p.start()