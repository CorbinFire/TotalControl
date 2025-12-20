from imports import *
from classes import *
from definitions import *

pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
width,hieght = info.current_w,info.current_h
square_size = [width,width] if width < hieght else [hieght,hieght]
add_to_each_point = [0,(hieght-width)/2] if width < hieght else [(width-hieght)/2,0]
rightsidecoverpos = [0,(hieght+width)/2] if width < hieght else [(width+hieght)/2,0]
sidecoverplus = [width,(hieght-width)/2] if width < hieght else [(width-hieght)/2,hieght]
wn = pygame.display.set_mode([width,hieght],pygame.FULLSCREEN)

sidebar = sidebarclass(rightsidecoverpos+rightsidecoverpos/np.array([8,8]))
background1 = background(add_to_each_point)
p1units = [assault([300,300])]
clickspawn=None
Home = True
Main = False
Tutorial = False
Shop = False
while Home:
    time.sleep(0.001)
    Mouse = pygame.mouse
    Keys = pygame.key
    w = Keys.get_pressed()[pygame.K_w]
    a = Keys.get_pressed()[pygame.K_a]
    d = Keys.get_pressed()[pygame.K_d]
    s = Keys.get_pressed()[pygame.K_s]
    if w:
        background1.pos += np.array([0,square_size[0]*0.013])
    if a:
        background1.pos += np.array([square_size[0]*0.013,0])
    if d:
        background1.pos -= np.array([square_size[0]*0.013,0])
    if s:
        background1.pos -= np.array([0,square_size[0]*0.013])



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Home = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if within(sidebar.pos,sidebar.pos+sidebar.size,Mouse.get_pos()) and sidebar.index == 1:
                sidebar.index = (sidebar.index+1)%2
                sidebar.pos = sidebar.poses[sidebar.index]
                sidebar.size = sidebar.sizes[sidebar.index]
                sidebar.im = sidebar.ims[sidebar.index]

            elif within(sidebar.pos+sidebar.size-np.array(sidebar.size/np.array([1.4,5])), sidebar.pos+sidebar.size/np.array([1.4,1]),Mouse.get_pos()) and sidebar.index == 0:
                sidebar.index = (sidebar.index+1)%2
                sidebar.pos = sidebar.poses[sidebar.index]
                sidebar.size = sidebar.sizes[sidebar.index]
                sidebar.im = sidebar.ims[sidebar.index]

            elif clickspawn!=None:
                p1units+=[clickspawn(np.array(Mouse.get_pos())-add_to_each_point)]
                clickspawn=None

            elif within(sidebar.pos+sidebar.size*np.array([0,0.4]), sidebar.pos+sidebar.size*np.array([0,0.4])+sidebar.sizes[1]*np.array([1.85,1.5]), Mouse.get_pos()):
                clickspawn=sidebar.page[1][1]

            elif within(sidebar.pos+sidebar.size*np.array([0,0.15]), sidebar.pos+sidebar.size*np.array([0,0.15])+sidebar.sizes[1]*np.array([1.85,2]), Mouse.get_pos()):
                sidebar.pgindex = (sidebar.pgindex-1)%3
                sidebar.page = sidebar.pages[sidebar.pgindex]

            elif within(sidebar.pos+sidebar.size*np.array([0,0.15])+sidebar.sizes[1]*np.array([1.85,0]), sidebar.pos+sidebar.size*np.array([0,0.15])+sidebar.sizes[1]*np.array([3.7,2]), Mouse.get_pos()):
                sidebar.pgindex = (sidebar.pgindex+1)%3
                sidebar.page = sidebar.pages[sidebar.pgindex]




    wn.blit(background1.im, background1.pos)
    firstshift = True
    for unit in p1units:
        wn.blit(unit.im,unit.pos)
        pygame.draw.rect(wn,(255,0,0),[unit.pos[0]+unit.size[0]*0.1,unit.pos[1]-unit.size[1]*0.1,(unit.size[0]*0.8*unit.damage_multiplier*unit.health)/100,unit.size[1]*0.075])
        pygame.draw.rect(wn,(0,0,0),[unit.pos[0]+unit.size[0]*0.1,unit.pos[1]-unit.size[1]*0.1,unit.size[0]*0.8,unit.size[1]*0.075],int(round(unit.size[1]*0.015,0)))
        if w:
            unit.pos += np.array([0,square_size[0]*0.013])
        if a:
            unit.pos += np.array([square_size[0]*0.013,0])
        if d:
            unit.pos -= np.array([square_size[0]*0.013,0])
        if s:
            unit.pos -= np.array([0,square_size[0]*0.013])
    wn.fill((0,0,0),[0,0,sidecoverplus[0],sidecoverplus[1]])
    wn.fill((0,0,0),[rightsidecoverpos[0],rightsidecoverpos[1],sidecoverplus[0],sidecoverplus[1]])
    wn.blit(sidebar.im,sidebar.pos)
    if sidebar.index == 0:
        wn.blit(pygame.transform.scale(pygame.image.load(sidebar.page[1][0]),sidebar.sizes[1]),sidebar.pos+sidebar.size/np.array([8,2.3]))
        
    pygame.display.flip()