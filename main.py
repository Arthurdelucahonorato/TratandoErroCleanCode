from Classes.torneio import Torneio

if __name__ == "__main__":
    torneio = Torneio()

    # Adicionando times
    torneio.adicionar_time("Brasil")
    torneio.adicionar_time("")  # ❌ Nome inválido
    torneio.adicionar_time("Canadá")
    torneio.adicionar_time("Argentina")
    torneio.adicionar_time("Angola")

    # Criando partidas
    torneio.criar_partida("Brasil", "Canadá", 1, 0)
    torneio.criar_partida("Argentina", "Angola", 2, 0)
    torneio.criar_partida("Brasil", "Argentina", -10, -2)  # ❌ Gols inválidos
    torneio.criar_partida("Brasil", "Argentina", 0, 2)
    torneio.criar_partida("Angola", "Canadá", 1, 1)
    torneio.criar_partida("Brasil", "Angola", 3, 2)
    torneio.criar_partida("Argentina", "Nigéria", 3, 3)  # ❌ Time não existe
    torneio.criar_partida("Argentina", "Canadá", 2, 4)

    # Resultados
    torneio.jogar()
