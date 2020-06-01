import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

sound_dir = './sounds/'

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(27, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

# applause = pygame.mixer.Sound(sound_dir+"applause.wav")
audience_laugh = pygame.mixer.Sound(sound_dir+"audience_laugh.wav")
yay = pygame.mixer.Sound(sound_dir+"yay.wav")
boo = pygame.mixer.Sound(sound_dir+"boo.wav")
boo.set_volume(.7)
laugh = pygame.mixer.Sound(sound_dir+"laugh.wav")
laugh.set_volume(.7)
ahh = pygame.mixer.Sound(sound_dir+"ahh.wav")
ahh.set_volume(.7)
# buzzer = pygame.mixer.Sound(sound_dir+"buzzer.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)
soundChannelD = pygame.mixer.Channel(4)
soundChannelE = pygame.mixer.Channel(5)

print("Sampler Ready.")

while True:
    try:
        if (GPIO.input(23) == True):
            soundChannelA.play(audience_laugh)
            print('chan 23')
        if (GPIO.input(24) == True):
            soundChannelB.play(ahh)
            print('chan 24')
        if (GPIO.input(25) == True):
            soundChannelC.play(boo)
            print('chan 25')
        if (GPIO.input(26) == True):
            soundChannelD.play(yay)
            print('chan 26')
        if (GPIO.input(27) == True):
            soundChannelE.play(laugh)
            print('chan 27')
        sleep(.1)
    except KeyboardInterrupt:
        exit()
