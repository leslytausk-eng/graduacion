import pgzrun
import random

WIDTH = 1080 # Anchura de la ventana
HEIGHT = 1080 # Altura de la ventana

TITLE = "El nombre de su juego" # Título de su proyecto de juego
FPS = 30 # Número de fotogramas por segundo



def draw():
    screen.clear()
    screen.blit("menu",(0,0))

pgzrun.go()