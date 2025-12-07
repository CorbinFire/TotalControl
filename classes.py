from imports import *


class characterbackbone:
    def __init__(self,pos,health,UT) -> None:
        self.pos = pos
        self.health = health
        self.UT = UT

class background:
    def __init__(self,pos,square_size) -> None:
        self.pos = pos
        self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class assault(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'assault')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class sniper(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'sniper')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class recon(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'recon')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class commander(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'commander')

class tank(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'tank')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class plane(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'plane')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class main(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'main')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class farm(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'farm')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class mine(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'mine')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class factory(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'factory')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class airport(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'airport')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)


