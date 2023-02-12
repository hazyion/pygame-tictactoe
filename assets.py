import pygame
import time
import math
import copy

pygame.font.init()

def makeX(rect):
	len = rect.width
	x1 = rect.x + int(len * 0.15)
	y1 = rect.y + int(len * 0.15)
	x2 = rect.x + int(len * 0.85)
	y2 = rect.y + int(len * 0.85)
	return [(x1, y1, x2, y2), (x1, y2, x2, y1)]

def makeO(rect):
	return (rect.center, int(rect.width * .425))

def makePointer(rect):
	len = rect.width
	x1 = rect.x + int(len * 0.25)
	y1 = rect.y + int(len * 0.45)
	x2 = rect.x + int(len * 0.65)
	y2 = rect.y + int(len * 0.70)
	x3 = x1
	y3 = rect.y + int(len * 0.95)
	return [(x1, y1, x2, y2), (x2, y2, x3, y3)]

def makeMenuXO(pixels, XFirst):
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

boxList, borderList, XList, OList, menuX, menuO = [], [], [], [], [], []
turn = 1
bot = True
swapTurn = False
menu = True
run = True
end = False
pointer = -1
XFirst = True
tie = False
t = time.time()

# windowWidth, windowHeight = 800, 600
windowWidth, windowHeight = 1920, 1000
borderShort = 5
borderLong = int(.45 * windowHeight) + 2 * borderShort

endLines = []

endLines.extend([
	((
		int((windowWidth - 3 * 0.15 * windowHeight + 2 * borderShort)/2),
		int(0.27 * windowHeight + windowHeight * 0.075 + i * (windowHeight * 0.15 + borderShort))
	), (
		int((windowWidth + 3 * 0.15 * windowHeight + 6 * borderShort)/2),
		int(0.27 * windowHeight + windowHeight * 0.075 + i * (windowHeight * 0.15 + borderShort))
	))
	for i in range(3)])

endLines.extend([
	((
		int((windowWidth - 2 * 0.15 * windowHeight + 2 * borderShort + 2 * i * (borderShort + 0.15 * windowHeight))/2),
		int(0.27 * windowHeight)
	), (
		int((windowWidth - 2 * 0.15 * windowHeight + 2 * borderShort + 2 * i * (borderShort + 0.15 * windowHeight))/2),
		int(windowHeight * 0.73)
	))
	for i in range(3)])

endLines.extend([
	((
		int((windowWidth - 3 * 0.15 * windowHeight + 2 * borderShort)/2),
		int(0.27 * windowHeight)
	), (
		int((windowWidth + 3 * 0.15 * windowHeight + 6 * borderShort)/2),
		int((0.27 + 3 * 0.15) * windowHeight + 2 * borderShort)
	)), ((
		int((windowWidth - 3 * 0.15 * windowHeight + 2 * borderShort)/2),
		int((0.27 + 3 * 0.15) * windowHeight + 2 * borderShort)
	), (
		int((windowWidth + 3 * 0.15 * windowHeight + 6 * borderShort)/2),
		int(0.27 * windowHeight)
	))
])

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

menuRect = pygame.Rect(int(windowWidth * 0.80), 0, int(windowWidth * 0.05), int(windowWidth * 0.05))
count = math.ceil((windowHeight)/(windowWidth * 0.05))
gap = int(windowWidth * 0.01)
menuXORect, menuX, menuO = [], [], []

for i in range(count):
	menuRect.top = (i+1) * gap + i * menuRect.width
	menuXORect.append(copy.copy(menuRect))

c_lightCyan = pygame.Color(107, 192, 209)
c_brightCyan = pygame.Color(138, 221, 237)
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(1, 1, 1)
c_red = pygame.Color(252, 48, 3)

p_menuText_left = int(windowWidth * 0.15)
p_pointerPvp_left = int(windowWidth * 0.1)
p_menuTitle_top = int(windowHeight * 0.18)
p_menuPvp_top = int(windowHeight * 0.45)
p_menuCpu_top = int(windowHeight * 0.6)

f_InterBold = pygame.font.Font('./assets/Inter-Bold.otf', int(windowWidth * 0.08))
f_InterLight = pygame.font.Font('./assets/Inter-Light.otf', int(windowWidth * 0.05))

s_title = f_InterBold.render('Tic Tac Toe', True, c_black)
s_pvp = f_InterLight.render('vs Player', True, c_black)
s_cpu = f_InterLight.render('vs Computer', True, c_black)

r_title = s_title.get_rect()
r_title.x = p_menuText_left
r_title.y = p_menuTitle_top
r_pvp = s_pvp.get_rect()
r_pvp.x = p_menuText_left
r_pvp.y = p_menuPvp_top
r_cpu = s_cpu.get_rect()
r_cpu.x = p_menuText_left
r_cpu.y = p_menuCpu_top
r_endPointer = copy.copy(boxList[5])
r_endPointer.x = int(windowWidth - 2 * r_endPointer.width) 
r_endPointer.y -= int(r_endPointer.height * 0.85)
r_endPointer.width *= 2
r_endPointer.height *= 2

defaultPointerWidth = int(windowHeight / 100)
endPointer = makePointer(r_endPointer)
endPointerWidth = int(windowWidth / 50)

pointerArray = [
	pygame.Rect(int(windowWidth * 0.10), int(windowHeight * 0.45), int(windowWidth * 0.05), int(windowWidth * 0.05)),
	pygame.Rect(int(windowWidth * 0.10), int(windowHeight * 0.60), int(windowWidth * 0.05), int(windowWidth * 0.05))
]

pygame.font.quit()