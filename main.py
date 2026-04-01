import pygame

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        self.white_sq = []

        self.white_pieces = "RNBKQBNRPPPPPPPP"
        self.white_pos = [63, 62, 61, 60, 59, 58, 57, 56,
                          55, 54, 53, 52, 51, 50, 49, 48]
        
        self.black_pieces = "PPPPPPPPRNBKQBNR"
        self.black_pos = [15, 14, 13, 12, 11, 10, 9, 8,
                          7, 6, 5, 4, 3, 2, 1, 0]

    def check_pattern(self):
        for i in range(8):
            for j in range(8):
                if i % 2 == j % 2:
                    self.white_sq.append((i, j))

    def image_load(self, piece, color):
        img = pygame.transform.scale_by(pygame.image.load(f"Pieces/{color}/{piece}_{color}.png"), 2)
        img.set_colorkey((0, 255, 0))
        return img

    def piece_check(self, x):
        piece = "pawn"
        if x == "P":
            piece = "pawn"
        elif x == "R":
            piece = "rook"
        elif x == "N":
            piece = "knight"
        elif x == "B":
            piece = "bishop"
        elif x == "Q":
            piece = "queen"
        else:
            piece = "king"

        return piece

    def draw_pieces(self):
        for index, x in enumerate(self.white_pieces):
            pos = self.white_pos[index]
            x_coord, y_coord = (pos % 8) * 50 + 105, (pos // 8) * 50 + 105
            self.screen.blit(self.image_load(self.piece_check(x), "wh"), (x_coord, y_coord))

        for index, x in enumerate(self.black_pieces):
            pos = self.black_pos[index]
            x_coord, y_coord = (pos % 8) * 50 + 105, (pos // 8) * 50 + 105
            self.screen.blit(self.image_load(self.piece_check(x), "bl"), (x_coord, y_coord))

    def update(self):
        run = True
        self.check_pattern()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill((100, 100, 100))

            # Drawing Board
            for x in self.white_sq:
                pygame.draw.rect(self.screen, (200, 150, 150), pygame.Rect(x[0] * 50 + 100, x[1] * 50 + 100, 50, 50))

            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(100, 100, 400, 400), 2)

            # Drawing pieces
            self.draw_pieces()

            pygame.display.update()
            self.clock.tick(60)

Game().update()