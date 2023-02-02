import ttt
import pygame
from assets import *

pygame.init()
windowWidth, windowHeight = 1900, 1000
borderShort = 5
borderLong = int(.45 * windowHeight) + 2 * borderShort
display = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Tic Tac Toe")
boxList = []
borderList = []
XList = []
OList = []
turn = 1

for i in range(3):
	boxList.extend([pygame.Rect(
		int((windowWidth - 3 * 0.15 * windowHeight + 2 * borderShort)/2) + j * (int(0.15 * windowHeight) + borderShort), 
		int(0.27 * windowHeight + i * (0.15 * windowHeight + borderShort)),
		int(0.15 * windowHeight),
		int(0.15 * windowHeight)
		) for j in range(3)]
	)

for i in range(2):
	borderList.append(pygame.Rect(
		int((windowWidth - 3 * 0.15 * windowHeight + 2 * borderShort)/2 + 0.15 * windowHeight * (i+1) + i * borderShort),
		int(0.27 * windowHeight),
		borderShort,
		borderLong)
	)

for i in range(2):
	borderList.append(pygame.Rect(
		int((windowWidth - 3 * 0.15 * windowHeight + 2 * borderShort)/2),
		int(0.27 * windowHeight + (i+1) * 0.15 * windowHeight + i * borderShort),
		borderLong,
		borderShort)
	)

run = True
game = ttt.TTT()
game.display()

def makeX(rect):
	len = rect.width
	x1 = rect.x + int(len * 0.15)
	y1 = rect.y + int(len * 0.15)
	x2 = rect.x + int(len * 0.85)
	y2 = rect.y + int(len * 0.85)
	return [(x1, y1, x2, y2), (x1, y2, x2, y1)]

def makeO(rect):
	return (rect.center, int(rect.width * .425))

def drawX(arr):
	for i in arr:
		pygame.draw.line(display, c_black, (i[0], i[1]), (i[2], i[3]), 2)

def drawO(arr):
	for i in arr:
		pygame.draw.circle(display, c_black, i[0], i[1], 2)


while run:
	display.fill((107, 192, 209))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		# if event.type == pygame.KEYDOWN:
		if event.type == pygame.MOUSEBUTTONDOWN:
			xy = pygame.mouse.get_pos()
			for i in range(len(boxList)):
				if boxList[i].collidepoint(xy):
					if game.state[i] != '0':
						break
					if turn == 1:
						game.state = game.place(i, turn)
						XList.extend(makeX(boxList[i]))
						turn = 2
					else:
						game.state = game.place(i, turn)
						OList.append(makeO(boxList[i]))
						turn = 1
					game.display()


	for i in boxList:
		pygame.draw.rect(display, c_lightCyan, i)

	for i in borderList:
		pygame.draw.rect(display, c_white, i)

	drawX(XList)
	drawO(OList)
			
	pygame.display.flip()

pygame.quit()