import pygame
pygame.init()


running = True

xResolution = 450
yResolution = 800

xPos = xResolution/2
yPos = yResolution

xPosInit = xPos
yPosInit = yPos

playerDim = 30
gravConst = 0.05
loopClock = 0
bounceVel = 5

screen = pygame.display.set_mode((xResolution, yResolution))
clock = pygame.time.Clock()

while running:
	screen.fill((0,0,0))

	events = pygame.event.get()
	player = pygame.Rect((xPos-(playerDim/2), yPos-playerDim, playerDim, playerDim))
	staticPlatform = pygame.Rect((100, 650, 80, 10))

	#Draws player 
	pygame.draw.rect(screen, (255, 255, 255), player)

	#Draws platforms
	pygame.draw.rect(screen, (255, 255, 255), staticPlatform)

	#Handles exiting game
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	#Key controls
	#TODO Try to get player to 'wrap around'
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (xPos - 25) >= 0:
		xPos-= 6
	if keys[pygame.K_RIGHT] and (xPos + 25) <= xResolution:
		xPos += 6

	#Rudimentary physics engine for realistic bouncing
	deltaY = int(bounceVel * loopClock - (0.5*gravConst*loopClock*loopClock))
	yPos = yPosInit - deltaY

	#Bounce time loop
	if deltaY < 0:
		loopClock = 0
	else:
		loopClock += 1

	if player.colliderect(staticPlatform):
		yPosInit = staticPlatform.top

	#Rerenders screen
	clock.tick(120)
	pygame.display.flip()

pygame.quit()