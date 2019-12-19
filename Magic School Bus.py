
 
import pygame
 
pygame.init()

# Global constants
font = pygame.font.SysFont("Arial", 25, bold=True)
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (25, 86, 8)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (235, 58, 56)
DARK_RED = (175, 33, 24)
CELL_PINK = (255, 138, 148)
CELL_BLUE = (90, 128, 211)
 
scoretext = font.render(str("Kids collected: 0/4"), False, WHITE)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(
        pygame.image.load("images.png").convert(),
        (40, 30)
        )
        


        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/coin
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, self.level.bouncer_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, self.level.bouncer_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        self.rect.x += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        double_jump_list_r = pygame.sprite.spritecollide(self, self.level.bouncer_list, False)
        self.rect.x -= 4
        double_jump_list_l = pygame.sprite.spritecollide(self, self.level.bouncer_list, False)
        self.rect.y -= 2
        self.rect.x += 2

    
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
        
        if len(double_jump_list_r) > 0 or len(double_jump_list_l) > 0:
            print("DOUBLE JUMP")
            self.change_y = +10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 


class Player_2(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 300
        height = 300
        self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(
        pygame.image.load("images.png").convert(),
        (300, 300)
        )
        


        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/coin
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, self.level.bouncer_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, self.level.bouncer_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        self.rect.x += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        double_jump_list_r = pygame.sprite.spritecollide(self, self.level.bouncer_list, False)
        self.rect.x -= 4
        double_jump_list_l = pygame.sprite.spritecollide(self, self.level.bouncer_list, False)
        self.rect.y -= 2
        self.rect.x += 2

    
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
        
        if len(double_jump_list_r) > 0 or len(double_jump_list_l) > 0:
            print("DOUBLE JUMP")
            self.change_y = +10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0



class Token(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("pheobe.png")
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Token_2(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("asian.png")
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Token_Intro(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("shrink.png")
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Token_3(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("carlos.png")
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

class Token_4(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("otherkid.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Token_5(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("arnold.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height, color=GREEN):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

class Bouncer(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height, color=GREEN):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.bouncer_list = pygame.sprite.Group()
    
 
        self.rect = self.image.get_rect()


class Bullet(pygame.sprite.Sprite):
    VELOCITY = 3

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image = pygame.transform.scale(pygame.image.load("heart_edit.png"), (10, 10))

        self.rect = self.image.get_rect()

    def update(self):
        #move the bullet up the screen
        self.rect.x -= self.VELOCITY

 
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.token_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.bouncer_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
         
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.token_list.update()
        self.platform_list.update()
        self.bouncer_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLACK)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)
 
 
# Create platforms for the level
class Intro(Level):
    """ Definition for level 1. """

    def draw(self, screen):
        screen.fill(BLACK)
        
        introtext = font.render(str("Oh no! All the kids got separated while we were inside the body."), False, WHITE)
        intro2 = font.render(str("Quick! Let's go and find them."), False, WHITE)
        tokentext = font.render(str("Collect the shrink ray to begin."), False, WHITE)


        frizzle = pygame.Surface([50, 50])
        frizzle = pygame.transform.scale(pygame.image.load("frizz.png"), (154, 270))
        screen.blit(frizzle, (154, 200))

        
        screen.blit(introtext, (2, 10))
        screen.blit(intro2, (2, 40))
        screen.blit(tokentext, (2, 150))

        

        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player) 

        self.token_list.add(Token_Intro(500, 400))




class Level_01(Level):
    """ Definition for level 1. """
 
    def draw(self, screen):

        blood = pygame.Surface([50, 50])
        blood = pygame.transform.scale(pygame.image.load("bloodcell.jpg"), (800, 600))
        screen.blit(blood, (0, 0))

        scoretext = font.render(str("Kids collected: 0/5"), False, WHITE)
        screen.blit(scoretext, (500, 10))

        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)
    



    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        
        # Array with width, height, x, and y of platform
        level = [
            [220, 70, 500, 500, PINK, "bouncer"],
            [210, 70, 200, 400, DARK_RED, "bouncer"],
            [210, 70, 600, 300, DARK_RED, "bouncer"],
            [270, 20, 10, 240, PINK, "bouncer"],
            [50, 20, 20, 50, DARK_RED, "bouncer"],
            [50, 20, 400, 90, DARK_RED, "bouncer"],
            [50, 20, 650, 90, DARK_RED]
        ]
 
        # Go through the array above and add platforms
        for platform in level:
     
            block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        self.token_list.add(Token(650, 30))




    



class Level_02(Level):


    def draw(self, screen):

        blood = pygame.Surface([50, 50])
        blood = pygame.transform.scale(pygame.image.load("cells.jpg"), (800, 600))
        screen.blit(blood, (0, 0))


        level2text = font.render(str("Kids collected: 1/5"), False, WHITE)
        screen.blit(level2text, (500, 10))

        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)


    def __init__(self, player):
        super().__init__(player)

        level = [
            [120, 90, 130, 310, CELL_PINK],
            [100, 50, 500, 450, CELL_BLUE],
            [200, 50, 550, 200, CELL_PINK],
            [50, 25, 330, 50, CELL_BLUE],
            [50, 25, 50, 200, CELL_PINK],
            [25, 150, 550, 0, CELL_BLUE],
            [50, 20, 650, 90, CELL_BLUE]
        ]

        for platform in level:
            if platform[-1] == "bouncer":
                block = Bouncer(platform[0], platform[1], platform[4])
            else:
                block = Platform(platform[0], platform[1], platform[4])
    
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        
        self.token_list.add(Token_2(650,30))

class Level_03(Level):


    def draw(self, screen):
            blood = pygame.Surface([50, 50])
            blood = pygame.transform.scale(pygame.image.load("greenedit.jpg"), (800, 600))
            screen.blit(blood, (0, 0))

            level3text = font.render(str("Kids collected: 2/5"), False, WHITE)
            screen.blit(level3text, (500, 50))
           
            self.platform_list.draw(screen)
            self.bouncer_list.draw(screen)
            self.enemy_list.draw(screen)
            self.token_list.draw(screen)

            bouncetext = font.render(str("You can double jump on green blocks by tapping jump twice."), False, WHITE)

            screen.blit(bouncetext, (2, 10))


    def __init__(self, player):
        super().__init__(player)

    

        level = [
            [60, 90, 400, 250, GREEN, "bouncer"],
            [10, 50, 200, 400, GREEN, "bouncer"],
            [200, 50, 550, 130, GREEN, "bouncer"],
            [25, 50, 250, 50, DARK_GREEN, "bouncer"],
            [25, 50, 350, 20, CELL_BLUE, "regular"],
            [50, 25, 25, 100, GREEN, "bouncer"],
            [25, 130, 550, 0, GREEN, "regular"]

        
        ]

        for platform in level:
            if platform[-1] == "bouncer":
                block = Bouncer(platform[0], platform[1], platform[4])
            else:
                block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        
        self.token_list.add(Token_3(20,50))


class Level_04(Level):

    def draw(self, screen):

        blood = pygame.Surface([50, 50])
        blood = pygame.transform.scale(pygame.image.load("lung.jpg"), (800, 600))
        screen.blit(blood, (0, 0))

        level4text = font.render(str("Kids collected: 3/5"), False, WHITE)
        screen.blit(level4text, (500, 10))


        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)


    def __init__(self, player):
        super().__init__(player)

        level = [
            [120, 90, 130, 310, GREEN],
            [100, 50, 00, 450, DARK_GREEN],
            [200, 50, 550, 200, GREEN],
            [50, 25, 350, 60, DARK_GREEN],
            [50, 25, 50, 200, GREEN],
            [25, 150, 550, 0, DARK_GREEN],
            [20, 100, 250, 0, CELL_BLUE],
            [250, 1, 0, 0, BLACK],
            [15, 200, 450, 225, GREEN]
        ]


        for platform in level:
            if platform[-1] == "bouncer":
                block = Bouncer(platform[0], platform[1], platform[4])
            else:
                block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        
        self.token_list.add(Token_4(350,0))



