import pygame
import math

class HexagonalCalendar:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 800
        self.HEX_SIZE = 40
        self.CENTER_X = self.WIDTH // 2
        self.CENTER_Y = self.HEIGHT // 2
        
        self.BACKGROUND = (245, 245, 245)
        self.GRID_COLOR = (100, 100, 100)
        self.CELL_COLOR = (255, 255, 255)
        self.TEXT_COLOR = (50, 50, 50)
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.Font(None, 24)  # Taille de police ajustée
        pygame.display.set_caption("Calendrier Perpétuel")
    

        
        # Dictionnaire avec le contenu réel du calendrier
        self.hex_content = {
            # Première ligne (Mois)
            (0,-4): "Mai", (1,-4): "Juin", (3,-4): "Juil", (4,-4): "Août",
            
            # Deuxième ligne
            (-1,-3): "Avril", (0,-3): "Dim", (1,-3): "Lun", (2,-3): "Mar", 
            (3,-3): "Mer", (4,-3): "Sept",
            
            # Troisième ligne
            (-2,-2): "Mars", (0,-2): "Jeu", (1,-2): "Ven", (2,-2): "Sam", (4,-2): "Oct",
            
            # Quatrième ligne (début des nombres)
            (-3,-1): "Fév", (-2,-1): "1", (-1,-1): "2", (0,-1): "3",
            (1,-1): "4", (2,-1): "5", (3,-1): "6", (4,-1): "Nov",
            
            # Suite des nombres et mois
            (-4,0): "Janv", (-3,0): "7", (-2,0): "8", (-1,0): "9", (0,0): "10",
            (1,0): "11", (2,0): "12", (3,0): "13", (4,0): "Déc",
            
            # Nombres
            (-3,1): "14", (-2,1): "15", (-1,1): "16", (0,1): "17",
            (1,1): "18", (2,1): "19",
            
            (-3,2): "20", (-2,2): "21", (-1,2): "22", (0,2): "23", (1,2): "24",
            
            (-3,3): "25", (-2,3): "26", (-1,3): "27", (0,3): "28",
            
            (-3,4): "29", (-2,4): "30", (-1,4): "31"
        }

    def draw_hexagon_with_text(self, x, y, size, q, r, color):
        # Dessine l'hexagone
        points = []
        for i in range(6):
            angle_deg = 60 * i + 30
            angle_rad = math.pi / 180 * angle_deg
            point_x = x + size * math.cos(angle_rad)
            point_y = y + size * math.sin(angle_rad)
            points.append((point_x, point_y))
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, self.GRID_COLOR, points, 2)
        
        # Affiche le contenu de l'hexagone
        content = self.hex_content.get((q,r), "")
        if content:
            text_surface = self.font.render(content, True, self.TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(x, y))
            self.screen.blit(text_surface, text_rect)


    # def draw_hexagon_with_coords(self, x, y, size, q, r, color):
        # # Dessine l'hexagone
        # points = []
        # for i in range(6):
        #     angle_deg = 60 * i + 30
        #     angle_rad = math.pi / 180 * angle_deg
        #     point_x = x + size * math.cos(angle_rad)
        #     point_y = y + size * math.sin(angle_rad)
        #     points.append((point_x, point_y))
        # pygame.draw.polygon(self.screen, color, points)
        # pygame.draw.polygon(self.screen, self.GRID_COLOR, points, 2)
        
        # # Ajoute les coordonnées
        # coords_text = f"({q},{r})"
        # text_surface = self.font.render(coords_text, True, self.TEXT_COLOR)
        # text_rect = text_surface.get_rect(center=(x, y))
        # self.screen.blit(text_surface, text_rect)

    def get_hex_coordinates(self, radius):
        coordinates = []
        for q in range(-radius, radius + 1):
            r1 = max(-radius, -q - radius)
            r2 = min(radius, -q + radius)
            for r in range(r1, r2 + 1):
                coordinates.append((q, r))
        return coordinates

    def axial_to_pixel(self, q, r):
        x = self.HEX_SIZE * (math.sqrt(3) * q + math.sqrt(3)/2 * r)
        y = self.HEX_SIZE * (3/2 * r)
        return (x + self.CENTER_X, y + self.CENTER_Y)

    def draw_grid(self):
        self.screen.fill(self.BACKGROUND)
        
        coords = self.get_hex_coordinates(4)
        for q, r in coords:
            x, y = self.axial_to_pixel(q, r)
            self.draw_hexagon_with_text(x, y, self.HEX_SIZE, q, r, self.CELL_COLOR)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.draw_grid()
            pygame.display.flip()
            
        pygame.quit()

if __name__ == "__main__":
    calendar = HexagonalCalendar()
    calendar.run()
