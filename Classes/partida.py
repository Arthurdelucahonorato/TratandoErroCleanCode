class Partida:
    def __init__(self, time1, time2, gols1, gols2):
        if gols1 < 0 or gols2 < 0:
            raise ValueError("Gols não podem ser negativos.")
        self.time1 = time1
        self.time2 = time2
        self.gols1 = gols1
        self.gols2 = gols2

    def resultado(self):
        if self.gols1 > self.gols2:
            self.time1.pontos += 3
        elif self.gols2 > self.gols1:
            self.time2.pontos += 3
        else:
            self.time1.pontos += 1
            self.time2.pontos += 1

    def placar(self):
        return f"{self.time1.nome} {self.gols1} x {self.gols2} {self.time2.nome}"
