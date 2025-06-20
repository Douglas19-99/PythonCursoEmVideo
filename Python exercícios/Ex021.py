import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("musica_animada_10s.mp3")
pygame.mixer.music.play()

# Espera até a música terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Somente desse jeito funcionou tocar musica em mp3 no python 3.13.5
