import pygame
import math
import random
import numpy as np 

class Piece:
    def __init__(self, id):
        self.id = id
        self.cells = []
        self.color = (200, 150, 150)
        self.position = (0,0)

    def rotate(self):
        """Rotation de 60 degrés dans le sens horaire pour une grille hexagonale"""
        new_cells = []
        for q, r in self.cells:
            # Formule de rotation pour coordonnées axiales
            new_q = -r
            new_r = q + r
            new_cells.append((new_q, new_r))
        self.cells = new_cells

    def draw(self, calendar):
        for cell in self.cells:
            abs_pos = (self.position[0] + cell[0], self.position[1] + cell[1])
            x, y = calendar.axial_to_pixel(abs_pos[0], abs_pos[1])
            calendar.draw_hexagon(x, y, calendar.HEX_SIZE, self.color)

class HexagonalCalendar:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 800
        self.HEX_SIZE = 30
        self.CENTER_X = self.WIDTH // 2
        self.CENTER_Y = self.HEIGHT // 2
        
        self.BACKGROUND = (245, 245, 245)
        self.GRID_COLOR = (100, 100, 100)
        self.CELL_COLOR = (255, 255, 255)
        self.TEXT_COLOR = (50, 50, 50)
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.Font(None, 24)
        pygame.display.set_caption("Calendrier Perpétuel")


        # Création des deux pièces
        self.piece1 = Piece(1)
        self.piece1.cells = [(-1,0), (0,0), (1,0), (0,-1), (1,-1), (1,-2)]
        self.piece1.position = (-2, 0)
        self.piece1.color = list(np.random.choice(range(256), size=3)) 
        
        self.piece2 = Piece(2)
        self.piece2.cells = [(-2,0), (-1,0), (0,0), (1,0), (2,0)]  # nouvelle pièce
        self.piece2.position = (-2, 2)  # position initiale différente
        self.piece2.color = list(np.random.choice(range(256), size=3)) 

        self.piece3 = Piece(3)
        self.piece3.cells = [(-1,0), (0,0), (1,0),(-1,1), (0,1), (1,1)]  # nouvelle pièce
        self.piece3.position = (-2, 2) 
        self.piece3.color = list(np.random.choice(range(256), size=3)) 

        self.piece4 = Piece(4)
        self.piece4.cells = [(-2,0), (-1,0), (0,0), (1,0), (1,1)]  # nouvelle pièce
        self.piece4.position = (0, 0)  
        self.piece4.color = list(np.random.choice(range(256), size=3)) 

        self.piece5 = Piece(5)
        self.piece5.cells = [(-1,0), (0,0), (1,0),(-1,1),(0,1)]  # nouvelle pièce
        self.piece5.position = (0, 2)  
        self.piece5.color = list(np.random.choice(range(256), size=3)) 
                
        self.piece6 = Piece(6)
        self.piece6.cells = [(0,-1), (0,0), (1,-1),(-1,1),(0,1)]  # nouvelle pièce
        self.piece6.position = (0, 0)  
        self.piece6.color = list(np.random.choice(range(256), size=3)) 

        self.piece7 = Piece(7)
        self.piece7.cells = [(-1,0), (0,0), (1,0),(1,1),(2,1)]  # nouvelle pièce
        self.piece7.position = (0, 0)  
        self.piece7.color = list(np.random.choice(range(256), size=3)) 

        self.piece8 = Piece(8)
        self.piece8.cells = [(-1,0), (0,0), (1,0),(2,-1),(-2,1)]  # nouvelle pièce
        self.piece8.position = (0, 0)  
        self.piece8.color = list(np.random.choice(range(256), size=3)) 

        self.piece9 = Piece(9)
        self.piece9.cells = [(-1,0), (0,0), (1,0),(1,1),(1,2)]  # nouvelle pièce
        self.piece9.position = (0, 0)  
        self.piece9.color = list(np.random.choice(range(256), size=3)) 
        
        self.piece10 = Piece(10)
        self.piece10.cells = [(-1,0), (0,0), (1,0),(-1,1),(-2,1)]  # nouvelle pièce
        self.piece10.position = (0, 0)  
        self.piece10.color = list(np.random.choice(range(256), size=3)) 

        self.piece11 = Piece(11)
        self.piece11.cells = [(-1,0), (0,0), (1,0),(-1,1),(-2,1),(-3,1)]  # nouvelle pièce
        self.piece11.position = (0, 0)  
        self.piece11.color = list(np.random.choice(range(256), size=3)) 
        
        # Dictionnaire du contenu du calendrier
        self.hex_content = {
            # Ligne -4 (Mois haut)
            (0,-4): "Mai", (1,-4): "Juin", (3,-4): "Juil", (4,-4): "Août",
            
            # Ligne -3
            (-1,-3): "Avril", (0,-3): "Dim", (1,-3): "Lun", (2,-3): "Mar", 
            (3,-3): "Mer", (4,-3): "Sept",
            
            # Ligne -2
            (-2,-2): "Mars", (0,-2): "Jeu", (1,-2): "Ven", (2,-2): "Sam", (4,-2): "Oct",
            
            # Ligne -1
            (-3,-1): "Fév", (-2,-1): "1", (-1,-1): "2", (0,-1): "3",
            (1,-1): "4", (2,-1): "5", (3,-1): "6", (4,-1): "Nov",
            
            # Ligne 0
            (-4,0): "Janv", (-3,0): "7", (-2,0): "8", (-1,0): "9", (0,0): "10",
            (1,0): "11", (2,0): "12", (3,0): "13", (4,0): "Déc",
            
            # Ligne 1
            (-3,1): "14", (-2,1): "15", (-1,1): "16", (0,1): "17",
            (1,1): "18", (2,1): "19",
            
            # Ligne 2
            (-3,2): "20", (-2,2): "21", (-1,2): "22", (0,2): "23", (1,2): "24",
            
            # Ligne 3
            (-3,3): "25", (-2,3): "26", (-1,3): "27", (0,3): "28",
            
            # Ligne 4
            (-3,4): "29", (-2,4): "30", (-1,4): "31"
        }

    def draw_hexagon(self, x, y, size, color):
        points = []
        for i in range(6):
            angle_deg = 60 * i + 30  # +30 pour avoir un plat en haut
            angle_rad = math.pi / 180 * angle_deg
            point_x = x + size * math.cos(angle_rad)
            point_y = y + size * math.sin(angle_rad)
            points.append((point_x, point_y))
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, self.GRID_COLOR, points, 2)

    def draw_hexagon_with_text(self, x, y, size, q, r, color):
        self.draw_hexagon(x, y, size, color)
        content = self.hex_content.get((q,r), "")
        if content:
            text_surface = self.font.render(content, True, self.TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(x, y))
            self.screen.blit(text_surface, text_rect)

    def axial_to_pixel(self, q, r):
        x = self.HEX_SIZE * (math.sqrt(3) * q + math.sqrt(3)/2 * r)
        y = self.HEX_SIZE * (3/2 * r)
        return (x + self.CENTER_X, y + self.CENTER_Y)

    def get_hex_coordinates(self, radius):
        coordinates = []
        for q in range(-radius, radius + 1):
            r1 = max(-radius, -q - radius)
            r2 = min(radius, -q + radius)
            for r in range(r1, r2 + 1):
                coordinates.append((q, r))
        return coordinates


    def draw_grid(self):
        self.screen.fill(self.BACKGROUND)
        
        # Dessine d'abord la grille de base
        coords = self.get_hex_coordinates(4)
        for q, r in coords:
            x, y = self.axial_to_pixel(q, r)
            self.draw_hexagon_with_text(x, y, self.HEX_SIZE, q, r, self.CELL_COLOR)
        
        # Dessine ensuite la pièce par-dessus
        self.piece1.draw(self)
        self.piece2.draw(self)
        self.piece3.draw(self)
        self.piece4.draw(self)
        self.piece5.draw(self)
        self.piece6.draw(self)
        self.piece7.draw(self)
        self.piece8.draw(self)
        self.piece9.draw(self)
        self.piece10.draw(self)
        self.piece11.draw(self)

        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Rotation avec la touche espace
                        self.piece1.rotate()
                    
            self.draw_grid()
            pygame.display.flip()
            
        pygame.quit()

if __name__ == "__main__":
    calendar = HexagonalCalendar()
    calendar.run()
