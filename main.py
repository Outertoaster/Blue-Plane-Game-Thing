#!/bin/python
#main script -  outers version
import pygame
import os

def setWindow():
	WIDTH, HEIGHT = 512, 288 # set initial window size
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Blue Plane Game") # set window title

def main():
	setWindow() # Call window draw function
	
	print("\nTesting, Testing!\n") # print in terminal if game starts

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				
	pygame.quit()


if __name__ == "__main__":  # prevent python from mistaking main()
	main()              # for something from a module just in case
