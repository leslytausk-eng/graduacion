import pgzrun
import random

WIDTH = 1080 # Anchura de la ventana
HEIGHT = 1080 # Altura de la ventana

TITLE = "El nombre de su juego" # Título de su proyecto de juego
FPS = 30 # Número de fotogramas por segundo
button_play = Actor("btnplay", (320,200))
mode = "menu"

def draw():
    
    if mode == "menu":
        screen.clear()
        screen.blit("menu", (0,0))
        button_play.draw()
    elif mode == "game":
        screen.clear()
        screen.blit("bg", (0,0))

def on_mouse_down(pos):
    global mode
    if mode == "menu":
        if button_play.collidepoint(pos):
            mode = "game"

pgzrun.go()
