import pygame as p
import random
from utilities import *
p.init()
backScreen = p.surface.Surface((1920,1080))
font = p.font.Font('./fonts/guardener.ttf', 300)
font1 = p.font.Font('./fonts/guardener.ttf', 200)

def titleScreen(screen) -> str:
    # cloud = p.transform.scale(p.image.load("./images/sprites/cloud.png").convert_alpha(),(300,150))

    title = font.render("Pamiro",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    #(240,200,160)
    undertaleLogo = p.transform.scale(p.image.load("./images/sprites/undertale.png").convert_alpha(),(850,350))
    backScreen = p.surface.Surface((1920,1080))
    undertaleIntroSound = p.mixer.Sound("./sounds/undertaleIntro.wav")
    undertaleIntroSound.set_volume(70)


    OnTitle : bool = True
    p.time.delay(1500)
    p.mixer.Sound.play(undertaleIntroSound)

    screen.blit(undertaleLogo,(putAtCenter(screen,undertaleLogo),100))
    p.display.flip()

    p.time.delay(int((p.mixer.Sound.get_length(undertaleIntroSound) -2)*1000))
    p.mixer.Sound.stop(undertaleIntroSound)

    p.mixer.Sound.play(p.mixer.Sound("./sounds/fart.wav"))

    p.draw.rect(screen,(0,0,0), p.Rect(0,0,1920,1080))
    screen.blit(title,(putAtCenter(screen,title),80))
    p.display.flip()

    p.time.delay(2200)
    loadAndPlay("./sounds/titleMusic.wav",-1)

    cloudData : list = [[random.randint(0,2500),random.randint(0,800),random.uniform(1,3),random.uniform(0.65,1.35),random.randint(0,2)] for i in range(8)]
    title.set_alpha(200)
    while OnTitle:
        debugQuit()
        p.draw.rect(screen,(100,150,255), p.Rect(0,0,1920,1080))
        for el in cloudData:
            cloud = p.transform.scale(p.image.load(f"./images/sprites/cloud{el[4]}.png").convert_alpha(),(300,150))
            if el[0] <= -(el[2] * cloud.get_width()):
                el[0] = random.randint(1500,3000)
                el[1] = random.randint(0,800)
            else:
                el[0] -= el[3]
            screen.blit(p.transform.scale(cloud,(cloud.get_width()*el[2],cloud.get_height()*el[2])),(el[0],el[1]))
        screen.blit(title,(putAtCenter(screen,title),80))
        p.display.flip()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    OnTitle = False
                    backScreen.set_alpha(0)
                    p.mixer.music.fadeout(500)
                    for i in range(50):
                        p.time.delay(10)
                        backScreen.set_alpha(backScreen.get_alpha() + 1)
                        screen.blit(backScreen,(0,0))
                        p.display.flip()
                    p.time.delay(500)
                    return "mario"
                elif event.key == p.K_F4:
                    return "mario"
        if isPressed(p.K_LEFT):
            print("ton code marche\n")

def pauseScreen(screen):
    pause = True
    pauseTitle = font.render("Pause",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    backScreen.set_alpha(200)
    screen.blit(backScreen,(0,0))
    screen.blit(pauseTitle,(putAtCenter(screen,pauseTitle),100))
    p.display.flip()
    p.mixer.pause()
    p.mixer.music.pause()
    p.mixer.Sound.play(p.mixer.Sound("./sounds/pause.wav"))
    while pause:
        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.mixer.unpause()
                    p.mixer.music.unpause()
                    pause = False