import pygame
from components.config import SCREEN_WIDTH, SCREEN_HEIGHT


def game_over_screen(screen, current_score, highscore):
    font = pygame.font.SysFont("Arial", 30)
    small_font = pygame.font.SysFont("Arial", 22)

    game_over_text = font.render("Game Over", True, (255, 0,0))
    current_score_text = small_font.render(f"Score: {current_score}", True, (255, 255, 255))
    highscore_text = small_font.render(f"Highscore: {highscore}", True, (255, 255, 255))

    # define button rectangles
    restart_rect = pygame.Rect(150, 500, 120, 50)
    quit_rect = pygame.Rect(350, 500, 120, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if restart_rect.collidepoint(mouse_pos):
                    return "restart"
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    return "quit"
                
        screen.fill(pygame.Color("black"))

        # draw texts
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 300))
        screen.blit(current_score_text, (SCREEN_WIDTH // 2 - current_score_text.get_width() // 2, 350))
        screen.blit(highscore_text, (SCREEN_WIDTH // 2 - highscore_text.get_width() // 2, 400))

        # draw buttons
        pygame.draw.rect(screen, (0,255,0), restart_rect)
        pygame.draw.rect(screen, (255, 0, 0), quit_rect)

        restart_text = small_font.render("Restart", True, (0,0,0))
        quit_text = small_font.render("Quit", True, (0,0,0))
        screen.blit(restart_text, (restart_rect.centerx - restart_rect.get_width() // 2,
                                   restart_rect.centery - restart_rect.get_height() // 2))
        screen.blit(quit_text, (quit_rect.centerx - quit_rect.get_width() // 2,
                                quit_rect.centery -  quit_rect.get_height() // 2))
        
        pygame.display.flip()



