from pygame import *

init()

# сдвиг фона
shift = 0
# текущая скорость фона
speed = 0

class GameSprite(sprite.Sprite):
	def __init__(self, player_image, player_x, player_y, player_speed):
		super().__init__()

		self.image = transform.scale(image.load(player_image), (55, 55))
		self.speed = player_speed

		self.rect = self.image.get_rect()
		self.rect.x = player_x
		self.rect.y = player_y

	def reset(self):
		window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
	def update(self):
		keys = key.get_pressed()
		if keys[K_LEFT] and self.rect.x > 5:
			self.rect.x -= self.speed
		if keys[K_RIGHT] and self.rect.x < win_width - 80:
			self.rect.x += self.speed
		if keys[K_UP] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_DOWN] and self.rect.y < win_height - 80:
			self.rect.y += self.speed
	def gravitate(self):
 		self.y_speed += 0.25
 		self.stands_on = False 
 	
# 	def jump(self, y):
#		if self.stands_on:
#		 	self.y_speed = y


class Wall(sprite.Sprite):
    def _init_(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super()._init_()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

img_player = 'player.png'

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("ARCADA")
background = transform.scale(image.load("phon1.png"), (win_width, win_height))

all_sprites = sprite.Group()
barriers = sprite.Group()

clock = time.Clock()
FPS = 60

player = Player(img_player, 50, win_height / 2, 10)


w = Wall(0, 255, 255, 200, 350, 300, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 0, 200, 350, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 500, 0, 20, 370)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 0, 550, 300, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 450, 550, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 750, 470, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 450, 550, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 500, 350, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 950, 200, 20, 500)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 750, 250, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 950, 180, 500, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1600, 550, 100, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1190, 550, 100, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1390, 550, 100, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 970, 550, 100, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1070, 370, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1380, 370, 380, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1600, 0, 20, 370)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 2000, 270, 20, 500)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1800, 470, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 1800, 270, 200, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 2100, 270, 70, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 2260, 270, 70, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 2410, 270, 70, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 0, 0, 5000, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 0, 0, 20, 720)
barriers.add(w)
all_sprites.add(w)
w = Wall(0, 255, 255, 2480, 0, 20, 720)
barriers.add(w)
all_sprites.add(w)

#Это лава. Напишите код проигрыша при столкновении с ней.
w = Wall(255, 0, 0, 0, 580, 5000, 20)
barriers.add(w)
all_sprites.add(w)


game = True
finish = False

while game:
	for e in event.get():
		if e.type == QUIT:
			game = False
	if finish != True:
		window.blit(background, (0,0))

		all_sprites.update()
        all_sprites.draw(window)
		player.update()
		player.reset()

		

#		w.draw_wall()

	display.update()
clock.tick(FPS)
