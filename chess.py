import pygame
from enum import Enum

class ChessEnum(Enum):
    pass
class ChessRed(ChessEnum):
    Rook = "车"
    Knight = "马"
    Elephant = "象"
    Mandarin = "士"
    King = "将"
    Cannon = "炮"
    Pawn = "卒"
class ChessBlack(ChessEnum):
    Chariot = "车"
    Horse = "马"
    Bishop = "相"
    Guard = "士"
    General = "帅"
    Canon = "炮"
    Soldier = "兵"

class Chess(pygame.sprite.Sprite):
    
    def __init__(self, location, r, type: ChessEnum):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/chess.png")
        self.image = pygame.transform.smoothscale(self.image, (r,r))
        self.rect = pygame.Rect(0,0,r,r)
        self.type = type
        self.rect.center = location

#pingfang
        fontName = pygame.font.match_font("songti")
        font = pygame.font.Font(fontName, 24)

        self.text = font.render(type.value, True, (0,0,0))
        self.textRect = self.text.get_rect(center=location)

    def renderTo(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)

    # spr_file_text = font.render("Feed me some file or image!", 1, (255, 255, 255))
    # spr_file_text_rect = spr_file_text.get_rect()
    # spr_file_text_rect.center = surf.get_rect().center

        
