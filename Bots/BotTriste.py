from Bots.Bot import Bot
from Comando import Comando


class BotTriste(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {
            1: Comando(1, 'Oláa!!', ['Oi...']),
            2: Comando(2, 'Como você está? :)', ['Queria sentir algo para te responder...']),
            3: Comando(3, 'Pode me ajudar?', ['Até posso, mas acho que não ajudaria muito de qualquer jeito...']),
            4: Comando(4, 'Tchau', ['Tchau...'])
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def apresentacao(self):
        return f'Meu nome, infelizmente, é {self.__nome}...'

    def executa_comando(self, cmd):
        try:
            return self.__comando[cmd]
        except:
            print("Não sei...")

    def boas_vindas(self):
        return f'--> {self.nome} diz: Você tinha que escolher logo o mais inútil?'

    def despedida(self):
        return f'--> {self.nome} diz: Finalmente você vai se livrar de mim!'
