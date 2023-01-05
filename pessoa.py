class Pessoa:
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def falar(self,assunto):
        if self.comendo:
            print(f"{self.nome} está comendo e não pode falar agora")
            return
    def comer(self,alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        print(f"{self.nome} está falando.")
        self.falando = True
        print(f"{self.nome} está comendo {alimento}")
        self.comendo = False
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo")
            return

p1 = Pessoa("Gui",18)
p1.comer("maça") # chama o objeto.(nome)função
p1.falar("poo")






