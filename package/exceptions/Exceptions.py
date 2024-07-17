class InvalidAction(Exception):
    def __init__(self, mensagem):
        self.message = mensagem

class InvalidName(Exception):
    def __init__(self,msg):
        self.message = msg