print("")

# Import libraries
import pygame
import random
from time import *
from pygame.locals import *

# Intialize the mixer and clock
pygame.init()
pygame.mixer.init()
fpsClock = pygame.time.Clock()

# Damage, while not yet fully implemented, will be in the future
global currentDamage
currentDamage = 0
def addDamage(Damage):
    global currentDamage
    currentDamage =+ Damage


# Intensity is split into two parts: The displayed Gauge and the behind-the-scenes Counter
IntensityGauge = 0
IntensityCounter = 0

# Board Dimensions (In Blocks)
width = 7
height = 9

# How much the blocks will go up when manually raising the stack
BlockPush = range(33)

# Setting the frame rate; All time-based events will automatically adapt to the frame rate
FrameRate = 30

# Time for the blocks to rise/spawn, in seconds
SpawnTimeInSeconds = 10

# Some math to allow the last two lines of code to be future-proof
OriginalSpawnTime = SpawnTimeInSeconds * FrameRate
global time_to_spawn
time_to_spawn = OriginalSpawnTime

# Sound that plays when you Game Over
GG = pygame.mixer.Sound('audio/ouch.wav')
# Sound that plays when you clear blocks (normal audio is a bit too loud)
ClearSound = pygame.mixer.Sound('audio/VirusClear.wav')
ClearSound.set_volume(0.8)

# Multiple tracks, randomized each time you play!
MusicSelector = (random.randint(1, 6))
if MusicSelector == 1:
    musiC = pygame.mixer.Sound('audio/musica.wav')
elif MusicSelector == 2:
    musiC = pygame.mixer.Sound('audio/DungeonDome.wav')
elif MusicSelector == 3:
    musiC = pygame.mixer.Sound('audio/LavaReef1.wav')
elif MusicSelector == 4:
    musiC = pygame.mixer.Sound('audio/GrassLand4.wav')
elif MusicSelector == 5:
    musiC = pygame.mixer.Sound('audio/SandCanyon2.wav')
elif MusicSelector == 6:
    musiC = pygame.mixer.Sound('audio/Iceberg1.wav')
musiC.play(-1)



# Window settings
size = (700,425)
windowSurfaceObj = pygame.display.set_mode(size)
pygame.display.set_caption('Block Bash Py')

# Image shenanigans (These will become important later)
red = pygame.image.load('images/red.png')
white = pygame.Color(255,255,255)
blue = pygame.image.load('images/blue.png')
green = pygame.image.load('images/green.png')
yellow = pygame.image.load('images/yellow.png')
purple = pygame.image.load('images/purple.png')
gray_map = {'red': pygame.image.load('images/red_clear.png'),
            'blue': pygame.image.load('images/blue_clear.png'),
            'green': pygame.image.load('images/green_clear.png'),
            'yellow': pygame.image.load('images/yellow_clear.png'),
            'purple': pygame.image.load('images/purple_clear.png')}
clear_map = dict([(c, pygame.image.load('images/%s2.png' % c)) for c in ('red', 'blue', 'green', 'yellow', 'purple')])
# I'm going to have a lot of fun messing with this line of code...
testFont = pygame.font.Font('freesansbold.ttf', 32)

# Randomly selects which kind of enemy will appear
EnemySelector = random.randint(1, 2)
# EnemyState is used for playing animations for enemies
global EnemyState
EnemyState = 0

# This will display the enemy title (It also displays the character's title)
def EnemyTitle():
    if EnemySelector == 1:
        EnemyTitle1 = testFont.render("Meanie", False, (0, 0, 0))
        EnemyTitle2 = testFont.render("Beanie", False, (0, 0, 0))
        windowSurfaceObj.blit(EnemyTitle1, (510, 360))
        windowSurfaceObj.blit(EnemyTitle2, (550, 390))
    if EnemySelector == 2:
        EnemyTitle1 = testFont.render("Mister", False, (0, 0, 0))
        EnemyTitle2 = testFont.render("Twister", False, (0, 0, 0))
        windowSurfaceObj.blit(EnemyTitle1, (510, 360))
        windowSurfaceObj.blit(EnemyTitle2, (550, 390))
    CharacterTitle1 = testFont.render("Block", False, (0, 0, 0))
    CharacterTitle2 = testFont.render("Head", False, (0, 0, 0))
    windowSurfaceObj.blit(CharacterTitle1, (300, 360))
    windowSurfaceObj.blit(CharacterTitle2, (360, 390))

