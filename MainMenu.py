# Import pygame and libraries
from pygame.locals import *
from time import *
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

# Music!
pygame.init()
pygame.mixer.init(frequency=32006)
MainMenuMusic = pygame.mixer.Sound('audio/64_Menu.wav')
MainMenuMusic.play(-1)

# Max number of characters is 38
KeyboardControls = ['Use the arrow keys to move the cursor',
         'Use the space bar to swap blocks',
         'Connect 3+ Blocks to bash them!',
         'Gain Awesome Points!',
         'Press Zero to raise the blocks'
         ]

# Will change this when controller support is added
ControllerControls = ['Use the arrow keys to move the cursor',
         'Use the space bar to swap blocks',
         'Connect 3+ Blocks to bash them!',
         'Gain Awesome Points!',
         'Press Zero to raise the blocks'
         ]

# Color of the... background
COLOR_BACKGROUND = (236, 203, 217)
# Color of options
COLOR_BLACK = (0, 0, 0)
# Color when highlighting a selection by default
COLOR_WHITE = (234, 82, 111)
FPS = 60.0
# Color of the inner menu
MENU_BACKGROUND_COLOR = (255, 239, 246)
WINDOW_SIZE = (640, 480)

# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Block Bash Main Menu')
clock = pygame.time.Clock()

# Not really sure what this does...
dt = 1 / FPS

# Global variables
# Will later implement a level select
DIFFICULTY = ['GAME']


# -----------------------------------------------------------------------------

def play_function(difficulty, font):
    """
    Main game function
    
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None
    """
    MainMenuMusic.stop()

    import tetrisattack

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        try:
            playevents = pygame.event.get()
            for e in playevents:
                if e.type == QUIT:
                    exit()
                elif e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        if main_menu.is_disabled():
                            main_menu.enable()

                            # Quit this function, then skip to loop of main-menu on line 197
                            return
        except pygame.error:
            break

        # Pass events to main_menu
        main_menu.mainloop(playevents)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()


def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    surface.fill(COLOR_BACKGROUND)


# -----------------------------------------------------------------------------

# PLAY MENU
play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Play menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
# When pressing return -> play(DIFFICULTY[0], font)
play_menu.add_option('Start', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))

play_menu.add_option('Back', PYGAME_MENU_BACK)

# KBC / Keyboard MENU
KBC_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='Controls',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )

# CNC / ControllerControls MENU
CNC_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='Controls',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )

for m in KeyboardControls:
    KBC_menu.add_line(m)
KBC_menu.add_option('Return to menu', PYGAME_MENU_BACK)

for m in ControllerControls:
    CNC_menu.add_line(m)
CNC_menu.add_option('Return to menu', PYGAME_MENU_BACK)


# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Play', play_menu)
main_menu.add_option('Keyboard Controls', KBC_menu)
# main_menu.add_option('Controller Controls', CNC_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
# Main loop
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    try:
        main_menu.mainloop(events)
    except pygame.error:
        break

    # Flip surface
    pygame.display.flip()

# Nice confirmation message when code ends
print("End of Menu")
