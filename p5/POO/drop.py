import random
from pygame import Vector2


class drop:
    def __init__(self):
        self.gravity= random.randint(0,6)
        self.size=random.randint(0,4)
        self.R=random.randint(0,255)
        self.V=random.randint(0,255)
        self.B=random.randint(0,255)
        self.position=Vector2(50.50)
    def tomber (self):

        self.position.y = self.position.y + self.gravity

    def raz (self):
        self.position.y=0