# CharacterState is used for playing animations for characters
global CharacterState
CharacterState = 0
global Character

# Uses the CharacterState to play animations
# Character swaps between two animations unless an interval of 10 damage has been dealt
def AnimateCharacter():
    global CharacterState
    global Character
    global CharacterX
    global CharacterY
    if CharacterState == 0:
        Character = pygame.image.load('images/Blockhead_01.png')
        CharacterX = 320
        CharacterY = 200
    if CharacterState == 30:
        Character = pygame.image.load('images/Blockhead_02.png')
        CharacterX = 320
        CharacterY = 214
    # The large parameter allows for more design space, since I can add more animations later
    if CharacterState == 300:
        Character = pygame.image.load('images/Blockhead_00.png')
        CharacterX = 320
        CharacterY = 200
    # Resets the animation
    if (CharacterState == 60) or (CharacterState == 330):
        CharacterState = -1
    windowSurfaceObj.blit(Character, (CharacterX, CharacterY))
    CharacterState += 1

# Similar to the Character animations, but uses its own variables
# This one is for the Meanie Beanie enemy
def MeanieBeanie():
    global EnemyState
    global Enemy
    global BeanieX
    global BeanieY
    global currentDamage
    if EnemyState == 0:
        Enemy = pygame.image.load('images/MeanieBeanie_01.png')
        BeanieX = 520
        BeanieY = 200
    if EnemyState == 30:
        Enemy = pygame.image.load('images/MeanieBeanie_02.png')
        BeanieX = 520
        BeanieY = 207
    if EnemyState == 300:
        Enemy = pygame.image.load('images/MeanieBeanie_00.png')
        BeanieX = 470
        BeanieY = 215
    if (EnemyState == 60) or (EnemyState == 330):
        EnemyState = -1
    windowSurfaceObj.blit(Enemy, (BeanieX, BeanieY))
    EnemyState += 1

# Once again similar to the previous animations
# This one is for the Mister Twister enemy
def MisterTwister():
    global EnemyState
    global Enemy
    global TwisterX
    global TwisterY
    global currentDamage
    if EnemyState == 0:
        Enemy = pygame.image.load('images/MisterTwister_01.png')
        TwisterX = 520
        TwisterY = 190
    if EnemyState == 30:
        Enemy = pygame.image.load('images/MisterTwister_02.png')
        TwisterX = 520
        TwisterY = 190
    if EnemyState == 300:
        Enemy = pygame.image.load('images/MisterTwister_00.png')
        TwisterX = 520
        TwisterY = 190
    if (EnemyState == 60) or (EnemyState == 330):
        EnemyState = -1
    windowSurfaceObj.blit(Enemy, (TwisterX, TwisterY))
    EnemyState += 1

# Depending one what enemy was chosen, this will animate its corresponding enemy.
def EnemyAnimate():
    if EnemySelector == 1:
        MeanieBeanie()
    if EnemySelector == 2:
        MisterTwister()


# Checks if three consecutive blocks touch each other
def three_consecutive_same(li):
    for i in range(len(li) - 2):
        if li[i] == li[i+1] and li[i+1] == li[i+2]:
            return True
    return False


class Block:
    fall_delay_time = FrameRate * 3 # Number of frames to fall 1 cell
    gravity_time = FrameRate / 3 # Number of frames block is in the air before falling
    clear_color = pygame.Color(150, 150, 150)

    def __init__(self, color_info):
        self.color_name, self.color = color_info
        self.timestep = 0
        self.clear_time = 50
        self.fall_delay = self.fall_delay_time
        self.is_falling = False # Changed by Board class
        self.fell_from_match = False # Changed to True by Board class
        self.clearing = False
        self.score_on_clear = 1

    def step(self):
        if self.is_falling or self.clearing:
            self.timestep += 1
        else:
            self.timestep = 0


