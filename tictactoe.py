# Importation des modules nécessaires
import pygame, sys  # Utilisé pour les éléments graphiques, sys pour quitter le programme
import numpy as np  # Utilisé pour manipuler le tableau de jeu

# Importation des constantes pour les dimensions, les couleurs, etc.
from constants import *

# --- CONFIGURATION DE PYGAME ---

pygame.init()  # Initialise tous les modules Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Création de la fenêtre du jeu
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# Initialisation du tableau de jeu (plateau de 3x3, rempli de zéros)
board = np.zeros((BOARD_ROWS, BOARD_ROWS))

# Fonction pour dessiner les lignes du plateau
def draw_lines():
    # Première ligne horizontale
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # Deuxième ligne horizontale
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Première ligne verticale
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # Deuxième ligne verticale
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Fonction pour dessiner les figures (cercles et croix) sur le plateau
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # Si la case est marquée par un cercle
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:  # Si la case est marquée par une croix
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Fonction pour marquer une case (1 pour cercle, 2 pour croix)
def mark_square(row, col, player):
    board[row][col] = player

# Fonction pour vérifier si une case est disponible
def available_square(row, col):
    return board[row][col] == 0

# Fonction pour vérifier si le plateau est plein
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:  # Si une case est vide, le plateau n'est pas plein
                return False
    return True

# Fonction pour vérifier si un joueur a gagné
def check_win(player):
    # Vérification des colonnes pour une victoire
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)  # Dessine la ligne de victoire
            return True
        
    # Vérification des lignes pour une victoire
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
        
    # Vérification de la diagonale ascendante
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_winning_diagonal(player)
        return True
    
    # Vérification de la diagonale descendante
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    
    return False

# Fonction pour dessiner une ligne verticale en cas de victoire
def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

# Fonction pour dessiner une ligne horizontale en cas de victoire
def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

# Fonction pour dessiner une diagonale ascendante en cas de victoire
def draw_asc_winning_diagonal(player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

# Fonction pour dessiner une diagonale descendante en cas de victoire
def draw_desc_diagonal(player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

# Fonction pour redémarrer le jeu (réinitialiser le plateau)
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()  # Dessine les lignes au début du jeu
player = 1  # Le joueur 1 commence (cercles)
game_over = False  # Statut du jeu, à vrai si la partie est terminée

# Fonction pour afficher l'écran de fin de jeu (gagnant ou match nul)
def display_end_screen(player):
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 60)
    small_font = pygame.font.Font(None, 40)
    
    if player == 1 or player == 2:  # Si un joueur a gagné
        text_message = font.render("Winner!", True, BLACK)
        screen.blit(text_message, (WIDTH // 2 - text_message.get_width() // 2, HEIGHT // 2 + 50))
        if player == 1:
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH // 2, HEIGHT // 2 - 30), CIRCLE_RADIUS, CIRCLE_WIDTH)
        elif player == 2:
            pygame.draw.line(screen, CROSS_COLOR, (WIDTH // 2 - SQUARE_SIZE // 2 + SPACE, HEIGHT // 2 - 30 + SQUARE_SIZE // 2 - SPACE),
                             (WIDTH // 2 + SQUARE_SIZE // 2 - SPACE, HEIGHT // 2 - 30 - SQUARE_SIZE // 2 + SPACE), CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOR, (WIDTH // 2 - SQUARE_SIZE // 2 + SPACE, HEIGHT // 2 - 30 - SQUARE_SIZE // 2 + SPACE),
                             (WIDTH // 2 + SQUARE_SIZE // 2 - SPACE, HEIGHT // 2 - 30 + SQUARE_SIZE // 2 - SPACE), CROSS_WIDTH)

        # Affiche les instructions "Press 'R' to Restart" et "Press 'Q' to Quit"
        text_restart = small_font.render("Press 'R' to Restart", True, BLACK)
        text_quit = small_font.render("Press 'Q' to Quit", True, BLACK)
        # Affiche le texte centré sur l'écran 
        screen.blit(text_restart, (WIDTH // 2 - text_restart.get_width() // 2, HEIGHT // 2 + 100))  # Rapproche encore
        screen.blit(text_quit, (WIDTH // 2 - text_quit.get_width() // 2, HEIGHT // 2 + 140))  # Rapproche encore

    else:  # Affichage en cas de match nul
        text_message = font.render("Game Over", True, BLACK)
            # Affiche "Game Over" au centre de l'écran
        screen.blit(text_message, (WIDTH // 2 - text_message.get_width() // 2, HEIGHT // 2 + 50))


        # Dessine un cercle à gauche pour représenter l'égalité
        pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH // 2 - 80, HEIGHT // 2 - 50), CIRCLE_RADIUS - 15, CIRCLE_WIDTH)  # Réduit le rayon et déplace plus haut

        # Dessine une croix à droite du cercle pour représenter l'égalité
        pygame.draw.line(screen, CROSS_COLOR, (WIDTH // 2 + 80 - SQUARE_SIZE // 2 + SPACE, HEIGHT // 2 - 50 - SQUARE_SIZE // 2 + SPACE), 
                         (WIDTH // 2 + 80 + SQUARE_SIZE // 2 - SPACE, HEIGHT // 2 - 50 + SQUARE_SIZE // 2 - SPACE), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (WIDTH // 2 + 80 - SQUARE_SIZE // 2 + SPACE, HEIGHT // 2 - 50 + SQUARE_SIZE // 2 - SPACE), 
                         (WIDTH // 2 + 80 + SQUARE_SIZE // 2 - SPACE, HEIGHT // 2 - 50 - SQUARE_SIZE // 2 + SPACE), CROSS_WIDTH)

        # Afficher les instructions pour redémarrer ou quitter
        text_restart = small_font.render("Press 'R' to Restart", True, BLACK)
        text_quit = small_font.render("Press 'Q' to Quit", True, BLACK)
        screen.blit(text_restart, (WIDTH // 2 - text_restart.get_width() // 2, HEIGHT // 2 + 100))
        screen.blit(text_quit, (WIDTH // 2 - text_quit.get_width() // 2, HEIGHT // 2 + 140))

# Mainloop
while True:
    # Parcourt tous les événements possibles
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            sys.exit()

        # Si un clic de souris est détecté
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # Coordonnée x
            mouseY = event.pos[1]  # Coordonnée y

            clicked_row = int(mouseY // SQUARE_SIZE) # Calcule la ligne cliquée
            clicked_col = int(mouseX // SQUARE_SIZE) # Calcule la colonne cliquée

            # Si la case cliquée est libre
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player) # Marque la case avec le joueur actuel
                if check_win(player): # Vérifie si le joueur a gagné
                    game_over = True # Indique que la partie est terminée
                    winner_message = player  # Enregistre le joueur gagnant (1 pour cercle, 2 pour croix)
                elif is_board_full():  # Vérifie si toutes les cases sont remplies (match nul)
                    game_over = True # Indique que la partie est terminée
                    winner_message = "Game Over"  # Aucun gagnant (un match nul)
                player = player % 2 + 1 # Change de joueur (1 ou 2)

                draw_figures() # Redessine les figures (croix ou cercle) sur le plateau

        # Si une touche est appuyée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False # Réinitialise l'état de fin de partie

            if event.key == pygame.K_q:
                quit()

    if game_over:
        display_end_screen(winner_message)  # Affiche l'écran de fin de partie (victoire ou match nul)

    pygame.display.update() # Rafraîchit l'écran pour refléter les changements