class Jogo():
    def __init__(self,tempo,modo):
        self.tempo = tempo
        self.modo = modo
    def get_tempo(self):
        return self.tempo
    def set_tempo(self,novo_tempo):
        self.tempo = novo_tempo
    def get_modo(self):
        return self.modo
    def set_modo(self,novo_modo):
        self.modo = novo_modo
    def mostra_dados(self):
        print(f"JOGO\nTEMPO:{self.tempo} HORAS\nMODO DE JOGO: {self.modo}")

if __name__ == "__main__":
    jogo1 = Jogo(5,"Médio")
    #print(jogo1)
    jogo2 = Jogo(10, "Díficil")
    print("\t\t-----CARREGANDO DADOS ------")
    print("------ INFORMAÇÕES SOBRE OS JOGOS!--------")
    print("JOGO1:")
    print(f"DURAÇÃO: {jogo1.get_tempo()} HORAS\nMODO: {jogo1.get_modo()}")
    print("-"*30)
    print("JOGO2:")
    print(f"DURAÇÃO: {jogo2.get_tempo()} HORAS\nMODO: {jogo2.get_modo()}")
    print("IREMOS FAZER A ATUALIZAÇÃO DOS MODOS DE JOGOS E TEMPOS:")
    x = input("DIGITE UM NOVO TEMPO PARA O JOGO:")
    jogo1.set_tempo(x)
    jogo1.get_tempo()
    y = input("DIGITE UM NOVO MODO PARA O JOGO:")
    jogo1.set_modo(y)
    jogo1.get_modo()
    jogo1.mostra_dados()


    #print(f"O TEMPO DO JOGO FOI ALTERADO PARA {jogo1.get_tempo()} HORAS")
    #jogo1.mostra_dados()
