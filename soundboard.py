import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

sound_dir = './sounds/'

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

sndA = pygame.mixer.Sound(sound_dir+"CastleThunder.wav")
sndB = pygame.mixer.Sound(sound_dir+"applause.wav")
sndC = pygame.mixer.Sound(sound_dir+"WilhelmScream.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print("Sampler Ready.")

while True:
   try:
      if (GPIO.input(23) == True):
         soundChannelA.play(sndA)
         print('sndA')
      if (GPIO.input(24) == True):
         soundChannelB.play(sndB)
         print('sndB')
      if (GPIO.input(25) == True):
         soundChannelC.play(sndC)
         print('sndC')
      sleep(.1)
   except KeyboardInterrupt:
      exit()