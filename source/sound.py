import pygame

class Sound():
	def __init__(self):
		self.shoot = pygame.mixer.Sound('../music/shoot.wav')
		self.boom = pygame.mixer.Sound('../music/boom.wav')

	def play_background_sound(self):
		pygame.mixer.music.load('../music/background.mp3')
		pygame.mixer.music.play()

	def play_shoot(self):
		self.shoot.play()

	def play_boom(self):
		self.boom.play()