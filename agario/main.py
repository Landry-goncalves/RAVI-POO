import core
from agario.bille import Bille
from agario.creep import Creep
from agario.playeur import Playeur

playeur1 = None


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    global playeur1
    playeur1 =Playeur()

    print("Setup END-----------")


def run():
    print('run')
    playeur1.afficher(core)
    if core.getMouseLeftClick() is not None:
        playeur1.deplacer(core.getMouseLeftClick())

if __name__ == '__main__':
    core.main(setup, run)




















if __name__ == '__main__':
    mon_joueur = player()
