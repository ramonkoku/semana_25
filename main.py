# main
from produtor import Produtor
from koku import Consumidor

produtor = Produtor()
consumidor1 = Consumidor("koku")
consumidor2 = Consumidor("arcos ")
espaço = ("\n")
produtor.register_observer(consumidor1)
produtor.register_observer(consumidor2)

produtor.produzir("\n oi eu sou a luz \n")
produtor.produzir("\n vcs deseja qual prato? \n")
