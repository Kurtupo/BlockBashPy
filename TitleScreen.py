import pygame
from pygame.locals import *
from time import sleep

pygame.init()

FrameRate = 30
fpsClock = pygame.time.Clock()

WindowDimensions = (900, 600)
white = (255, 255, 255)
DisplaySurface = pygame.display.set_mode(WindowDimensions)
pygame.display.set_caption('Block Bash Intro')

pygame.init()
pygame.mixer.init()
IntroMusic = pygame.mixer.Sound('audio/Intro.wav')
IntroMusic.play()

BigFont = pygame.font.Font('freesansbold.ttf', 48)
LittleFont = pygame.font.Font('freesansbold.ttf', 32)


global LineOne
global LineTwo
global LineThree

LineOne = "The Story So Far..."
LineTwo = "Far off in the distance..."
LineThree = "In a land unbound by time and space..."
LineFour = "lies the World of Shapes."
LineFive = "A peaceful place"
LineSix = "without worries or fears."
LineSeven = "Until one fateful day..."
LineEight = "The Sorcerer of Chaos appeared!"
LineNine = "He sought the powerful weapon"
LineTen = "hidden in the Land of Shapes."
LineEleven = "The Sorcerer's evil legion wrought havoc"
LineTwelve = "and captured the shapes of the land."
LineThirteen = "Now only one Shape can bring peace."
LineFourteen = "Using the Block Bash technique,"
LineFifteen = "Blockhead seeks to free his land and people"
LineSixteen = "and defeat the Sorcerer of Chaos."


LineOneVar = BigFont.render(LineOne, False, (0, 0, 0))
LineTwoVar = LittleFont.render(LineTwo, False, (0, 0, 0))
LineThreeVar = LittleFont.render(LineThree, False, (0, 0, 0))
LineFourVar = LittleFont.render(LineFour, False, (0, 0, 0))
LineFiveVar = LittleFont.render(LineFive, False, (0, 0, 0))
LineSixVar = LittleFont.render(LineSix, False, (0, 0, 0))
LineSevenVar = LittleFont.render(LineSeven, False, (0, 0, 0))
LineEightVar = LittleFont.render(LineEight, False, (0, 0, 0))
LineNineVar = LittleFont.render(LineNine, False, (0, 0, 0))
LineTenVar = LittleFont.render(LineTen, False, (0, 0, 0))
LineElevenVar = LittleFont.render(LineEleven, False, (0, 0, 0))
LineTwelveVar = LittleFont.render(LineTwelve, False, (0, 0, 0))
LineThirteenVar = LittleFont.render(LineThirteen, False, (0, 0, 0))
LineFourteenVar = LittleFont.render(LineFourteen, False, (0, 0, 0))
LineFifteenVar = LittleFont.render(LineFifteen, False, (0, 0, 0))
LineSixteenVar = LittleFont.render(LineSixteen, False, (0, 0, 0))


ShapeWorld = pygame.image.load('images/ShapeWorld.png')
Sorcerer = pygame.image.load('images/ChaosSorcerer.png')
Blockhead = pygame.image.load('images/BlockheadIntro.png')

def Blink(w):
    pygame.display.update()
    sleep(w)

while True:
    try:
        DisplaySurface.fill(white)
        # Y Value +35 for each line
        DisplaySurface.blit(LineOneVar, (10, 20))
        Blink(1)
        DisplaySurface.blit(ShapeWorld, (700, 80))
        DisplaySurface.blit(LineTwoVar, (20, 80))
        Blink(1.3)
        DisplaySurface.blit(LineThreeVar, (20, 115))
        Blink(1.5)
        DisplaySurface.blit(LineFourVar, (70, 150))
        Blink(1.3)
        DisplaySurface.blit(LineFiveVar, (20, 185))
        Blink(1.5)
        DisplaySurface.blit(LineSixVar, (70, 210))
        Blink(1.5)
        DisplaySurface.blit(LineSevenVar, (20, 245))
        Blink(1.5)
        DisplaySurface.blit(Sorcerer, (550, 200))
        DisplaySurface.blit(LineEightVar, (20, 280))
        Blink(1.3)
        DisplaySurface.blit(LineNineVar, (20, 315))
        Blink(1.4)
        DisplaySurface.blit(LineTenVar, (70, 350))
        Blink(1.5)
        DisplaySurface.blit(LineElevenVar, (20, 385))
        Blink(1.5)
        DisplaySurface.blit(LineTwelveVar, (70, 420))
        Blink(1.4)
        DisplaySurface.blit(LineThirteenVar, (20, 455))
        Blink(1.5)
        DisplaySurface.blit(Blockhead, (700, 400))
        DisplaySurface.blit(LineFourteenVar, (20, 490))
        Blink(1.5)
        DisplaySurface.blit(LineFifteenVar, (70, 525))
        Blink(1.5)
        DisplaySurface.blit(LineSixteenVar, (120, 560))
        Blink(1.5)
        sleep(1)
        IntroMusic.stop()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        pygame.display.update()
        fpsClock.tick(FrameRate)
        break
    except pygame.error:
        break

import MainMenu
print("")
