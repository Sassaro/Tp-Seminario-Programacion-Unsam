from ast import arg
import threading
import time
from tkinter import Y

#Place hereda de Thread
class Place:

    def __init__(self, tokens):
        #Tokens contenidos en el place
        self.tokens = tokens

    def getToken(self,tokens:int):
        self.tokens += tokens

    def removeToken(self,tokens:int):
        self.tokens -= tokens