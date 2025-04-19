import pygame
import random
import time
import math
import sys

pygame.init()
pygame.mixer.init()
wn = pygame.display.set_mode((2600,1400))
background = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con background.png'),(2600,1400))
class background:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.im = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con background.png'),(2600,1400))

class map_hidder:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.im = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con dark cloud hidemap.png'),(600,600))

class flamethrower_soldier:
    def __init__(self,pos,side,speed,color) -> None:
        self.hp = 120
        self.move = True
        self.originalhp = 120
        self.hpbar = 50
        self.side = side
        self.color = color
        self.unittype='fs'
        self.im = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con flamethrower soldier.png'),(65,65))
        self.originalpos = pos
        self.speed = speed
        self.pos = pos
        self.target = pos

class pistol_soldier:
    def __init__(self,pos,side,speed,color) -> None:
        self.hp = 70
        self.move = True
        self.originalhp = 70
        self.hpbar = 50
        self.side = side
        self.color = color
        self.unittype='ps'
        self.im = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con pistol soldier.png'),(50,50))
        self.originalpos = pos
        self.speed = speed
        self.pos = pos
        self.target = pos

class buildingfspsgen:
    def __init__(self,pos,side,color) -> None:
        self.unittype=['fs','ps']
        self.side = side
        self.color = color
        self.hpbar = 150
        self.spawnfs = False
        self.spawnps = False
        self.hp = 150
        self.fspsgen = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con soldier generator.png'),(175,175))
        self.pos = pos

class picbuildingfspsgen:
    def __init__(self,pos) -> None:
        self.unittype='pic'
        self.side = None
        self.fspsgen = pygame.transform.scale(pygame.image.load('/Users/cameroncheke/TotalControl/total con soldier generator.png'),(175,175))
        self.pos = pos    

class bullet:
    def __init__(self,pos,damage,target,side) -> None:
        self.pos = pos
        self.side = side
        self.damage = damage
        self.target = target

class crate:
    def __init__(self,pos,level) -> None:
        pass

class steel_wall:
    def __init__(self,pos):
        self.pos = pos
        self.hp = 100

class picsteel_wall:
    def __init__(self,pos):
        self.pos = pos
        self.hp = None

map_hidders = []  
map_hidders_destroyed = []  
for i in range(22):
    for j in range(12):
        map_hidders.append(map_hidder([i*120-30,j*120-30]))
