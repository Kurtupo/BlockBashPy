import tkinter
import pygame
from time import *

pygame.init()
pygame.mixer.init(frequency=44100)
MainMenuMusic = pygame.mixer.Sound('audio/Bomb5_Title.wav')


# Create menu window
menu = tkinter.Tk()

# Change menu window background color
menu.configure(bg="white")

# Change the title
menu.title("Main Menu")
MainMenuMusicStatus = True

# Change the window size
menu.geometry("250x150")

# Function to start the game
def Start_Game():
    menu.quit()
    global MainMenuMusicStatus
    if MainMenuMusicStatus:
        MainMenuMusicStatus = False
        MainMenuMusic.stop()
    import tetrisattack

def Toggle_Music():
    global MainMenuMusicStatus
    if MainMenuMusicStatus:
        MainMenuMusicStatus = False
        MainMenuMusic.stop()
    else:
        MainMenuMusicStatus = True
        MainMenuMusic.play(-1)

# Function to quit the entire thing
def Exit():
    if MainMenuMusicStatus:
        MainMenuMusic.stop()
    menu.quit()

# The "Title" of the Menu
lbl_title = tkinter.Label(menu, text="Main Menu", bg="white")
lbl_title.pack()

# Just an empty space
lbl_empty = tkinter.Label(menu, text="", bg="white")
lbl_empty.pack()

# A button to start the game
btn_Start_Game = tkinter.Button(menu, text="Start Game", fg="black", bg="white", command=Start_Game)
btn_Start_Game.pack()

btn_Toggle_Music = tkinter.Button(menu, text="Toggle Music", fg="black", bg="white", command=Toggle_Music)
btn_Toggle_Music.pack()

lbl_empty2 = tkinter.Label(menu, text="", bg="white")
lbl_empty2.pack()

btn_Exit = tkinter.Button(menu, text="Quit", bg="white", command=Exit)
btn_Exit.pack()

# Set the music!
MainMenuMusic.play(-1)

# Start the main events loop
menu.mainloop()
print("End of Menu")