class Board:
    chain_grace_period = Block.gravity_time # Chains are planned to be removed altogether
    def __init__(self):
        self.cells = [[None] * width for _ in range(height)]

        # Told you these guys would be important; generate_row() will use these
        self.tile_colors = [('red', red), ('blue', blue), ('green', green), ('yellow', yellow), ('purple', purple)]

        self.next_row = [None] * width
        
        self.generate_next_row()
        self.has_lost = False
        self.time = 0 # Number of frames since start
        self.chain = 0
        self.time_since_chain_end = 0
        self.num_matched = 0
        self.score = 0

    def get_cell(self, x, y):
        block = self.cells[y][x]
        if block:
            return block.color
        else:
            return None

    # This is for generating the next row (Generated rows are grayed out)
    def generate_next_row(self):
        for i in range(width):
            self.next_row[i] = random.choice(self.tile_colors)
        # This basically "re-rolls" if there is a natural combo. Game can't be too easy!
        if three_consecutive_same(self.next_row):
            self.generate_next_row()
        else:
            for i in range(width):
                self.next_row[i] = Block(self.next_row[i])

    # A simple game state function. Nothing fancy
    def is_going_to_lose(self):
        for cell in self.cells[0]:
            if cell is not None:
                return True
        return False

    # This actually adds the generated row to the matrix
    def add_next_row(self):
        if self.is_going_to_lose():
            # Stuff that happens when you lose
            print("Game Over!")
            print("Your Awesomeness: " + str(currentDamage))
            print("Intensity Reached: " + str(IntensityGauge))
            musiC.stop()
            GG.play()
            sleep (2)
            GG.stop()
            pygame.quit()
        else:
            # Swap each row up
            for i in range(height - 1):
                self.cells[i] = self.cells[i+1]
                self.cells[height - 1] = list(self.next_row)
                self.generate_next_row()

    # Swap cells when pressing Spacebar
    def swap_cells(self, x1, y1, x2, y2):
        if self.cells[y1][x1] is None or (not self.cells[y1][x1].clearing and not self.cells[y1][x1].is_falling):
            if self.cells[y2][x2] is None or (not self.cells[y2][x2].clearing and not self.cells[y2][x2].is_falling):
                self.cells[y1][x1], self.cells[y2][x2] = self.cells[y2][x2], self.cells[y1][x1]

    def clear_cells(self):
        # The original said this is only for debugging, so I won't mess with it
        self.cells = [[None] * width for _ in range(height)]

    def is_valid(self, x, y):
        return x in range(width) and y in range(height)

    def find_matched(self, x, y):
        # Checks right + down, adds all cells it finds in match 3
        block_type = self.get_cell(x,y)
        matched = set()
        if block_type != None and not self.cells[y][x].clearing:
            if x + 2 < width:
                if self.get_cell(x+1, y) == block_type and not self.cells[y][x+1].is_falling and not self.cells[y][x+1].clearing:
                    if self.get_cell(x+2, y) == block_type and not self.cells[y][x+2].is_falling and not self.cells[y][x+2].clearing:
                        matched.add((x+1,y))
                        matched.add((x+2,y))
                        matched.add((x,y))
            if y + 2 < height:
                if self.get_cell(x, y+1)==block_type and not self.cells[y+1][x].is_falling and not self.cells[y+1][x].clearing:
                    if self.get_cell(x, y+2)==block_type and not self.cells[y+2][x].is_falling and not self.cells[y+2][x].clearing:
                        matched.add((x, y+1))
                        matched.add((x, y+2))
                        matched.add((x,y))
        return matched

    def matched_blocks(self):
        # Returns a list of coordinates, where each coordinate represents the start of a match
        used_blocks = set()
        for i in range(width):
            for j in range(height):
                used_blocks = used_blocks.union(self.find_matched(i, j))
        if len(used_blocks) > 0:
            self.num_matched = len(used_blocks)
        return used_blocks

    def clear_matches(self):
        matched = self.matched_blocks()
        if matched:
            self.chain += 1
            for x, y in matched:
                self.cells[y][x].clearing = True
                self.cells[y][x].shown_color = Block.clear_color

    def reset_chain(self):
        self.chain = 0

    def timestep(self):
        """
        Order of events
        
        Blocks fall
        Matches get cleared
        New lines get spawned
        Values get reset
        
        Implement by checking every block multiple times. Probably optimizable. <-- (A word)
        """
        # The Intensity makes it so that the blocks will spawn at a faster rate the longer the game goes on
        global IntensityCounter
        global IntensityGauge
        global time_to_spawn
        IntensityCounter += 1

        # Intensity Gauge will naturally increase by 1 every second
        if IntensityCounter % FrameRate == 0:
            IntensityGauge += 1
            # Every 10 seconds, the spawn time lowers
            if IntensityCounter % (FrameRate * 10):
                time_to_spawn -= (FrameRate * (1/30))
                # Always make fail-safes
                if time_to_spawn <= 0:
                        time_to_spawn = 2
                IntensityCounter += 1

        # First find which blocks are falling. Default to not falling
        for i in range(width):
            for j in range(height):
                if self.cells[j][i]:
                    self.cells[j][i].is_falling = False
                if self.cells[j][i] is None:
                    for k in range(0, j):
                        if self.cells[k][i]:
                            if self.cells[k][i].clearing:
                                break
                            self.cells[k][i].is_falling = True
                    
        # Then timestep each falling block
        # Doing bottom up makes it work as intended
        for i in range(width):
            for j in range(height - 1, -1, -1):
                cell = self.cells[j][i]
                if cell:
                    cell.step()
                    if cell.clearing:
                        if cell.timestep >= cell.clear_time:
                            self.cells[j][i] = None
                            global currentDamage
                            currentDamage += 1

                            '''
                            # Damage will become important later
                            print ("" + (str(currentDamage)))
                            '''
                            # Certain aactions occur when an interval of 10 damage is dealt
                            # Here, it animates the character and enemy
                            if ((currentDamage % 10) == 0) and (currentDamage != 0):
                                global EnemyState
                                global CharacterState
                                # print("Nice blow!")
                                EnemyState = 300
                                CharacterState = 300
                            ClearSound.play()
                            self.score += cell.score_on_clear
                            # Tell all above that they are falling from a match
                            for k in range(j):
                                if self.cells[k][i]:
                                    self.cells[k][i].fell_from_match = True
                    elif (cell.fall_delay > 0) and (cell.timestep >= cell.fall_delay):
                        # Hope that this will only occur in valid situations. Probably does...
                        cell.fall_delay = 0
                        cell.timestep = 0
                    elif cell.timestep >= cell.gravity_time:
                        self.cells[j+1][i] = cell
                        self.cells[j][i] = None
                        # Recompute is falling
                        cell.is_falling = False
                        for k in range(j+2, height):
                            if self.cells[k][i] is None:
                                cell.is_falling = True
                        if not cell.is_falling:
                            cell.fall_delay = Block.fall_delay_time
                        
        self.clear_matches()
        self.time += 1
        # Rows spawn
        if self.time % time_to_spawn == 0:
            self.add_next_row()
        no_clearing = True
        for i in range(width):
            for j in range(height):
                if self.cells[j][i] and self.cells[j][i].clearing:
                    no_clearing = False
        if no_clearing and self.chain > 0:
            self.time_since_chain_end += 1
            if self.time_since_chain_end > Board.chain_grace_period:
                self.reset_chain()
                
