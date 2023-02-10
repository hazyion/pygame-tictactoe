import pygame
import time
import math
import copy

pygame.font.init()

boxList, borderList, XList, OList, menuX, menuO = [], [], [], [], [], []
turn = 1
bot = True
swapTurn = False
menu = True
run = True
pointer = -1
XFirst = True

# windowWidth, windowHeight = 800, 600
windowWidth, windowHeight = 1920, 1000
borderShort = 5
borderLong = int(.45 * windowHeight) + 2 * borderShort

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
t = time.time()

for i in range(count):
	menuRect.top = (i+1) * gap + i * menuRect.width
	menuXORect.append(copy.copy(menuRect))

c_lightCyan = pygame.Color(107, 192, 209)
c_brightCyan = pygame.Color(138, 221, 237)
c_white = pygame.Color(255, 255, 255)
c_black = pygame.Color(1, 1, 1)

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

pointerArray = [
	pygame.Rect(int(windowWidth * 0.10), int(windowHeight * 0.45), int(windowWidth * 0.05), int(windowWidth * 0.05)),
	pygame.Rect(int(windowWidth * 0.10), int(windowHeight * 0.60), int(windowWidth * 0.05), int(windowWidth * 0.05))
	]


pygame.font.quit()