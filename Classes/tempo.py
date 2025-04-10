class Time:
    def __init__(self, nome):
        if not nome or nome.strip() == "":
            raise ValueError("Nome do time não pode ser vazio ou nulo.")
        self.nome = nome
        self.pontos = 0
