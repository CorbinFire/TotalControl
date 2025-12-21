from imports import *

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
width,hieght = info.current_w,info.current_h
square_size = np.array([width,width]) if width < hieght else np.array([hieght,hieght])
sidelen = np.array([0,width]) if width < hieght else np.array([hieght,0])
add_to_each_point = np.array([0,(hieght-width)/2]) if width < hieght else np.array([(width-hieght)/2,0])

class characterbackbone:
    def __init__(self,pos,health,UT,size,im) -> None:
        self.damage_multiplier = 100/health
        self.pos = np.array(pos)+add_to_each_point
        self.size = np.array([size[0]*square_size[0],size[1]*square_size[1]])
        self.im = pygame.transform.scale(pygame.image.load(im),self.size)
        self.centerpos = np.array([self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2])
        self.health = health
        self.UT = UT

class attack:
    def __init__(self,dmg,deviation=0):
        self.dmg = dmg
        self.deviation = deviation
    
    def use(self,opponent):
        opponent.health -= random.randint(self.dmg-self.deviation,self.dmg+self.deviation)

class sidebarclass:
    def __init__(self,pos) -> None:
        self.index = 1
        self.pgindex = 0
        self.pages = [{1:['Assets/soldier generator.png',main],2:['Assets/farm.png',farm],3:[],4:[]},{1:['Assets/mine.png',mine],2:['Assets/pistol soldier2.png',assault],3:[],4:[]},{1:['Assets/tank.png',tank],2:[],3:[],4:[]}]#,[[],[],[],[]],[]]
        self.page = self.pages[self.pgindex]
        self.poses = [np.array(pos)-[0.075]*sidelen,np.array(pos)]
        self.pos = self.poses[self.index]
        self.sizes = [np.array([0.2*square_size[0],0.4*square_size[1]]),np.array([0.05*square_size[0],0.055*square_size[1]])]
        self.size = self.sizes[self.index]
        self.ims = [pygame.transform.scale(pygame.image.load('Assets/sidebar.png'),self.sizes[0]),pygame.transform.scale(pygame.image.load('Assets/dropbox.png'),self.sizes[1])]
        self.im = self.ims[self.index]

class background:
    def __init__(self,pos) -> None:
        self.pos = np.array(pos)
        self.im = pygame.transform.scale(pygame.image.load('Assets/background.png'),square_size+square_size+square_size)

class bullet(attack):
    def __init__(self,pos,endpoint,dmg,dev) -> None:
        super.__init__(dmg,dev)
        self.pos = np.array(pos)
        self.im = pygame.transform.scale(pygame.image.load('Assets/bullet.png'),square_size*np.array([0.0075,0.0075]))
        self.endpoint = np.array(endpoint)

class assault(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,30,'assault',[0.02375,0.02725],'Assets/pistol soldier2.png')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class sniper(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,30,'sniper')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class recon(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,20,'recon')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class commander(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'commander')

class tank(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,100,'tank',[0.03,0.0425],'Assets/tank.png')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class plane(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,80,'plane')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class main(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'main',[0.04725,0.05],'Assets/soldier generator.png')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class farm(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'farm',[0.05225,0.055],'Assets/farm.png')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class mine(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'mine',[0.055,0.05],'Assets/mine.png')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class factory(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'factory')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)

class airport(characterbackbone):
    def __init__(self,pos) -> None:
        super().__init__(pos,60,'airport')
        # self.im = pygame.transform.scale(pygame.image.load('total con background.png'),square_size)


