import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.game_over = False
        
        self.menu_screen()
        
        self.start_timer = pygame.time.get_ticks()
        self.timer = None
        self.final_timer = None
        
        self.level = Level(self.gameOver,self.game_over,self.start_timer)

        # sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.6)
        main_sound.play(loops = -1)
        
        self.run()
    
    def run(self):
        while not self.game_over:
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
    
    def gameOver(self):
        self.timer = pygame.time.get_ticks()
        self.final_timer = (self.timer - self.start_timer) // 60
        self.game_over = True
        run = True
        backgroundImage = pygame.transform.scale(pygame.image.load("graphics/menu_background.png"), (WIDTH,HEIGHT))
        
        while run:
            self.clock.tick(FPS)
            self.screen.blit(backgroundImage, (0,0))
            
            gameOverFont = pygame.font.Font(UI_FONT,60)
            font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
            
            gameOverText = gameOverFont.render("GAME OVER!!!", False, TEXT_COLOUR)
            timerText = font.render(f"You lasted: {round(self.final_timer,2)} seconds", False, TEXT_COLOUR)
            clickToRestart = font.render("Click to restart!", False, TEXT_COLOUR)
            
            self.screen.blit(gameOverText, ((WIDTH // 2) - (gameOverText.get_width() // 2),(HEIGHT // 2) - (gameOverText.get_height() * 3)))
            self.screen.blit(timerText, ((WIDTH // 2) - (timerText.get_width() // 2),(HEIGHT // 2) - (timerText.get_height() * 2)))
            self.screen.blit(clickToRestart, ((WIDTH // 2) - (clickToRestart.get_width() // 2),(HEIGHT // 2) - (clickToRestart.get_height() // 2)))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

    def menu_screen(self):
        run = True
        backgroundImage = pygame.transform.scale(pygame.image.load("graphics/menu_background.png"), (WIDTH,HEIGHT))
        
        while run:
            self.clock.tick(FPS)
            self.screen.blit(backgroundImage, (0,0))
            playFont = pygame.font.Font(UI_FONT,60)
            instructionsFont = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
            
            clickToPlay = playFont.render("Click to Play!", False, TEXT_COLOUR)
            controlsMove = instructionsFont.render("WASD or Arrows to move.", False, TEXT_COLOUR)
            controlsWeaponsSwitch = instructionsFont.render("Q to switch weapons.", False, TEXT_COLOUR)
            controlsWeaponAttack = instructionsFont.render("SPACE to malee attack.", False, TEXT_COLOUR)
            controlsMagicSwitch = instructionsFont.render("E to switch magic type.", False, TEXT_COLOUR)
            controlsMagicAttack = instructionsFont.render("LCTRL to use magic.", False, TEXT_COLOUR)
            controlsUpgradeMenu = instructionsFont.render("M to open and close upgrade menu.", False, TEXT_COLOUR)
            
            self.screen.blit(clickToPlay, ((WIDTH // 2) - (clickToPlay.get_width() // 2),(HEIGHT // 2) - (clickToPlay.get_height() // 2)))
            self.screen.blit(controlsMove, (25,25))
            self.screen.blit(controlsWeaponsSwitch, (25,50))
            self.screen.blit(controlsWeaponAttack, (25,75))
            self.screen.blit(controlsMagicSwitch, (25,100))
            self.screen.blit(controlsMagicAttack, (25,125))
            self.screen.blit(controlsUpgradeMenu, (25,150))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

if __name__ == '__main__':
    while True:
        game = Game()