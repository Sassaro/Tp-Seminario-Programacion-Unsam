
class Place:

    def __init__(self, tokens):
        #Tokens contenidos en el place
        self.tokens = tokens

    #Se le agregan tokens al place
    def getToken(self,tokens:int):
        self.tokens += tokens
        
    #Se le quitan tokens al Place
    def removeToken(self,tokens:int):
        self.tokens -= tokens