# ---------
# CONSTANTS
# ---------

# --- PIXELS ---
WIDTH = 600
HEIGHT = 600

BOARD_ROWS = 3  # Nombre de lignes du plateau
BOARD_COLS = 3  # Nombre de colonnes du plateau
SQUARE_SIZE = WIDTH // BOARD_COLS  # Taille d'une case du plateau

LINE_WIDTH = 15  # Épaisseur des lignes du plateau
CIRCLE_WIDTH = 15  # Épaisseur du cercle
CROSS_WIDTH = 25  # Épaisseur de la croix

CIRCLE_RADIUS = SQUARE_SIZE // 3  # Rayon du cercle

SPACE = SQUARE_SIZE // 4  # Espace entre les traits des croix et les bords des cases

# --- COLORS ---

BLACK = (66,66,66)  # Couleur noire pour les croix et les textes
BG_COLOR = (200,160,230)  # Couleur de fond du plateau
LINE_COLOR = (170,140,210)  # Couleur des lignes du plateau
CIRCLE_COLOR = (239,231,200)  # Couleur des cercles (joueur 1)
CROSS_COLOR = (66,66,66)  # Couleur des croix (joueur 2)