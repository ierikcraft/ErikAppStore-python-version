import pygame
import sys

# 1. Inicialización de Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Primer Juego en Pygame")

# 3. Colores (R, G, B)
NEGRO = (0, 0, 0)  # Para borrar la pantalla

# 4. Cargar la imagen del jugador
# Asegúrate de tener un archivo 'personaje.png' en la misma carpeta
try:
    jugador_img = pygame.image.load("bugs.jpg")
except FileNotFoundError:
    # Si no encuentran la imagen, creamos un cuadrado verde de respaldo
    jugador_img = pygame.Surface((50, 50))
    jugador_img.fill((0, 255, 0)) 

# Obtenemos el rectángulo (hitbox) de la imagen para manejar coordenadas
jugador_rect = jugador_img.get_rect()
jugador_rect.center = (ANCHO // 2, ALTO // 2) # Posición inicial centro

# 5. Variables de movimiento
velocidad = 5

# 6. Control de FPS (Cuadros por segundo)
reloj = pygame.time.Clock()

# ---------------------------------------------------------
# BUCLE PRINCIPAL DEL JUEGO
# ---------------------------------------------------------
ejecutando = True
while ejecutando:
    # A. Manejo de Eventos (Inputs)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # B. Lógica de control (Teclado)
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador_rect.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_rect.x += velocidad
    if teclas[pygame.K_UP]:
        jugador_rect.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_rect.y += velocidad

    # C. Dibujado en pantalla
    pantalla.fill(NEGRO)  # 1. Limpiamos el frame anterior
    pantalla.blit(jugador_img, jugador_rect) # 2. Dibujamos al jugador
    
    # 3. Actualizamos la ventana para que el usuario vea los cambios
    pygame.display.flip()

    # D. Control de velocidad del bucle
    reloj.tick(60)  # Limitamos a 60 FPS

# Salir limpiamente
pygame.quit()
sys.exit()
