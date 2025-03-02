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
            1: [  # Piece 1 avec ses deux positions triangle
                [(-1, 0), (0, 0), (1, 0), (0, -1), (1, -1), (1, -2)],
                [(0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (2, -1)],
            ],
            2: [  # Piece 2 avec sa position unique barre
                [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
                [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)],
                [(-1, 1), (-2, 2), (0, 0), (1, -1), (2, -2)],
            ],
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
                # inverse
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
                [(1, -1), (0, 0), (-1, 1), (1, -2), (0, -1), (-1, 0)],
            ],
            4: [
                # Rotation 0° (Position initiale)
                [(-2, 0), (-1, 0), (0, 0), (1, 0), (1, 1)],  # Position initiale
                [(2, 0), (1, 0), (0, 0), (-1, 0), (-2, 1)],  # Retournée initiale
                # Rotation 60°
                [(0, -2), (0, -1), (0, 0), (0, 1), (-1, 2)],  # Rotation 60°
                [(0, -2), (0, -1), (0, 0), (0, 1), (-1, -2)],  # Retournée + 60°
                # Rotation 120°
                [(-1, 1), (-2, 1), (0, 0), (1, -1), (2, -2)],  # Rotation 120°
                [(-1, 1), (1, -2), (0, 0), (1, -1), (-2, 2)],  # Retournée + 120°
                # Rotation 180°
                [(2, 0), (1, 0), (0, 0), (-1, 0), (-1, -1)],  # Rotation 180°
                [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, -1)],  # Retournée + 180°
                # Rotation 240°
                [(0, 2), (0, 1), (0, 0), (0, -1), (1, -2)],  # Rotation 240°
                [(0, 2), (0, 1), (0, 0), (0, -1), (1, 2)],  # Retournée + 240°
                # Rotation 300°
                [(1, -1), (2, -1), (0, 0), (-1, 1), (-2, 2)],  # Rotation 300°
                [(1, -1), (-1, 2), (0, 0), (-1, 1), (2, -2)],  # Retournée + 300°
            ],
            5: [
                # Positions normales
                [(-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1)],  # Position initiale
                [(0, -1), (0, 0), (0, 1), (1, -1), (1, 0)],  # Rotation 60°
                [
                    (0, -1),
                    (0, 0),
                    (0, 1),
                    (-1, -0),
                    (-1, 1),
                ],  # Rotation 120° (corrigée)
                # Positions retournées
                [(-1, 0), (0, 0), (1, 0), (0, -1), (1, -1)],  # Retournée initiale
                [(-1, 1), (0, 0), (0, 1), (1, -1), (1, 0)],  # Retournée + 60°
                [
                    (-1, 1),
                    (0, 0),
                    (0, 1),
                    (-1, 2),
                    (1, 0),
                ],  # Retournée + 120° (corrigée)
            ],
            6: [
                # Positions normales
                [(0, -1), (0, 0), (1, -1), (-1, 1), (0, 1)],  # Position initiale
                [(1, -1), (0, 0), (1, 0), (-1, 0), (-1, 1)],  # Rotation 60°
                [(0, -1), (0, 0), (1, 0), (0, 1), (-1, 0)],  # Rotation 120°
            ],
            7: [
                # Rotation 0° (Position initiale)
                [(-1, 0), (0, 0), (1, 0), (1, 1), (2, 1)],
                [(-1, 0), (0, 0), (1, 0), (2, -1), (3, -1)],  # Rotation 0° Retourne
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (-1, 2), (-1, 3)],
                [
                    (0, -1),
                    (0, 0),
                    (0, 1),
                    (1, 1),
                    (1, 2),
                ],  # 60°  (appliquée : (q, r) -> (-r, q+r))
                # Rotation 120°
                [(1, -1), (0, 0), (-1, 1), (-2, 1), (-3, 2)],
                [
                    (1, -1),
                    (0, 0),
                    (-1, 1),
                    (-1, 2),
                    (-2, 3),
                ],  # 120° (60° appliquée deux fois)
                # Rotation 180°
                [(1, 0), (0, 0), (-1, 0), (-1, -1), (-2, -1)],
                [
                    (1, 0),
                    (0, 0),
                    (-1, 0),
                    (-2, 1),
                    (-3, 1),
                ],  # 180° (équivalent à (q, r) -> (-q, -r))
                # Rotation 240°
                [(0, 1), (0, 0), (0, -1), (1, -2), (1, -3)],
                [
                    (0, 1),
                    (0, 0),
                    (0, -1),
                    (-1, -1),
                    (-1, -2),
                ],  # 240° (rotation 180° + 60° supplémentaire)
                # Rotation 300°
                [(-1, 1), (0, 0), (1, -1), (2, -1), (3, -2)],
                [(-1, 1), (0, 0), (1, -1), (1, -2), (2, -3)],  # retoune
            ],
            8: [
                # Rotation 0°
                [(-1, 0), (0, 0), (1, 0), (2, -1), (-2, 1)],
                # retouner
                [(1, 0), (0, 0), (-1, 0), (-1, -1), (1, 1)],
                # Rotation 60°
                [(0, -1), (0, 0), (0, 1), (1, 1), (-1, -1)],
                # Rotation 60° retouner
                [(0, 1), (0, 0), (0, -1), (1, -2), (-1, 2)],
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
                [(-1, 1), (0, 0), (1, -1), (2, -1), (3, -1)],
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
                # Il faut retouner la piece mainteannt
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
                [(-1, 1), (0, 0), (1, -1), (-1, 0), (-2, 1)],
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
                # retouner
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
                [(-1, 1), (0, 0), (1, -1), (-1, 0), (-2, 1), (-3, 2)],
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

    def solve_puzzle(self, empty_cells=None):
        # Si empty_cells n'est pas spécifié, on utilise un ensemble vide
        if empty_cells is None:
            empty_cells = set()

        # Définir les cellules valides du plateau (hexagone de rayon 4)
        valid_cells = {
            (q, r) for q in range(-4, 5) for r in range(-4, 5) if abs(q + r) <= 4
        }

        # Retirer les cellules que l'utilisateur souhaite laisser vides
        valid_cells = valid_cells - set(empty_cells)

        # On définit l'ordre de placement des pièces
        pieces_order = sorted(self.pieces.keys())

        # Dictionnaire pour enregistrer le placement de chaque pièce
        solution = {}
        # Ensemble pour mémoriser les cellules déjà occupées
        occupied = set()

        def backtrack(index):
            # Si toutes les pièces ont été placées, c'est que l'on a une solution
            if index == len(pieces_order):
                return True

            piece_id = pieces_order[index]
            # Pour chaque rotation possible (chaque variante de la pièce)
            for rotation_index, variant in enumerate(self.pieces[piece_id]):
                # Essayer chaque cellule du plateau comme point d'ancrage
                for offset in valid_cells:
                    valid = True
                    abs_positions = []
                    # Calcul des positions absolues que la pièce occuperait
                    for dq, dr in variant:
                        pos = (dq + offset[0], dr + offset[1])
                        # Vérifier que la position est dans valid_cells et non occupée
                        if pos not in valid_cells or pos in occupied:
                            valid = False
                            break
                        abs_positions.append(pos)
                    if not valid:
                        continue

                    # On place la pièce en enregistrant sa rotation et son décalage
                    solution[piece_id] = (rotation_index, offset, abs_positions)
                    for pos in abs_positions:
                        occupied.add(pos)

                    # Passage à la pièce suivante
                    if backtrack(index + 1):
                        return True

                    # Sinon, on backtrack : on retire la pièce et on réessaie
                    del solution[piece_id]
                    for pos in abs_positions:
                        occupied.remove(pos)
            return False

        if backtrack(0):
            print("Solution trouvée :")
            self.solution = solution
            for pid in sorted(solution.keys()):
                rotation_index, offset, positions = solution[pid]
                print(
                    f"Pièce {pid} → Rotation {rotation_index}, Décalage {offset}, Positions absolues {positions}"
                )
            return True
        else:
            print("Aucune solution trouvée.")
            self.solution = None
            return False

    def select_empty_cells(self):
        """Permet à l'utilisateur de sélectionner les cases à laisser vides"""
        self.empty_cells = set()
        selecting = True

        print("Sélection des cases vides. Cliquez sur les cases à laisser vides.")
        print("Appuyez sur ENTRÉE pour valider ou ÉCHAP pour annuler.")

        while selecting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Touche Entrée
                        selecting = False
                    elif event.key == pygame.K_ESCAPE:  # Touche Échap
                        self.empty_cells = set()
                        selecting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche
                        # Convertir les coordonnées de la souris en coordonnées axiales
                        mouse_x, mouse_y = event.pos
                        # Trouver la cellule la plus proche
                        closest_cell = None
                        min_distance = float("inf")

                        for q in range(-4, 5):
                            for r in range(-4, 5):
                                if abs(q + r) <= 4:
                                    x, y = self.axial_to_pixel(q, r)
                                    distance = (mouse_x - x) ** 2 + (mouse_y - y) ** 2
                                    if distance < min_distance:
                                        min_distance = distance
                                        closest_cell = (q, r)

                        # Si la cellule est déjà dans empty_cells, la retirer, sinon l'ajouter
                        if closest_cell in self.empty_cells:
                            self.empty_cells.remove(closest_cell)
                        else:
                            self.empty_cells.add(closest_cell)

            # Afficher la grille avec les cellules sélectionnées
            self.screen.fill((245, 245, 245))
            self.draw_grid()

            # Afficher les cellules sélectionnées en bleu
            for q, r in self.empty_cells:
                x, y = self.axial_to_pixel(q, r)
                self.draw_hexagon(x, y, self.HEX_SIZE, (100, 100, 255), q, r)

            pygame.display.flip()

        return True

    def draw_solution(self):
        # Parcourir toutes les pièces de la solution
        for piece_id, (_, offset, positions) in self.solution.items():
            # Utiliser une couleur différente pour chaque pièce
            color = [
                (255, 100, 100),
                (100, 255, 100),
                (100, 100, 255),
                (255, 255, 100),
                (255, 100, 255),
                (100, 255, 255),
                (200, 150, 100),
                (150, 200, 100),
                (100, 200, 150),
                (200, 100, 150),
                (150, 100, 200),
            ][piece_id % 11]

            # Dessiner chaque cellule de la pièce
            for pos in positions:
                x, y = self.axial_to_pixel(pos[0], pos[1])
                self.draw_hexagon(x, y, self.HEX_SIZE, color, pos[0], pos[1])

        # Afficher les cases vides en bleu clair
        if hasattr(self, "empty_cells"):
            for q, r in self.empty_cells:
                x, y = self.axial_to_pixel(q, r)
                self.draw_hexagon(x, y, self.HEX_SIZE, (200, 200, 255), q, r)

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
                    elif event.key == pygame.K_s:  # Touche 'S' pour résoudre (Solve)
                        if hasattr(self, "empty_cells"):
                            self.solve_puzzle(self.empty_cells)
                        else:
                            self.solve_puzzle()
                    elif (
                        event.key == pygame.K_e
                    ):  # Touche 'E' pour sélectionner les cases vides (Empty)
                        self.select_empty_cells()

            self.screen.fill((245, 245, 245))
            self.draw_grid()

            # Si une solution existe, dessinez toutes les pièces placées
            if hasattr(self, "solution") and self.solution:
                self.draw_solution()
            else:
                self.draw_piece()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    viewer = HexagonalCalendarWithPiece()
    viewer.run()
