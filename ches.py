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
    
    def __init__(self, filename: str, location, r, type: ChessEnum):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(filename)
        # self.image = pygame.transform.smoothscale(self.image, (r,r))
        self.rect = pygame.Rect(0,0,r,r)
        self.type = type
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(type.value, 1, (0,0,0))
        textRect = text.get_rect()
        textRect.center = self.rect.center

    # spr_file_text = font.render("Feed me some file or image!", 1, (255, 255, 255))
    # spr_file_text_rect = spr_file_text.get_rect()
    # spr_file_text_rect.center = surf.get_rect().center

        self.rect.center = location
        