class Level_05(Level):

    def draw(self, screen):

        blood = pygame.Surface([50, 50])
        blood = pygame.transform.scale(pygame.image.load("bcells.jpg"), (800, 600))
        screen.blit(blood, (0, 0))

        level5text = font.render(str("Kids collected: 4/5"), False, WHITE)
        screen.blit(level5text, (500, 10))


        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)


    def __init__(self, player):
        super().__init__(player)

        level = [
            [120, 90, 450, 260, CELL_BLUE],
            [100, 50, 350, 560, CELL_BLUE],
            [200, 50, 50, 220, CELL_BLUE],
            [50, 25, 150, 460, CELL_BLUE],
            [50, 25, 700, 60, CELL_BLUE],
            [25, 150, 55, 350, GREEN],
            [20, 100, 50, 64, CELL_BLUE],
        
        ]


        for platform in level:
            if platform[-1] == "bouncer":
                block = Bouncer(platform[0], platform[1], platform[4])
            else:
                block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        
        self.token_list.add(Token_5(700,0))

class Level_06(Level):
    """ Definition for level 1. """

    def draw(self, screen):
        screen.fill(BLACK)
        
        introtext = font.render(str("You did it! Thanks for your help."), False, WHITE)
    


        frizzle = pygame.Surface([50, 50])
        frizzle = pygame.transform.scale(pygame.image.load("frizz.png"), (154, 270))
        screen.blit(frizzle, (80, 150))

        pheobe = pygame.Surface([50, 50])
        pheobe = pygame.transform.scale(pygame.image.load("pheobe.png"), (153, 173))
        screen.blit(pheobe, (300, 200))

        carlos = pygame.Surface([50, 50])
        carlos = pygame.transform.scale(pygame.image.load("carlos.png"), (242, 172))
        screen.blit(carlos, (150, 200))

        asian = pygame.Surface([50, 50])
        asian = pygame.transform.scale(pygame.image.load("asian.png"), (139, 153))
        screen.blit(asian, (400, 200))

        brown = pygame.Surface([50, 50])
        brown = pygame.transform.scale(pygame.image.load("otherkid.png"), (100, 170))
        screen.blit(brown, (557, 200))

        arnold = pygame.Surface([50, 50])
        brown = pygame.transform.scale(pygame.image.load("arnold.png"), (153, 188))
        screen.blit(brown, (600, 200))
        
        
        screen.blit(introtext, (30, 60))
        

        

        self.platform_list.draw(screen)
        self.bouncer_list.draw(screen)
        self.enemy_list.draw(screen)
        self.token_list.draw(screen)
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player) 

    
 
def main():
    """ Main Program """
    pygame.init()


    music = pygame.mixer.Sound("lavendertown.wav")
   
    pygame.mixer.Sound.play(music)
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("The Magic School Bus: Find the Kids")
 
    # Create the player
    player = Player()
    bigbus = Player_2()
 
    # Create all the levels
    level_list = []

    level_list.append(Intro(bigbus))
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))
    level_list.append(Level_06(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    # player.rect.x = 340
    # player.rect.y = SCREEN_HEIGHT - player.rect.height

    player.rect.x = 0
    player.rect.y = 400

    active_sprite_list.add(player)

    
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet()
                    bullet.rect.x = player.rect.centerx
                    bullet.rect.y = player.rect.y
                    #add bullet to the list
                    active_sprite_list.add(bullet)
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        player_token_collision = pygame.sprite.spritecollide(player, current_level.token_list, True)

        if player_token_collision:
            current_level_no += 1
            current_level = level_list[current_level_no]
            player.rect.x = 0
            player.rect.y = SCREEN_HEIGHT - player.rect.height
            player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()