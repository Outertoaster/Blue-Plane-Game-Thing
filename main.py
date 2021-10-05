#!/usr/bin/env python
#main script - outers version
import pygame
import os

import palette # load palette variables from file
## remember to prepend "palette." to the colour variable

programIcon = pygame.image.load('tempicon.png') # set program icon
programName = "Blue Plane Game" # set program name
FPS = 30	# set game framerate cap

playerSpritesheet = pygame.image.load(os.path.join("assets", "player.png"))

def setWindow():
	WIDTH, HEIGHT = 512, 288 # set initial window size
	global WIN # make WIN global because its just easier to group stuff together in functions
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(programName) # set window title from var
	pygame.display.set_icon(programIcon) # set app icon from var
setWindow() # Call window draw function

def drawObjects():
	WIN.blit(playerSpritesheet, (256, 144))

def main():	
	print("\nTesting, Testing!\n") # print in terminal if game starts
	print(WIN)
	
	clock = pygame.time.Clock()
	run = True
	while run: # main loop
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		WIN.fill(palette.BLUE_1)

		drawObjects() # draw objects







		pygame.display.update()
	pygame.quit()


if __name__ == "__main__":  # prevent python from mistaking main()
	main()              # for something from a module just in case
