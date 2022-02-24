import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Rain rain rain")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGD_COLOUR = (230, 255, 250)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
cloud_image = pygame.image.load("Assets/cloud.png").convert_alpha()
cloud_image_tr = pygame.transform.scale(cloud_image, (200,100))
player_image = pygame.image.load("Assets/avatar.png").convert()
# image should not have been converted with convert_alpha(0 but with convert()
player_image.set_colorkey((255,255,255))
clock = pygame.time.Clock()

Ui_font = pygame.font.SysFont("arial", 25)


class RainDrop:
	def __init__(self, x ,y):
		self.x = x
		self.y = y
		self.velo = random.randint(1,10)
		self.accel = random.randint(1, 10)

	def move(self):
		self.y += self.accel

	def draw(self):
		pygame.draw.circle(screen, (150,150,150), (self.x, self.y), 2)


class Cloud:
	def __init__(self):

		self.x = -400

		self.y = 100

	def move(self):
		self.x += random.randint(1,2)

	def draw(self):
		screen.blit(cloud_image_tr, (self.x, self.y))

	def createrain(self):
		raindrops.append(RainDrop(random.randint(self.x, self.x+200), self.y+50))


class Player:
	def __init__(self):
		self.x = 0
		self.y = SCREEN_HEIGHT - 190

	def move(self):
		if pressed_keys[K_RIGHT]:
			self.x += 0.5

		if pressed_keys[K_LEFT]:
			self.x -= 0.5

	def draw(self):
		screen.blit(player_image, (self.x,self.y))


raindrops = []
cloud = Cloud()
player = Player()


while 1:
	#pygame registers all events from the users into an event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
		# 	y += 2

	pressed_keys = pygame.key.get_pressed()
	screen.fill(BACKGD_COLOUR)

	# Creating the rain one raindrop at a time
	cloud.createrain()

	cloud.draw()
	cloud.move()
	player.draw()
	player.move()

	for raindrop in raindrops:
		raindrop.move()
		raindrop.draw()


	pygame.display.flip()
