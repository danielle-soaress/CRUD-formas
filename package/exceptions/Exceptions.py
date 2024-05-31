class InvalidShape(Exception):
    def __init__(self, mensagem):
        self.message = mensagem