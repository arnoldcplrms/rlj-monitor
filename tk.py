from time import sleep
from socket import gethostbyname, create_connection
from tkinter import messagebox
from sys import platform

from WindowTitleGetter import WindowTitleGetter

wtg = WindowTitleGetter()

while True:
    print(wtg.get_title())
    sleep(5)

# REMOTE_SERVER = "www.google.com"


# def is_connected():
#     try:
#         host = gethostbyname(REMOTE_SERVER)
#         create_connection((host, 80), 2)
#         return True
#     except:
#         pass
#     return False


# print(is_connected())

# messagebox.showinfo("Title", is_connected())
