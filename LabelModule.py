import pygame

# copied from Daniel's example


class Label:
    def __init__(self, text, pos, size, colour):
        self.text = text
        self.pos = pos
        pygame.font.init()
        self.font = pygame.font.Font('./fonts/times new roman bold italic.ttf', size)
        # self.font = pygame.font.SysFont(None, size)
        self.font_colour = pygame.Color(colour)

    def draw(self, screen):
        img = self.font.render(self.text, True, self.font_colour)
        screen.blit(img, self.pos)
