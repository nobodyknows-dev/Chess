import pygame
from Scripts.pawn import pawn_move
from Scripts.capture_handler import handler

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.white_sq = []
        self.turn = True # True = White

        self.white_pieces = "RNBKQBNRPPPPPPPP"
        self.white_pos = [63, 62, 61, 60, 59, 58, 57, 56,
                          55, 54, 53, 52, 51, 50, 49, 48]
        
        self.black_pieces = "PPPPPPPPRNBKQBNR"
        self.black_pos = [15, 14, 13, 12, 11, 10, 9, 8,
                          7, 6, 5, 4, 3, 2, 1, 0]
        
        self.selected = None, None
        self.moves = []

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

    def legal_moves(self, piece, pos):
        legal = []
        if self.turn:
            color = "wh"
        else:
            color = "bl"

        if piece == "P":
            pos, promo = pawn_move(color, pos, self.black_pos, self.white_pos)
            legal.extend(pos)

        # Drawing legal moves
        for pos in legal:
            x, y = (pos % 8) * 50 + 100, (pos // 8) * 50 + 100
            if (pos % 8) % 2 == (pos // 8) % 2:
                pygame.draw.rect(self.screen, (183, 207, 228), pygame.Rect(x, y, 50, 50))
            else:
                pygame.draw.rect(self.screen, (111, 154, 154), pygame.Rect(x, y, 50, 50))

        return legal

    def check_selection(self):
        mx, my = pygame.mouse.get_pos()
        x, y = (mx - 100) // 50, ((my - 100) // 50)

        if 100 <= mx <= 500 and 100 <= my <= 500: 
            square = x + (y * 8)
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect((mx // 50) * 50, (my // 50) * 50, 50, 50))
            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn:  # White
                        if square in self.white_pos: # Clicking on a piece
                            self.selected = (self.white_pieces[self.white_pos.index(square)], square)
                        else:
                            if square in self.moves: # Clicking on legal moves
                                self.white_pos[self.white_pos.index(self.selected[1])] = square
                                self.moves = []
                                self.turn = not self.turn
                            self.selected = None, None
                    else: # Black
                        if square in self.black_pos: # Clicking on a piece
                            self.selected = (self.black_pieces[self.black_pos.index(square)], square)
                        else:
                            if square in self.moves: # Clicking on legal moves
                                self.black_pos[self.black_pos.index(self.selected[1])] = square
                                self.moves = []
                                self.turn = not self.turn
                            self.selected = None, None

        self.moves.extend(self.legal_moves(self.selected[0], self.selected[1]))
        self.black_pos, self.white_pos = handler(self.turn, self.black_pos, self.white_pos)

    def update(self):
        run = True

        self.check_pattern()
        while run:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill((118, 150, 86))

            # Drawing Board
            for x in self.white_sq:
                pygame.draw.rect(self.screen, (238, 238, 210), pygame.Rect(x[0] * 50 + 100, x[1] * 50 + 100, 50, 50))

            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(95, 95, 410, 410), 5)

            # Selection
            self.check_selection()

            # Drawing pieces
            self.draw_pieces()

            pygame.display.update()
            self.clock.tick(60)

Game().update()