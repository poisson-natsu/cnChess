import sys
from tokenize import Double
from typing import Tuple
import pygame

from chess import Chess, ChessRed

pygame.init()

# 一个格子长度
r = 60
# 棋盘边距
margin = r/2
# 棋盘线的宽度
lineWidth = 3
size = (margin*2+r*8, margin*2+r*9)
# 星距线的间距
starMargin = r/15
# 炮星的长度
starLength = r/10
# 星的宽度
starWidth = 2
# 棋子直径
chessR = 50

screen = pygame.display.set_mode(size)
screen.fill((115,115,115))

pygame.display.set_caption("Chinese Chess")

done = False

def drawStar(
    point: Tuple,
    position: int,
    margin: Double,
    length: Double,
    width: int = 1,):
    # point是围绕哪个点画星，position:画星的象限，0001，0010，0100， 1000
    if position & 1 == 1:
        pygame.draw.lines(screen, 
        (0,0,0), 
        False, 
        [
            (point[0]+margin, point[1]-margin-length - width/2),
            (point[0]+margin, point[1]-margin - width/2),
            (point[0]+margin+length, point[1]-margin - width/2)
        ], 
        width)

    if position & 2 == 2:
        pygame.draw.lines(screen, 
        (0,0,0), 
        False, 
        [
            (point[0]-margin - width/2, point[1]-margin-length - width/2),
            (point[0]-margin - width/2, point[1]-margin - width/2),
            (point[0]-margin-length - width/2, point[1]-margin - width/2)
        ], 
        width)
    if position & 4 == 4:
        pygame.draw.lines(screen, 
        (0,0,0), 
        False, 
        [
            (point[0]-margin - width/2, point[1]+margin+length),
            (point[0]-margin - width/2, point[1]+margin),
            (point[0]-margin-length - width/2, point[1]+margin)
        ], 
        width)
    if position & 8 == 8:
        pygame.draw.lines(screen, 
        (0,0,0), 
        False, 
        [
            (point[0]+margin, point[1]+margin+length),
            (point[0]+margin, point[1]+margin),
            (point[0]+margin+length, point[1]+margin)
        ], 
        width)


for i in range(10):
    pygame.draw.line(screen, (0,0,0), [margin, margin+i*r], [size[0] - margin, margin+i*r], lineWidth)
for j in range(9):
    if j == 0 or j == 8:
        pygame.draw.line(screen, (0,0,0), [margin+j*r, margin], [margin+j*r, margin+9*r], lineWidth)
    pygame.draw.line(screen, (0,0,0), [margin+j*r, margin], [margin+j*r, margin+4*r], lineWidth)
    pygame.draw.line(screen, (0,0,0), [margin+j*r, size[1] - margin], [margin+j*r, margin+5*r], lineWidth)

drawStar((margin+r,margin+2*r), 15,starMargin, starLength,starWidth)
drawStar((margin+r*7,margin+2*r), 15,starMargin, starLength,starWidth)
drawStar((margin+r,margin+7*r), 15,starMargin, starLength,starWidth)
drawStar((margin+r*7,margin+7*r), 15,starMargin, starLength,starWidth)

for i in range(2):
    drawStar((margin,margin+3*(i+1)*r), 9,starMargin, starLength,starWidth)
for i in range(2):
    drawStar((margin+8*r,margin+3*(i+1)*r), 6,starMargin, starLength,starWidth)
for i in range(3):
    drawStar((margin+r*(i+1)*2,margin+6*r), 15,starMargin, starLength,starWidth)
for i in range(3):
    drawStar((margin+r*(i+1)*2,margin+3*r), 15,starMargin, starLength,starWidth)
pygame.draw.line(screen, (0,0,0), [margin+3*r, size[1] - margin], [margin+5*r, size[1] - margin - 2*r], 3)
pygame.draw.line(screen, (0,0,0), [margin+3*r, size[1] - margin - 2*r], [margin+5*r, size[1] - margin], 3)
rook = Chess([margin, margin], chessR, ChessRed.Rook)
rook.renderTo(screen)
red = ChessRed.__members__
for key in red:
    print(key)
# print(pygame.font.get_fonts())

# fontName = pygame.font.match_font("songti")
# font = pygame.font.Font(fontName, 24)
# text = font.render("忍", True, (0,0,0), (255,255,0))
# # textRect = pygame.Rect(0,0,chessR,chessR)
# textRect = text.get_rect(center=[margin, margin])
# # textRect.center = screen.get_rect().center
# screen.blit(text, textRect)

# print(size)
# print(textRect.center)

# print(car.rect == car.textRect)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    pygame.display.flip()


