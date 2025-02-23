import pygame

class ScoreBoard:
    def __init__(self, font_size=30, position=(10, 10)):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", font_size)
        self.position = position

    def increase_score(self, points):
        self.score += points

    def draw(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, (255,255,255))
        screen.blit(score_surface, self.position)