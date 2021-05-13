import pygame   # externa

# inicializar juego
pygame.init()
# configuracion de pantalla de juego
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego")
# cargar imagenes
ball = pygame.image.load("img/ball.png")
ballrect = ball.get_rect()
bar = pygame.image.load("img/bar.png")
barrect = bar.get_rect()
# movimiento
speed = [1, 1]
# control del cicle
run = True
barrect.move_ip(400, 260)
while run:
    pygame.time.delay(2)
    # verificar si se cerro
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # deteccion de teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        barrect = barrect.move(0, 1)
    if keys[pygame.K_UP]:
        barrect = barrect.move(0, -1)
    
    # mover pelotita
    ballrect = ballrect.move(speed)
    # detectar colision
    if ballrect.top < 0 or ballrect.bottom > 600:
        speed[1] = -speed[1] 
    if ballrect.left < 0 or ballrect.right > 800:
        speed[0] = -speed[0]
    if (barrect.colliderect(ballrect)):
        speed[0] = -speed[0]
    # mostrar imagenes
    white = (255, 255, 255)
    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(bar, barrect)
    pygame.display.flip()

pygame.quit()

