import pygame

class ScoreBoard:
    def __init__(self, font_size=30, position=(10, 10), lives=3):
        self.score = 0
        self.lives = lives
        self.font = pygame.font.SysFont("Arial", font_size)
        self.position = position

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        lives_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        
        screen.blit(score_text, self.position)
        screen.blit(lives_text, (self.position[0], self.position[1] + 40))

    def increase_score(self, points):
        self.score += points

    def decrease_life(self):
        self.lives -= 1

    def reset(self):
        self.score = 0
        self.lives = 3
        