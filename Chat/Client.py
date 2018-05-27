import socket
import threading
from tkinter import *

def receiveMsg():
    while True:
        msg = clientSocket.recv(1024).decode("utf8")
        if not msg:
            break
        msgList.insert(END, msg)
        
def sendMsg(event = None):
    data = clientMsg.get()
    clientMsg.set("")
    clientSocket.send(bytes(data, "utf-8"))

def closeChat(event=None):
    clientSocket.close()
    tk.quit()

tk = Tk()
tk.title("Chat")

msgFrame = Frame(tk)
clientMsg = StringVar() 
scrollbar = Scrollbar(msgFrame) 

msgList = Listbox(msgFrame, height=15, width=40, yscrollcommand = scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msgList.pack(side=LEFT, fill=BOTH)
msgList.pack()
msgFrame.pack()

entryField = Entry(tk, width=40, textvariable = clientMsg).pack(fill=BOTH)
sendButton = Button(tk, text = "Send", command = sendMsg).pack(side=RIGHT)
quitButton = Button(tk, text="Quit", command=closeChat).pack(side=LEFT)

tk.protocol("WM_DELETE_WINDOW", closeChat)

HOST = input("Enter host: ")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, 10000))
inputThread = threading.Thread(target = receiveMsg)
inputThread.start()
tk.mainloop()
