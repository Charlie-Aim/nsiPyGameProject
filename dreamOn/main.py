import pygame as p
import random
from utilities import *
from screens import *

captions = ["coucou nathan","calcules QUENTIN EN BASE 10","What the hell","meilleur qu'Undertale","connard"]
p.init()
p.display.set_caption(captions[random.randint(0,len(captions)-1)])
# ecran = p.display.set_mode()
ecran = p.display.set_mode(p.display.get_desktop_sizes()[0])
screenSize = ecran.get_size()

print(screenSize)

""" dans le menu:

    ecran = "title"
    running = true
    while running:
        match ecran:
            case "title":
                titlescreen()
            case "Bros":
                mariobros():
            case "rpg":
                rpg()
"""                    


def marioBros():
    classmethod
    class aurélien:
        rondoudou = True
    class testClass:
        xpos : float = 50
        ypos : float = 0
        direction : str = "Right"
        Xmomentum : float = 0
        Ymomentum : float = 0
        image : p.Surface = p.image.load(f"./images/sprites/playerIdle{direction}.png")
        image : p.Surface = p.transform.scale(image,(image.get_width()*6,image.get_width()*6))
        def move():
            testClass.xpos += testClass.Xmomentum
            testClass.ypos += testClass.Ymomentum
    direction = "Right"
    loadAndPlay("./sounds/Pamiromariothemev2.wav",-1)
    backGround = p.image.load("./images/backgrounds/marioBros1.png").convert()
    #player = p.transform.scale(p.image.load("./images/sprites/girl.png").convert_alpha(), (32*3,48*3))
    PlayerT = p.transform.scale(p.image.load(f"./images/sprites/playerIdle{direction}.png").convert_alpha(), (p.image.load(f"./images/sprites/playerIdle{direction}.png").get_width()*6,p.image.load(f"./images/sprites/playerIdle{direction}.png").get_height()*6))
    flag = p.transform.scale(p.image.load("./images/sprites/flag.png"),(100,100))
    xpos = 50
    ypos = 751 - PlayerT.get_height()
    backGroundxPos = 0
    continuer : bool = True
    acceleration : float = 0.01
    isMoving : list = [False]*2
    jumping = False
    yposTemp = ypos
    Xmomentum = 0
    Ymomentum = 0
    while continuer:
        PlayerT = p.transform.scale(p.image.load(f"./images/sprites/playerIdle{direction}.png").convert_alpha(), (p.image.load(f"./images/sprites/playerIdle{direction}.png").get_width()*6,p.image.load(f"./images/sprites/playerIdle{direction}.png").get_height()*6))

        debugQuit()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p.KEYDOWN:
                match event.key:
                    case p.K_LEFT:
                        isMoving[0] = True
                    case p.K_RIGHT:
                        isMoving[1] = True
                    case p.K_SPACE:
                        if ypos == yposTemp and not jumping:
                            jumping = True
                            Ymomentum -= 2.4
                            p.mixer.Sound.play(p.mixer.Sound("./sounds/jump.wav"))
                    case p.K_ESCAPE:
                        isMoving = [False, False]
                        pauseScreen()
                        # continuer = False
            elif event.type == p.KEYUP:
                match event.key:
                    case p.K_LEFT:
                        isMoving[0] = False
                    case p.K_RIGHT:
                        isMoving[1] = False
                    case p.K_SPACE:
                        if jumping:
                            jumping = False
                            Ymomentum = Ymomentum/2

        
        movementDirection = (isPressed(p.K_LEFT),isPressed(p.K_RIGHT))
        match movementDirection:
            case (True,False):
                if testClass.Xmomentum > -1:
                    testClass.Xmomentum -= 0.005
            case (False,True):
                if testClass.Xmomentum < 1:
                    testClass.Xmomentum += 0.005
            case _ :
                if -0.005 < testClass.Xmomentum < 0.005:
                    testClass.Xmomentum = 0
                else:
                    testClass.Xmomentum -= 0.001 * getSign(testClass.Xmomentum)


        if testClass.Xmomentum <= 0:
            testClass.xpos += testClass.Xmomentum
        else:
            if testClass.xpos < 650:
                testClass.xpos += testClass.Xmomentum
            else:
                if backGroundxPos > -11300:
                    backGroundxPos -= testClass.Xmomentum

        #n'oublie pas de faire en sorte que si ni right ni left ne sont préssés alor momentum = 0
        if isPressed(p.K_LEFT) and not isPressed(p.K_RIGHT):
            direction = "Left"
        elif isPressed(p.K_RIGHT) and not isPressed(p.K_LEFT):
            direction = "Right"
        if isPressed(p.K_LEFT) and xpos > 0 :
            xpos -= 1
        if isPressed(p.K_RIGHT):
            # if xpos < ecran.get_width()/2 - player.get_width()/2:
            #     
            if xpos < 650:
                xpos += 1
            else:
                if backGroundxPos > -11300:
                    backGroundxPos -= 1
        if isPressed(p.K_c) and isPressed(p.K_a):
            backGroundxPos = -10000
        # if verticalMomentum < 0:
        #     verticalMomentum = 0
        # else:
        #     verticalMomentum -= 0.005

        actext = font1.render(str(acceleration),0,(255,255,255))
        # if ypos + player.get_height() < 751 and not jumping:
        Ymomentum += 0.01
        if ypos + PlayerT.get_height() >= 751 and not jumping:
            Ymomentum = 0
            yposTemp = ypos
        ypos += Ymomentum

            

        if backGroundxPos < -11350:
            print(backGroundxPos)
        ecran.blit(backGround, (backGroundxPos,0))
        ecran.blit(flag,(11375 + backGroundxPos,175))
        ecran.blit(PlayerT, (xpos,ypos))
        momentext = font1.render(str(Xmomentum),0,(255,255,255,100))
        ecran.blit(p.transform.scale(momentext,(momentext.get_width()/10,momentext.get_height()/10)),(20,20))
        ecran.blit(p.transform.scale(actext,(actext.get_width()/10,actext.get_height()/10)),(20,50))
        if backGroundxPos + 11575 <= ecran.get_width()/2:
            continuer = False
            gagné = True
        p.display.flip()
    flagYpos = 175

    if gagné:
        p.time.delay(1000)
        bowser = p.transform.scale_by(p.image.load("./images/sprites/bowser1.png"),5.5)
        bowserPos = [ecran.get_width()*0.75,-1000]
        acceleration = 0
        p.mixer.music.stop()
        p.time.delay(1)
        p.mixer.Sound.play(p.mixer.Sound("./sounds/downTheFlag.wav"))
        while flagYpos < 575:
            flagYpos += 0.65
            if ypos <= 695 - PlayerT.get_height():
                ypos += 1
            ecran.blit(backGround, (backGroundxPos,0))
            ecran.blit(flag,(11375 + backGroundxPos,flagYpos))
            ecran.blit(PlayerT,(xpos,ypos))
            p.display.flip()
        p.mixer.Sound.play(p.mixer.Sound("./sounds/stageEnd.wav"))

        
        while ypos + PlayerT.get_height() < 751:
            acceleration += 0.01
            ypos += acceleration
            xpos += 0.7
            ecran.blit(backGround, (backGroundxPos,0))
            ecran.blit(flag,(11375 + backGroundxPos,flagYpos))
            ecran.blit(PlayerT,(xpos,ypos))
            p.display.flip()
        p.time.delay(int(p.mixer.Sound.get_length(p.mixer.Sound("./sounds/stageEnd.wav"))*1000))
        while bowserPos[1] < 751 - bowser.get_height():
            bowserPos[1] += 3
            ecran.blit(backGround,(backGroundxPos,0))
            ecran.blit(PlayerT,(xpos,ypos))
            ecran.blit(flag,(11375 + backGroundxPos,flagYpos))
            ecran.blit(bowser,bowserPos)

            p.display.flip()
        p.time.delay(1700)
        bowser = p.transform.scale_by(p.image.load("./images/sprites/bowserSceptical.png"),5.5)
        ecran.blit(backGround,(backGroundxPos,0))
        ecran.blit(bowser,bowserPos)
        p.display.flip()
        p.time.delay(2000)



# textbox("TEST")
running : str = "title"
while True:
    match running:
        case "title":
            running = titleScreen(ecran)
        case "mario":
            marioBros()
        case "quit":
            break
p.quit()



# si jump:
#   yVelocity -= 5
#boucle qui s'itère quoi qu'il arrive:
#   ypos += yVelocity
#   yVelocity += 0.05