class Cursor:
    """Represents the  cursor for the self."""
    def __init__(self):
        # x, y represent the left box of the cursor
        self.x = 2
        self.y = 2
    def move_left(self):
        self.x = max(self.x - 1, 0)
    def move_right(self):
        self.x = min(self.x + 1, width - 2)
    def move_up(self):
        self.y = max(self.y - 1, 0)
    def move_down(self):
        self.y = min(self.y + 1, height - 1)

# This should ALWAYS be 40
cellSize = 40
# Margins added to make research paper longer than it actually is
leftOffset = 10
topOffset = 50

# Summoning the board and cursor into existence
board = Board()
cursor = Cursor()

#Adds blocks at the beginning of the game
for _ in range(3):
    board.add_next_row()
time_held = {K_UP: 0, K_LEFT: 0, K_RIGHT: 0, K_DOWN: 0}

# Main Loop
while True:
    # I use two big try-except blocks to bypass the code crashing --> Menu crashing
    try:
        windowSurfaceObj.fill(white)
        # These four lines make the outline of the matrix
        pygame.draw.line(windowSurfaceObj, (0,0,0), (5,10), (5,410), 5)
        pygame.draw.line(windowSurfaceObj, (0,0,0), (294,10), (294, 410), 5)
        pygame.draw.line(windowSurfaceObj, (0,0,0), (5,10), (294,10), 5)
        pygame.draw.line(windowSurfaceObj, (0,0,0), (5,410), (294, 410), 5)
        board.timestep()
        # Displaying the number of Awesome Points
        scoreObj = testFont.render("Awesomeness: %d" % board.score, False, (0, 0, 0))
        windowSurfaceObj.blit(scoreObj, (310, 125))

        # I believe these will never be used during actual gameplay, and are probably just for testing purposes
        botVisiblePixels = int(cellSize * (board.time % time_to_spawn) / time_to_spawn)
        netTopOffset = topOffset - botVisiblePixels

        for i in range(width):
            for j in range(height):
                color = board.get_cell(i, j)
                if color is None:
                    color = (255, 255, 255)
                    pygame.draw.rect(windowSurfaceObj, color,
                                     (leftOffset + cellSize * i, netTopOffset + cellSize * j, cellSize, cellSize))
                elif board.cells[j][i].clearing:
                    windowSurfaceObj.blit(clear_map[board.cells[j][i].color_name],
                                          (leftOffset + cellSize * i, netTopOffset + cellSize * j, cellSize, cellSize))
                else:
                    windowSurfaceObj.blit(color,
                                          (leftOffset + cellSize * i, netTopOffset + cellSize * j, cellSize, cellSize))
        row = board.next_row
        for i in range(width):
            cell = row[i]
            windowSurfaceObj.blit(gray_map[cell.color_name], (leftOffset + cellSize * i, netTopOffset + cellSize * 9), (0, 0, cellSize, botVisiblePixels))
        # These time conversions aren't used in the code, since I base everything of of the frame rate by default
        # I left it in because you gotta appreciate someone taking the time (pun most definitely intended) to make it
        minutes = board.time // (60 * FrameRate)
        sec = (board.time - (60 * FrameRate ) * minutes) // FrameRate
        # Displaying the Intensity Gauge
        timeObj = testFont.render("Intensity: " + str(IntensityGauge), False, (0, 0, 0) )
        windowSurfaceObj.blit(timeObj, (310, 75))
        '''
        # Uncomment this to display the Intensity Counter
        n10cTea = testFont.render("Counter: " + str(IntensityCounter), False, (0, 0, 0))
        windowSurfaceObj.blit(n10cTea, (350, 200))
        '''
        # Displaying the cursor
        cursorObj = pygame.image.load('images/cursor.png')
        windowSurfaceObj.blit(cursorObj, (cellSize * cursor.x + leftOffset - 10, cellSize * cursor.y + netTopOffset - 10))

        # Animating the character, enemy, and titles
        AnimateCharacter()
        EnemyAnimate()
        EnemyTitle()

        # The "VS" display
        windowSurfaceObj.blit((testFont.render("VS", False, (0, 0, 0))), (450, 375))

        # The heart of this program, pygame events!
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                # Hooray for key bindings!
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    cursor.move_up()
                if event.key == K_DOWN:
                    cursor.move_down()
                if event.key == K_LEFT:
                    cursor.move_left()
                if event.key == K_RIGHT:
                    cursor.move_right()
                if event.key == K_SPACE:
                    board.swap_cells(cursor.x, cursor.y, cursor.x + 1, cursor.y)
                # This is to speed up the rising of blocks (You can do this in the actual games)
                if event.key == K_0:
                    for b in BlockPush:
                        board.timestep()

        pygame.display.update()
        fpsClock.tick(FrameRate)

    # This allows the game ending to not cause the menu to close
    except pygame.error:
        break

