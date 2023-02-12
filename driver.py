import ttt
import pygame
import time
import copy
from assets import *

pygame.init()
display = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Tic Tac Toe")

game = ttt.TTT()

def drawX(tup, width=defaultPointerWidth):
	pygame.draw.line(display, c_black, (tup[0], tup[1]), (tup[2], tup[3]), width)

def drawO(tup, width=defaultPointerWidth):
	pygame.draw.circle(display, c_black, tup[0], tup[1], width)

while run:
	display.fill(c_lightCyan)
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
			elif not end:
				if bot:
					if turn == 1:
						for i in range(len(boxList)):
							if boxList[i].collidepoint(xy):
								if game.state[i] == '0':
									game.state = game.place(i, turn)
									XList.extend(makeX(boxList[i]))
									swapTurn = True
									if game.end(1) != -1:
										end = True
									elif game.tie():
										end = True
										tie = True

				else:
					for i in range(len(boxList)):
						if boxList[i].collidepoint(xy):
							if game.state[i] != '0':
								break
							if turn == 1:
								game.place(i, turn)
								XList.extend(makeX(boxList[i]))
								swapTurn = True
								if game.end(1) != -1:
									end = True
								elif game.tie():
									end = True
									tie = True
							else:
								game.place(i, turn)
								OList.append(makeO(boxList[i]))
								swapTurn = True
								if game.end(2) != -1:
									end = True
			else:
				if r_endPointer.collidepoint(xy):
					tie = False
					end = False
					menu = True
					game = ttt.TTT()
					turn = 1
					swapTurn = False
					XList.clear()
					OList.clear()

	if bot and turn == 2 and not end:
		time.sleep(0.5)
		nextState = game.Osearch(game.state, 4)
		for i in range(len(nextState)):
			if nextState[i] != game.state[i]:
				game.place(i, turn)
				OList.append(makeO(boxList[i]))
				break
		pygame.event.clear()
		if game.end(2) != -1:
			end = True
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
				drawX(i)

		XFirst = makeMenuXO(pixels, XFirst)
		for i in menuX:
			drawX(i)
		for i in menuO:
			drawO(i)
		pygame.display.flip()
		continue

	if not menu:
		for i in boxList:
			pygame.draw.rect(display, c_lightCyan, i)

		for i in borderList:
			pygame.draw.rect(display, c_white, i)

		for i in XList:
			drawX(i, 2)
		for i in OList:
			drawO(i, 2)

	if end:
		if not tie:
			if turn == 1:
				pygame.draw.line(display, c_red, endLines[game.end(1) - 1][0], endLines[game.end(1) - 1][1], 3)
			else:
				pygame.draw.line(display, c_red, endLines[game.end(2) - 1][0], endLines[game.end(2) - 1][1], 3)

		if r_endPointer.collidepoint(xy):
			endPointerWidth = int(windowWidth / 50)
		else:
			endPointerWidth = defaultPointerWidth

		for i in endPointer:
			drawX(i, endPointerWidth)

	if not end and swapTurn:
		turn = 2 if turn == 1 else 1
		swapTurn = False

	pygame.display.flip()

pygame.quit()