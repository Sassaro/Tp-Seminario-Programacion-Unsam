
#Place hereda de Thread
class Place:

    def __init__(self, tokens):
        #Tokens contenidos en el place
        self.tokens = tokens

    #Se le agrgan tokens al place
    def getToken(self,tokens:int):
        self.tokens += tokens
        
    #Se quitan tokens al Place
    def removeToken(self,tokens:int):
        self.tokens -= tokens