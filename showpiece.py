import pygame
import math


class HexagonalCalendarWithPiece:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 800
        self.HEX_SIZE = 40
        self.CENTER_X = self.WIDTH // 2
        self.CENTER_Y = self.HEIGHT // 2
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.Font(None, 20)
        pygame.display.set_caption("Calendrier avec PiÃ¨ce")

        # Definition des pieces et leurs positions
        self.pieces = {
            1: [  # PiÃ¨ce 1 avec ses deux positions triangle
                [(-1, 0), (0, 0), (1, 0), (0, -1), (1, -1), (1, -2)],
                [(0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (2, -1)],
            ],
            2: [  # Piece 2 avec sa position unique barre
                [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
                [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)],
                [(-1, 1), (-2, 2), (0, 0), (1, -1), (2, -2)],
            ],
            # 3: [
            #     [(-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)],
            #     [(1, 0), (0, 0), (-1, 0), (2, -1), (1, -1), (0, -1)], # Rotation 0° retournée

            #     [(0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, -2)],  # Rotation 60°
            #     [(0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)],  # Retournée + 60°

            #     [(-2, 2), (0, 0), (-1, 1), (1, 0), (0, 1), (-1, 2)], # Rotation 120°
            #     [(1, -1), (0, 0), (-1, 1), (1, 0), (0, 1), (-1, 2)]       # Retournée + 120°
            # ],
            3: [
                # Rotation 0° (identité)
                [(-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, 0), (-1, 1), (-1, 2)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (0, -1), (-1, 0), (-2, 1)],
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (1, -1), (0, -1), (-1, -1)],
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (1, 0), (1, -1), (1, -2)],
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (0, 1), (1, 0), (2, -1)],
                #inverse
                # Rotation 0° (position initiale)
                [(1, 0), (0, 0), (-1, 0), (2, -1), (1, -1), (0, -1)],
                # Rotation 60°
                [(0, 1), (0, 0), (0, -1), (1, 1), (1, 0), (1, -1)],
                # Rotation 120°
                [(-1, 1), (0, 0), (1, -1), (-1, 2), (0, 1), (1, 0)],
                # Rotation 180°
                [(-1, 0), (0, 0), (1, 0), (-2, 1), (-1, 1), (0, 1)],
                # Rotation 240°
                [(0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)],
                # Rotation 300°
                [(1, -1), (0, 0), (-1, 1), (1, -2), (0, -1), (-1, 0)]
            ],
            4: [
                # Rotation 0° (Position initiale)
                [(-2, 0), (-1, 0), (0, 0), (1, 0), (1, 1)],      # Position initiale
                [(2, 0), (1, 0), (0, 0), (-1, 0), (-2, 1)],      # Retournée initiale
                
                # Rotation 60°
                [(0, -2), (0, -1), (0, 0), (0, 1), (-1, 2)],      # Rotation 60°
                [(0, -2), (0, -1), (0, 0), (0, 1), (-1, -2)],     # Retournée + 60°
                
                # Rotation 120°
                [(-1, 1), (-2, 1), (0, 0), (1, -1), (2, -2)],    # Rotation 120°
                [(-1, 1), (1, -2), (0, 0), (1, -1), (-2, 2)],     # Retournée + 120°
                
                # Rotation 180°
                [(2, 0), (1, 0), (0, 0), (-1, 0), (-1, -1)],     # Rotation 180°
                [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, -1)],     # Retournée + 180°
                
                # Rotation 240°
                [(0, 2), (0, 1), (0, 0), (0, -1), (1, -2)],      # Rotation 240°
                [(0, 2), (0, 1), (0, 0), (0, -1), (1, 2)],       # Retournée + 240°
                
                # Rotation 300°
                [(1, -1), (2, -1), (0, 0), (-1, 1), (-2, 2)],    # Rotation 300°
                [(1, -1), (-1, 2), (0, 0), (-1, 1), (2, -2)],    # Retournée + 300°
            ],

            5: [
                # Positions normales
                [(-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1)],       # Position initiale
                [(0, -1), (0, 0), (0, 1), (1, -1), (1, 0)],       # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, -0), (-1, 1)],       # Rotation 120° (corrigée)
    
                # Positions retournées
                [(-1, 0), (0, 0), (1, 0), (0, -1), (1, -1)],        # Retournée initiale
                [(-1, 1), (0, 0), (0, 1), (1, -1), (1, 0)],      # Retournée + 60°
                [(-1, 1), (0, 0), (0, 1), (-1, 2), (1, 0)],          # Retournée + 120° (corrigée)
            ],

            6: [
                # Positions normales
                [(0, -1), (0, 0), (1, -1), (-1, 1), (0, 1)],      # Position initiale
                [(1, -1), (0, 0), (1, 0), (-1, 0), (-1, 1)],      # Rotation 60°
                [(0, -1), (0, 0), (1, 0), (0, 1), (-1, 0)],     # Rotation 120°
            ],
            7: [
                # Rotation 0° (Position initiale)
                [(-1, 0), (0, 0), (1, 0), (1, 1), (2, 1)],
                [(-1, 0), (0, 0), (1, 0), (2, -1), (3, -1)], #Rotation 0° Retourne
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, 2), (-1, 3)],
                [(0, -1), (0, 0), (0, 1), (1, 1), (1, 2)],  # 60°  (appliquée : (q, r) -> (-r, q+r))
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (-2, 1), (-3, 2)],
                [(1, -1), (0, 0), (-1, 1), (-1, 2), (-2, 3)],# 120° (60° appliquée deux fois)
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (-1, -1), (-2, -1)],
                [(1, 0), (0, 0), (-1, 0), (-2, 1), (-3, 1)], # 180° (équivalent à (q, r) -> (-q, -r))
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (1, -2), (1, -3)],
                [(0, 1), (0, 0), (0, -1), (-1, -1), (-1, -2)], # 240° (rotation 180° + 60° supplémentaire)
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (2, -1), (3, -2)], 
                [(-1, 1), (0, 0), (1, -1), (1, -2), (2, -3)]  #retoune
            ],
            8: [
                # Rotation 0°
                [(-1, 0), (0, 0), (1, 0), (2, -1), (-2, 1)],
                #retouner
                [(1, 0), (0, 0), (-1, 0), (-1, -1), (1, 1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (1, 1), (-1, -1)],
                # Rotation 60° retouner
                [(0,1), (0,0), (0,-1), (1,-2), (-1,2)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (-1, 2), (1, -2)],
                # Rotation 120° retouner
                [(1, -1), (0, 0), (-1, 1), (-2, 1), (2, -1)],
            ],
            9: [
                # Rotation 0° (identité)
                [(-1, 0), (0, 0), (1, 0), (1, 1), (1, 2)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, 2), (-2, 3)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (-2, 1), (-3, 1)],
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (-1, -1), (-1, -2)],
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (1, -2), (2, -3)],
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (2, -1), (3, -1)]
            ],
            10: [
                # Rotation 0° (position initiale)
                [(-1, 0), (0, 0), (1, 0), (-1, 1), (-2, 1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, 0), (-1, -1)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (0, -1), (1, -2)],
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (1, -1), (2, -1)],
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (1, 0), (1, 1)],
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (0, 1), (-1, 2)],
                #Il faut retouner la piece mainteannt
                # Rotation 0° (position initiale)
                [(-1, 0), (0, 0), (1, 0), (0, -1), (-1, -1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (1, -1), (1, -2)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (1, 0), (2, -1)],
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (0, 1), (1, 1)],
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (-1, 1), (-1, 2)],
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (-1, 0), (-2, 1)]
            ],
            11: [
                # Rotation 0° (identité)
                [(-1, 0), (0, 0), (1, 0), (-1, 1), (-2, 1), (-3, 1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, 0), (-1, -1), (-1, -2)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (0, -1), (1, -2), (2, -3)],
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (1, -1), (2, -1), (3, -1)],
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (1, 0), (1, 1), (1, 2)],
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (0, 1), (-1, 2), (-2, 3)],
                #retouner
                 # Rotation 0° (identité)
                [(-1, 0), (0, 0), (1, 0), (0, -1), (-1, -1), (-2, -1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (1, -1), (1, -2), (1, -3)],
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (1, 0), (2, -1), (3, -2)],
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (0, 1), (1, 1), (2, 1)],
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (-1, 1), (-1, 2), (-1, 3)],
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (-1, 0), (-2, 1), (-3, 2)]
            ],
        }
        self.current_piece = 1
        self.current_position = 0
        self.piece = self.pieces[self.current_piece][self.current_position]

    def draw_hexagon(self, x, y, size, color, q, r):
        points = []
        for i in range(6):
            angle_deg = 60 * i + 30
            angle_rad = math.pi / 180 * angle_deg
            point_x = x + size * math.cos(angle_rad)
            point_y = y + size * math.sin(angle_rad)
            points.append((point_x, point_y))
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, (100, 100, 100), points, 2)

        coords_text = f"({q},{r})"
        text_surface = self.font.render(coords_text, True, (50, 50, 50))
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def axial_to_pixel(self, q, r):
        x = self.HEX_SIZE * (math.sqrt(3) * q + math.sqrt(3) / 2 * r)
        y = self.HEX_SIZE * (3 / 2 * r)
        return (x + self.CENTER_X, y + self.CENTER_Y)

    def draw_grid(self):
        for q in range(-4, 5):
            for r in range(-4, 5):
                if abs(q + r) <= 4:
                    x, y = self.axial_to_pixel(q, r)
                    self.draw_hexagon(x, y, self.HEX_SIZE, (255, 255, 255), q, r)

    def draw_piece(self):
        for q, r in self.piece:
            x, y = self.axial_to_pixel(q, r)
            self.draw_hexagon(x, y, self.HEX_SIZE, (255, 100, 100), q, r)

    def toggle_piece_position(self):
        max_positions = len(self.pieces[self.current_piece])
        self.current_position = (self.current_position + 1) % max_positions
        self.piece = self.pieces[self.current_piece][self.current_position]

    # def switch_piece(self):
    #     self.current_piece = 1 if self.current_piece == 2 else 2
    #     self.current_position = 0
    #     self.piece = self.pieces[self.current_piece][self.current_position]

    def switch_piece(self):
        # Obtient le nombre total de pièces
        max_pieces = len(self.pieces)
        # Passe à la pièce suivante, revient à 1 après la dernière pièce
        self.current_piece = (self.current_piece % max_pieces) + 1
        # Réinitialise la position à 0 pour la nouvelle pièce
        self.current_position = 0
        # Met à jour la pièce courante
        self.piece = self.pieces[self.current_piece][self.current_position]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.toggle_piece_position()
                    elif event.key == pygame.K_p:
                        self.switch_piece()

            self.screen.fill((245, 245, 245))
            self.draw_grid()
            self.draw_piece()
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    viewer = HexagonalCalendarWithPiece()
    viewer.run()