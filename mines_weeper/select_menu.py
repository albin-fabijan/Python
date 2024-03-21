import pygame

from .paths import Paths
from .window import Window


class SelectMenu(Window):
    def __init__(self):
        super().__init__(350, 350)
        pygame.display.set_caption("Menu de Sélection de Difficulté")
        self.font = pygame.font.Font(None, 36)

        self.player_name = ""
        self.PLAYER_NAME_LENGTH = 8

        self.main_loop()

    def main_loop(self):
        while self.running:
            (
                player_name_rect,
                easy_button_rect,
                normal_button_rect,
                expert_button_rect
            ) = self.get_rects()

            self.input_loop(
                player_name_rect,
                easy_button_rect,
                normal_button_rect,
                expert_button_rect
            )
            self.display(
                player_name_rect,
                easy_button_rect,
                normal_button_rect,
                expert_button_rect
            )

    def load_images(self):
        p = Paths()
        image = pygame.image.load(p.select_sprite("menu_background.png"))
        scale = image.get_size()
        background_img = pygame.transform.scale(
            image ,
            (self.WIDTH, self.HEIGHT)
        )

        image = pygame.image.load(p.select_sprite("button.png"))
        scale = image.get_size()
        button_img = pygame.transform.scale(
            image,
            (int(scale[0] * 2), int(scale[1]* 2))
        )

        image = pygame.image.load(p.select_sprite("text_field.png"))
        scale = image.get_size()
        player_name_img = pygame.transform.scale(
            image,
            (int(scale[0] * 2), int(scale[1] * 2))
        )

        return background_img, button_img, player_name_img

    def get_rects(self):
        background_img, button_img, player_name_img = self.load_images()

        player_name_rect = player_name_img.get_rect(
            center=(
                self.WIDTH // 2,
                self.HEIGHT // 2 - 60
            )
        )

        easy_button_rect = button_img.get_rect(
            center=(
                self.WIDTH // 2,
                self.HEIGHT // 2 
            )
        )
        normal_button_rect = button_img.get_rect(
            center=(
                self.WIDTH // 2,
                self.HEIGHT // 2 + 50
            )
        )
        expert_button_rect = button_img.get_rect(
            center=(
                self.WIDTH // 2,
                self.HEIGHT // 2 + 100
            )
        )

        return player_name_rect, easy_button_rect, normal_button_rect, expert_button_rect

    def input_loop(
        self,
        player_name_rect,
        easy_button_rect,
        normal_button_rect,
        expert_button_rect
    ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

            if event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z:
                    if len(self.player_name) == self.PLAYER_NAME_LENGTH:
                        continue
                    self.player_name = (
                        self.player_name
                        + pygame.key.name(event.key).upper()
                    )
                if event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if easy_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Difficulté sélectionnée : 1")
                    return 1
                    self.running = False
                    break

                elif normal_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Difficulté sélectionnée : 1")
                    return 2
                    self.running = False
                    break

                elif expert_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Difficulté sélectionnée : 1")
                    return 3
                    self.running = False
                    break

    def display(
        self,
        player_name_rect,
        easy_button_rect,
        normal_button_rect,
        expert_button_rect
    ):
        DARK = (0, 0, 0)
        BRUN = (200, 173, 127)

        background_img, button_img, player_name_img = self.load_images()

        self.screen.fill(BRUN)
        self.screen.blit(background_img, (0, 0))

        self.screen.blit(player_name_img, player_name_rect)
        self.draw_text(
            "Entrez votre nom :",
            self.font,
            DARK,
            self.screen,
            self.WIDTH // 2,
            self.HEIGHT // 2 - 120
        )
        self.draw_text(
            self.player_name,
            self.font,
            DARK,
            self.screen,
            self.WIDTH // 2,
            self.HEIGHT // 2 - 75
        )

        self.screen.blit(button_img, easy_button_rect)
        self.draw_text(
            "Facile",
            self.font,
            DARK,
            self.screen,
            self.WIDTH // 2,
            self.HEIGHT // 2
        )

        self.screen.blit(button_img, normal_button_rect)
        self.draw_text(
            "Normal",
            self.font,
            DARK,
            self.screen,
            self.WIDTH // 2,
            self.HEIGHT // 2 + 50
        )

        self.screen.blit(button_img, expert_button_rect)
        self.draw_text(
            "Expert",
            self.font,
            DARK,
            self.screen,
            self.WIDTH // 2,
            self.HEIGHT // 2 + 100
        )

        pygame.display.flip()
