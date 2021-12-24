import pygame

pygame.init()

pygame.mixer.music.load('sample.mp3')

while True:
    command = input('play:p, pause:pp, unpause:up, stop:s, quit:q > ')
    if command == 'p':
        pygame.mixer.music.play()
    elif command == 'pp':
        pygame.mixer.music.pause()
    elif command == 'up':
        pygame.mixer.music.unpause()
    elif command == 's':
        pygame.mixer.music.stop()
    elif command == 'q':
        break
    else:
        print('incorrect command')