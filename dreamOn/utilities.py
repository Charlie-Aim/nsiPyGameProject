import pygame as p

def debugQuit():
    """
    Eteint le jeu quand la combinaison shift + ctrl + space sont presses

    params :
        aucun
    
    returns :
        None
    """
    keys = p.key.get_pressed()
    if keys[p.K_LSHIFT] and keys[p.K_LCTRL] and keys[p.K_SPACE]:
        p.quit()

def putAtCenter(s,a) -> float  :
    """
    Retourne la position de l'image pour laquelle cette derniere est affichee centre d'une surface donnee

    params :
        s : surface sur laquelle est affichee l'image
        a : image affichee
    
    returns :
        float : la position adequate de l'image
    """
    return s.get_width()/2 - a.get_width()/2

def loadAndPlay(m : str, l : int):
    """
    Charge et joue une musique avec un nombre d'iterations donnees

    params :
        m : chaine de caracteres correspondant au chemin d'acces au fichier de la musique
        l : entier correspondant au nombre d'iterations
    
    returns :
        None
    """
    p.mixer.music.load(m)
    p.mixer.music.play(l)

def isPressed(k) -> bool  :
    """
    Renvoie un booleen indiquant la pression ou non d'une touche donnee

    params :
        k : touche dont on verifie la pression
    
    returns :
        bool : True si la touche correspondant a k est pressee, sinon False
    """
    keys = p.key.get_pressed()
    return keys[k]

def aniMove(obj:dict,oPos:tuple,desPos:float,time:float):
    originalPos = oPos
    
def absoluteValue(num : float) -> float :
    return (num**2)**1/2

def getSign(num :float) -> float :
    return num / absoluteValue(num)