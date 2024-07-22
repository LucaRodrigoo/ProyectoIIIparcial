import random
import pygame
from pygame import mixer

pygame.init()

ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

pygame.display.set_caption("Bienvenido a Space Invaders")

puntuacion_valor = 0
puntuacionX = 5
puntuacionY = 5
fuente = pygame.font.Font('freesansbold.ttf', 20)

vidas = 3

nivel = 1

fuente_game_over = pygame.font.Font('freesansbold.ttf', 64)
fuente_terminado = pygame.font.Font('freesansbold.ttf', 40)

fuente_menu = pygame.font.Font('freesansbold.ttf', 32)
fuente_instrucciones= pygame.font.Font('freesansbold.ttf', 24)

mixer.music.load('proyecto_juego/data/background.wav')
mixer.music.play(-1)

imagenes_jugador = ['proyecto_juego/data/spaceship.png', 'proyecto_juego/data/spaceship2.png', 'proyecto_juego/data/spaceship3.png']
indice_imagen_jugador= 0
imagen_jugador = pygame.image.load(imagenes_jugador[indice_imagen_jugador])
jugadorX = 370
jugadorY = 523
jugador_Xcambio=0

imagen_invasor = []
invasor_X = []
invasor_Y = []
invasor_Xcambio = []
invasor_Ycambio = []
num_invasores = 8

for num in range(num_invasores):
    imagen_invasor.append(pygame.image.load('data/alien.png'))
    invasor_X.append(random.randint(64, 737))
    invasor_Y.append(random.randint(30, 180))
    invasor_Xcambio.append(0.3)
    invasor_Ycambio.append(40)

imagen_bala= pygame.image.load('data/bullet.png')
balaX = 0
balaY = 523
bala_Xcambio = 0
bala_Ycambio = 3
estado_bala = "reposo"