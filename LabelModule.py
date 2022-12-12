import pygame

# copied from Daniel's example

class Label:
    def __init__(self, text, pos, size, colour):
        self.text = text
        self.pos = pos
        pygame.font.init()
        # This font is downloaded from the website: https://freefontsfamily.com
        self.font = pygame.font.Font('./fonts/times new roman bold italic.ttf', size)
        self.font_colour = pygame.Color(colour)

    def draw(self, screen):
        img = self.font.render(self.text, True, self.font_colour)
        screen.blit(img, self.pos)
