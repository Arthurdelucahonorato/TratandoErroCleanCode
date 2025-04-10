import logging
from Classes.tempo import Time
from Classes.partida import Partida

logging.basicConfig(
    filename='torneio.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Torneio:
    def __init__(self):
        self.times = {}
        self.partidas = []

    def adicionar_time(self, nome):
        try:
            time = Time(nome)
            self.times[nome] = time
        except Exception as e:
            logging.error(f"Erro ao adicionar time '{nome}': {e}")
            print(f"❌ Erro ao adicionar time '{nome}': {e}")

    def criar_partida(self, nome1, nome2, gols1, gols2):
        try:
            if nome1 not in self.times or nome2 not in self.times:
                raise ValueError("Um ou ambos os times não estão registrados.")

            partida = Partida(self.times[nome1], self.times[nome2], gols1, gols2)
            self.partidas.append(partida)
            partida.resultado()
        except Exception as e:
            logging.error(f"Erro ao criar partida entre '{nome1}' e '{nome2}': {e}")
            print(f"❌ Erro ao criar partida entre '{nome1}' e '{nome2}': {e}")

    def jogar(self):
        print("\n🏆 Classificação Final:")
        ranking = sorted(self.times.values(), key=lambda t: t.pontos, reverse=True)
        for i, time in enumerate(ranking, 1):
            print(f"{i}. {time.nome} - {time.pontos} pontos")

        print("\n📋 Resultados das Partidas:")
        for partida in self.partidas:
            print(partida.placar())
