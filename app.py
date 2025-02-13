import pygame

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (180, 180, 255)
DARK_BLUE = (50, 50, 150)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Virtuel")

# Chargement des sons
notes = {
    pygame.K_a: ("c1.wav", "C1", "white", 0),
    pygame.K_z: ("c1s.wav", "C#1", "black", 0),
    pygame.K_s: ("d1.wav", "D1", "white", 1),
    pygame.K_e: ("d1s.wav", "D#1", "black", 1),
    pygame.K_d: ("e1.wav", "E1", "white", 2),
    pygame.K_f: ("f1.wav", "F1", "white", 3),
    pygame.K_t: ("f1s.wav", "F#1", "black", 2),
    pygame.K_g: ("g1.wav", "G1", "white", 4),
    pygame.K_y: ("g1s.wav", "G#1", "black", 3),
    pygame.K_h: ("a1.wav", "A1", "white", 5),
    pygame.K_u: ("a1s.wav", "A#1", "black", 4),
    pygame.K_j: ("b1.wav", "B1", "white", 6),
    pygame.K_k: ("c2.wav", "C2", "white", 7)
}

# Création des touches
white_keys = [(50 + i * 60, 50, 60, 200) for i in range(8)]
black_keys = [(95 + i * 60, 50, 40, 120) for i in range(5)]

pressed_white_keys = set()
pressed_black_keys = set()

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)
    
    # Dessin des touches blanches
    for i, (x, y, w, h) in enumerate(white_keys):
        color = BLUE if i in pressed_white_keys else WHITE
        pygame.draw.rect(screen, color, (x, y, w, h))
        pygame.draw.rect(screen, BLACK, (x, y, w, h), 2)
    
    # Dessin des touches noires
    for i, (x, y, w, h) in enumerate(black_keys):
        color = DARK_BLUE if i in pressed_black_keys else BLACK
        pygame.draw.rect(screen, color, (x, y, w, h))
        pygame.draw.rect(screen, BLACK, (x, y, w, h), 2)
    
    # Affichage des touches jouées
    y_offset = 10
    font = pygame.font.Font(None, 36)
    for key in pressed_white_keys.union(pressed_black_keys):
        for k, v in notes.items():
            if v[3] == key:
                text_surface = font.render(v[1], True, BLACK)
                screen.blit(text_surface, (650, y_offset))
                y_offset += 40
                break
    
    pygame.display.flip()
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in notes:
                sound_file, note_name, key_type, index = notes[event.key]
                pygame.mixer.Sound(sound_file).play()
                if key_type == "white":
                    pressed_white_keys.add(index)
                else:
                    pressed_black_keys.add(index)
        elif event.type == pygame.KEYUP:
            if event.key in notes:
                _, _, key_type, index = notes[event.key]
                if key_type == "white":
                    pressed_white_keys.discard(index)
                else:
                    pressed_black_keys.discard(index)

pygame.quit()