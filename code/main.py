import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self,screen,clock):

        self.screen = screen
        self.clock = clock
        
        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.6)
        main_sound.play(loops = -1)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOUR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

def menu_screen():
    
    # general setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Zelda')
    clock = pygame.time.Clock()
    run = True
    backgroundImage = pygame.transform.scale(pygame.image.load("graphics/menu_background.png"), (WIDTH,HEIGHT))
    
    while run:
        clock.tick(FPS)
        screen.blit(backgroundImage, (0,0))
        playFont = pygame.font.Font(UI_FONT,60)
        instructionsFont = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        
        clickToPlay = playFont.render("Click to Play!", False, TEXT_COLOUR)
        controlsMove = instructionsFont.render("WASD or Arrows to move.", False, TEXT_COLOUR)
        controlsWeaponsSwitch = instructionsFont.render("Q to switch weapons.", False, TEXT_COLOUR)
        controlsWeaponAttack = instructionsFont.render("SPACE to malee attack.", False, TEXT_COLOUR)
        controlsMagicSwitch = instructionsFont.render("E to switch magic type.", False, TEXT_COLOUR)
        controlsMagicAttack = instructionsFont.render("LCTRL to use magic.", False, TEXT_COLOUR)
        
        screen.blit(clickToPlay, ((WIDTH // 2) - (clickToPlay.get_width() // 2),(HEIGHT // 2) - (clickToPlay.get_height() // 2)))
        screen.blit(controlsMove, (25,25))
        screen.blit(controlsWeaponsSwitch, (25,50))
        screen.blit(controlsWeaponAttack, (25,75))
        screen.blit(controlsMagicSwitch, (25,100))
        screen.blit(controlsMagicAttack, (25,125))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    
    game = Game(screen,clock)
    game.run()

if __name__ == '__main__':
    menu_screen()