bullets = []
destroyed_bullets = []
walls = []
men = [pistol_soldier([2100,700],'m',12,(0,0,255))]
dead = []
buildings = [picbuildingfspsgen([2350,0]),picbuildingfspsgen([50,0])]
count = 0
money1 = 20000000
money2 = 20000000
clicked_on_fs_ps_gen = False
# die_sound = pygame.mixer.Sound()
# flame_sound = pygame.mixer.Sound()
shot_sound = pygame.mixer.Sound('/Users/cameroncheke/TotalControl/gunshot.mp3')
# n = 1
while True:
    
    shot_sound_first = True
    check_building=None
    count+=1
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            mouse = pygame.mouse.get_pos()
            for i in buildings:
                if i.pos[0] - mouse[0] > -175 and i.pos[0] - mouse[0] < 0 and i.pos[1] - mouse[1] > -175 and i.pos[1] - mouse[1] < 0 and money1 >= 50 and i.unittype==['fs','ps'] and i.side == 'm':
                    if event.key == pygame.K_f:
                        i.spawnfs = True
                        done = True
                        money1 -= 50
                        check_building = i
                    if event.key == pygame.K_p:
                        i.spawnps = True
                        done = True
                        money1 -= 50
                        check_building = i
            if event.key == pygame.K_k:
                men = []
        if event.type == pygame.MOUSEBUTTONDOWN: 
            
            clicked = pygame.mouse.get_pos()
            if clicked[0] > 2350 and clicked[0] < 2550 and clicked[1] > 0 and clicked[1] < 225 and money1 >= 300:
                done = False
                money1-=300
                while done == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            buildings.append(buildingfspsgen(pygame.mouse.get_pos(),'m',(0,0,255)))
                            done = True
            
            if clicked[0] > 0 and clicked[0] < 250 and clicked[1] > 0 and clicked[1] < 225 and money2 >= 300:
                done = False
                money2-=300
                while done == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            buildings.append(buildingfspsgen(pygame.mouse.get_pos(),'e',(255,0,0)))
                            done = True
            
            for i in men:
                if i.target == 'find':
                    i.target = clicked
                if i.pos[0] - clicked[0] > -75 and i.pos[0] - clicked[0] < 0 and i.pos[1] - clicked[1] > -75 and i.pos[1] - clicked[1] < 0  and i.side == 'm':
                    i.target = 'find'
    for i in buildings:
        if count%15==0 and money2 > 200 and i.side=='e':
            i.spawnfs = True
            check_building = i
            money2 -= 50
            if count%30==0 and money2 > 100 and i.side=='e':
                i.spawnps = True
                check_building = i
                money2 -= 50
    wn.blit(background,(0,0))
    for i in buildings:
        for j in men:
            if i.pos[0] - j.pos[0] > -175 and i.pos[0] - j.pos[0] < 0 and i.pos[1] - j.pos[1] > -175 and i.pos[1] - j.pos[1] < 0 and i.side != j.side and i.unittype!='pic':
                i.hp -= 1
                if i.hp <= 0:
                    i.side = j.side
                    i.hp = 150
                    i.color = j.color
                i.spawnfs = False
                i.spawnps = False
            # elif i.unittype != 'pic':
            #     if i.hp < 100:
            #         i.hp += 1

        wn.blit(i.fspsgen,i.pos)
        if i.side != None:
            pygame.draw.rect(wn,i.color,(i.pos[0],i.pos[1]-20,i.hp,10))
            pygame.draw.rect(wn,(0,0,0),(i.pos[0],i.pos[1]-20,150,10),width=1)
        if i.unittype==['fs','ps'] and i.spawnfs == True:
            men.append(flamethrower_soldier([i.pos[0]+100,i.pos[1]+150],i.side,12,i.color))
        if i.unittype==['fs','ps'] and i.spawnps == True:
            men.append(pistol_soldier([i.pos[0]+100,i.pos[1]+150],i.side,12,i.color))
            
        i.spawnfs = False
        i.spawnps = False
    count_for_men_place = 0
    cantattack = []
    for i in men:
        canshoot=True
        # if i.unittype=='ps' and count%7==0:
        #     i.move = True
        if i.target != 'find':
            dx = i.target[0] - i.pos[0]
            dy = i.target[1] - i.pos[1]
            distance = (dx**2 + dy**2)**0.5
            if distance <= i.speed:
                i.pos[0] = i.target[0]
                i.pos[1] = i.target[1]
            else:
                i.pos[0] += i.speed * dx / distance
                i.pos[1] += i.speed * dy / distance
        target_picked = False
        count_for_men_place2 = 0
        for j in men:
            pn1 = random.choice([-1,1])
            pn2 = random.choice([-1,1])
            if i.pos[0] - j.pos[0] > -30 and i.pos[0] - j.pos[0] < 30 and i.pos[1] - j.pos[1] > -30 and i.pos[1] - j.pos[1] < 30 and i != j and i.side == j.side:
                i.pos[0]=i.pos[0]+31*pn1
                i.pos[1]=i.pos[1]+31*pn2
                # i.originalpos[0]=i.originalpos[0]+31*pn1
                # i.originalpos[1]=i.originalpos[1]+31*pn1

            if i.pos[0] - j.pos[0] > -50 and i.pos[0] - j.pos[0] < 50 and i.pos[1] - j.pos[1] > -50 and i.pos[1] - j.pos[1] < 50 and i.side != j.side:
                if i.unittype == 'fs':
                    j.hp-=10
                    if j.hp > 0:
                        j.hpbar-=(50/j.originalhp)*10
                if j.hp <= 0:
                    dead.append(men.pop(count_for_men_place2))
            
            # dict1 = {}
            # for u in range(len(men)):
            #     if men[u].side != i.side:
            #         dict1[men[u].pos[0]+men[u].pos[1]] = [men[u]]
            # list1 = []
            # for u in dict1:
            #     list1.append(u)
            # closest_shot = dict1[min(list1)]

            # dict2 = {}
            # for u in range(len(men)):
            #     if men[u].side != i.side:
            #         dict2[men[u].pos[0]+men[u].pos[1]] = [men[u]]
            
            # for u in range(len(buildings)):
            #     if u.side != i.side:
            #         dict2[buildings[u].pos[0]+buildings[u].pos[1]] = [buildings[u]]
            #     list2 = []
            # for u in dict2:
            #     list2.append(u)
            # closestgoodguy = dict2[min(list2)]
                


            if cantattack != j and i.pos[0] - j.pos[0] > -500 and i.pos[0] - j.pos[0] < 500 and i.pos[1] - j.pos[1] > -500 and i.pos[1] - j.pos[1] < 100 and i.side != j.side and target_picked == False:
                if i.unittype == 'ps' and count%15 == 0:
                    if shot_sound_first == True:
                        shot_sound.play()
                        shot_sound_first = False
                    bullets.append(bullet([i.pos[0]+3,i.pos[1]+10],60,[j.pos[0]+20,j.pos[1]+20],i.side))
                    i.move = False
                    canshoot = False
                    cantattack=None
                    target_picked = True
            if i.side != 'm' and i.pos[0] - j.pos[0] > -700 and i.pos[0] - j.pos[0] < 700 and i.pos[1] - j.pos[1] > -700 and i.pos[1] - j.pos[1] < 700 and i.side != j.side and target_picked == False and i.move == True:
                target_picked = True
                dx = j.pos[0]-50 - i.pos[0]
                dy = j.pos[1]-50 - i.pos[1]
                distance = (dx**2 + dy**2)**0.5
                if distance <= i.speed:
                    pass
                    # i.originalpos[0] = j.pos[0]
                    # i.originalpos[1] = j.pos[1]
                else:
                    i.pos[0] += i.speed * dx / distance
                    i.pos[1] += i.speed * dy / distance
                    # i.originalpos[0] += 15 * dx / distance
                    # i.originalpos[0] += 15 * dx / distance

            if i.pos[0] - j.pos[0] > -100 and i.pos[0] - j.pos[0] < 100 and i.pos[1] - j.pos[1] > -100 and i.pos[1] - j.pos[1] < 100 and i.side != j.side and i.side == 'm' and target_picked == False and i.move == True:
                target_picked = True
                dx = j.pos[0] - i.pos[0]
                dy = j.pos[1] - i.pos[1]
                distance = (dx**2 + dy**2)**0.5
                if distance <= i.speed:
                    pass
                    # i.originalpos[0] = j.pos[0]
                    # i.originalpos[1] = j.pos[1]
                else:
                    i.pos[0] += i.speed * dx / distance
                    i.pos[1] += i.speed * dy / distance
            count_for_men_place2+=1
        # if count%10 == 0:
        #     n*=-1
        # i.pos[0]+=n
        # i.pos[1]+=n
        pygame.draw.rect(wn,i.color,(i.pos[0],i.pos[1]-20,i.hpbar,10))
        pygame.draw.rect(wn,(0,0,0),(i.pos[0],i.pos[1]-20,50,10),width=1)
        
        wn.blit(i.im,i.pos)
        if i.hp <= 0:
            dead.append(men.pop(count_for_men_place))
        count_for_men_place+=1
    
    count_for_bullet_place=0
    if len(bullets)!=0:    
        for x in bullets:
            pygame.draw.circle(wn,(255,255,0),x.pos,4)
            if (x.pos[0], x.pos[1]) != (x.target[0], x.target[1]):
                dx = x.target[0] - x.pos[0]
                dy = x.target[1] - x.pos[1]
                distance = (dx**2 + dy**2)**0.5
                if distance <= 30:
                    bullets.pop(count_for_bullet_place)
                else:
                    x.pos[0] += 30 * dx / distance
                    x.pos[1] += 30 * dy / distance
            for y in men:
                if x.pos[0] - y.pos[0] > 0 and x.pos[0] - y.pos[0] < 50 and x.pos[1] - y.pos[1] > 0 and x.pos[1] - y.pos[1] < 50 and x.side != y.side:
                    y.hp-=x.damage
                    if y.hp > 0:
                        y.hpbar-=(50/y.originalhp)*x.damage
        count_for_bullet_place+=1
    # which_to_disapear = []
    # for i in range(len(map_hidders)):
    #     for j in men:
    #         if j.pos[0] - map_hidders[i].pos[0] < 400 and j.pos[0] - map_hidders[i].pos[0] > -400 and j.pos[1] - map_hidders[i].pos[1] < 400 and j.pos[1] - map_hidders[i].pos[1] > -400 and j.side == 'm':
    #             which_to_disapear.append(i)
    #     wn.blit(map_hidders[i].im,map_hidders[i].pos)
    pygame.display.flip()