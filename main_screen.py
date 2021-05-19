import pygame

pygame.init()

# a function for making buttons
def button(screen, position, text):
    font = pygame.font.SysFont('timesnewroman', 50)
    text_render = font.render(text, 1, (150, 100, 100))
    x, y, width , height = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (0, 0, 150), (x, y), (x + width , y), 5)
    pygame.draw.line(screen, (0, 0, 150), (x, y - 2), (x, y + height), 5)
    pygame.draw.line(screen, (0, 0, 150), (x, y + height), (x + width , y + height), 5)
    pygame.draw.line(screen, (0, 0, 150), (x + width , y + height), [x + width , y], 5)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width , height))
    return screen.blit(text_render, (x, y))

# making the main screen back ground
main_screen = pygame.display.set_mode((640, 570))
pygame.display.set_caption( "Game Bot" )
BG_COLOR = (0, 0, 0)
main_screen.fill( BG_COLOR )



# main function for the screen
def mainmenu():

    pygame.draw.ellipse(main_screen, (180, 255, 180), [70, 20, 500, 150], 0)
    font = pygame.font.SysFont('timesnewroman', 50)
    text = font.render("John Nash's Demon",True,(150, 100, 100))
    textRect = text.get_rect()
    textRect.center = (320, 90)
    main_screen.blit(text,textRect)
    hex = button(main_screen,(282,200), "Hex")
    tic_tac_toe = button(main_screen, (207, 300), "Tic Tac Toe")
    domineering = button(main_screen, (193, 400), "Domineering")
    pick_the_brick = button(main_screen,(177,500), "Pick the Block")


    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # checks if the mouse has been clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tic_tac_toe.collidepoint(pygame.mouse.get_pos()):
                    pass
                elif domineering.collidepoint(pygame.mouse.get_pos()):
                    pass
                elif pick_the_brick.collidepoint(pygame.mouse.get_pos()):
                    pass
                elif hex.collidepoint(pygame.mouse.get_pos()):
                    pass
        pygame.display.update()


mainmenu()
