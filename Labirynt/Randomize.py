import pygame


class RandomizeButton:
    def __init__(self, image, pos):
        self.image = image
        self.original_image = image.copy()  # Przechowaj kopię oryginalnego obrazka
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # Rect obrazka (dla detekcji kolizji)

    def Update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)  # Rysowanie obrazka na ekranie

    def CheckForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def ChangeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            # Pobierz maskę alfa obrazka
            alpha_mask = self.original_image.convert_alpha()

            # Ustaw kolor biały na obrazku tam, gdzie maska alfa zawiera kółko
            for x in range(alpha_mask.get_width()):
                for y in range(alpha_mask.get_height()):
                    pixel_color = alpha_mask.get_at((x, y))
                    if pixel_color[3] > 0:  # Sprawdź wartość kanału alfa (większa niż 0 oznacza nieprzezroczystość)
                        alpha_mask.set_at((x, y), (
                        255, 255, 255, pixel_color[3]))  # Ustaw piksel na biały (z zachowaniem wartości alfa)

            # Nałóż obrazek z kółkiem na obrazek główny, uwzględniając maskę alfa
            self.image.blit(alpha_mask, (0, 0))