import ttt
import pygame
import time
import copy
from assets import *

pygame.init()
display = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Tic Tac Toe")

game = ttt.TTT()

def makeX(rect):
	len = rect.width
	x1 = rect.x + int(len * 0.15)
	y1 = rect.y + int(len * 0.15)
	x2 = rect.x + int(len * 0.85)
	y2 = rect.y + int(len * 0.85)
	return [(x1, y1, x2, y2), (x1, y2, x2, y1)]

def makeO(rect):
	return (rect.center, int(rect.width * .425))

def drawX(tup, width=5):
	pygame.draw.line(display, c_black, (tup[0], tup[1]), (tup[2], tup[3]), width)

def drawO(tup, width=4):
	pygame.draw.circle(display, c_black, tup[0], tup[1], width)

def makePointer(rect):
	len = rect.width
	x1 = rect.x + int(len * 0.25)
	y1 = rect.y + int(len * 0.45)
	x2 = rect.x + int(len * 0.65)
	y2 = rect.y + int(len * 0.70)
	x3 = x1
	y3 = rect.y + int(len * 0.95)
	return [(x1, y1, x2, y2), (x2, y2, x3, y3)]

def drawMenuXO(pixels, XFirst):
	menuX.clear()
	menuO.clear()
	for i in range(count):
		menuXORect[i].top -= pixels
		
	rem_count = 0
	for i in range(count):
		if menuXORect[i].top < (-1.5) * menuXORect[i].height:
			XFirst = not XFirst
			rem_count += 1
			continue;
		break;
		
	for i in range(rem_count):
		menuXORect.pop(0)
		menuRect.top = menuXORect[-1].top + gap + menuXORect[-1].height
		menuXORect.append(copy.copy(menuRect))

	X = XFirst
	for i in range(count):
		if X:
			X = not X
			menuX.extend(makeX(menuXORect[i]))
			
		else:
			X = not X
			menuO.append(makeO(menuXORect[i]))
	return XFirst

while run:
	display.fill((107, 192, 209))
	for event in pygame.event.get():
		xy = pygame.mouse.get_pos()
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if menu:
				if r_pvp.collidepoint(xy):
					menu = False
					bot = False
				elif r_cpu.collidepoint(xy):
					menu = False
					bot = True
			else:
				if bot:
					if turn == 1:
						for i in range(len(boxList)):
							if boxList[i].collidepoint(xy):
								if game.state[i] == '0':
									game.state = game.place(i, turn)
									XList.extend(makeX(boxList[i]))
									swapTurn = True
				else:
					for i in range(len(boxList)):
						if boxList[i].collidepoint(xy):
							if game.state[i] != '0':
								break
							if turn == 1:
								game.place(i, turn)
								XList.extend(makeX(boxList[i]))
								swapTurn = True
							else:
								game.place(i, turn)
								OList.append(makeO(boxList[i]))
								swapTurn = True
	
	if menu:
		pointer = -1
		if r_pvp.collidepoint(xy):
			pointer = 0
		elif r_cpu.collidepoint(xy):
			pointer = 1
		pixels = 0
		if time.time() - t > 0.05:
			t = time.time()
			pixels = 3
		display.blit(s_title, (p_menuText_left, p_menuTitle_top))
		display.blit(s_pvp, (p_menuText_left, p_menuPvp_top))
		display.blit(s_cpu, (p_menuText_left, p_menuCpu_top))
		if pointer != -1:
			for i in makePointer(pointerArray[pointer]):
				drawX(i, 11)

		XFirst = drawMenuXO(pixels, XFirst)
		for i in menuX:
			drawX(i)
		for i in menuO:
			drawO(i)
		pygame.display.flip()
		continue

	if bot and turn == 2:
		time.sleep(0.5)
		nextState = game.Osearch(game.state, 4)
		for i in range(len(nextState)):
			if nextState[i] != game.state[i]:
				game.place(i, turn)
				OList.append(makeO(boxList[i]))
				break
		swapTurn = True

	for i in boxList:
		pygame.draw.rect(display, c_lightCyan, i)

	for i in borderList:
		pygame.draw.rect(display, c_white, i)

	for i in XList:
		drawX(i, 2)
	for i in OList:
		drawO(i, 2)

	if swapTurn:
		turn = 2 if turn == 1 else 1
		swapTurn = False

	pygame.display.flip()

pygame.quit()