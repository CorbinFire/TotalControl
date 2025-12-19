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

    if Keys.get_pressed()[pygame.K_w]:
        background1.pos += np.array([0,20])
        for unit in p1units:
            unit.pos += np.array([0,20])
    if Keys.get_pressed()[pygame.K_a]:
        background1.pos += np.array([20,0])
        for unit in p1units:
            unit.pos += np.array([20,0])
    if Keys.get_pressed()[pygame.K_d]:
        background1.pos -= np.array([20,0])
        for unit in p1units:
            unit.pos -= np.array([20,0])
    if Keys.get_pressed()[pygame.K_s]:
        background1.pos -= np.array([0,20])
        for unit in p1units:
            unit.pos -= np.array([0,20])


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




    wn.blit(background1.im, background1.pos)
    for unit in p1units:
        wn.blit(unit.im,unit.pos)
    wn.fill((0,0,0),[0,0,sidecoverplus[0],sidecoverplus[1]])
    wn.fill((0,0,0),[rightsidecoverpos[0],rightsidecoverpos[1],sidecoverplus[0],sidecoverplus[1]])
    wn.blit(sidebar.im,sidebar.pos)
    if sidebar.index == 0:
        wn.blit(pygame.transform.scale(pygame.image.load(sidebar.page[1][0]),sidebar.sizes[1]),sidebar.pos+sidebar.size/np.array([8,2.3]))
    pygame.display.flip()