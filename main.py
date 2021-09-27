#!/bin/python
#main script -  outers version
import pygame
import os

pygame.init()

## reminder to self - stick entire DB32 palette into table so i dont have to
## remember or keep copy/pasting rgb values from aseprite
def setPal(): # set palette
	global DARKBLUE
	DARKBLUE = (91,110,225)

def setWindow():
	WIDTH, HEIGHT = 512, 288 # set initial window size
	global WIN # make WIN global because its just easier to group stuff together in functions
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Blue Plane Game") # set window title
setPal()
setWindow() # Call window draw function
def main():
	
	
	print("\nTesting, Testing!\n") # print in terminal if game starts
	print(WIN)

	run = True
	while run: # main loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		WIN.fill(DARKBLUE)
		pygame.display.update()		
	pygame.quit()


if __name__ == "__main__":  # prevent python from mistaking main()
	main()              # for something from a module just in case
