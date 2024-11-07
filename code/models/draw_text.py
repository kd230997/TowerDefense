from pygame import font, Surface, draw


class DrawText:
    def __init__(
        self, display_surface: Surface, text, position, color, is_bordered=False
    ) -> None:
        self.font = font.Font(None, 36)
        self.position = position
        if is_bordered:
            position_x, position_y = position
            self.text_surface = self.font.render(text, True, color)
            text_size_width, text_size_height = self.text_surface.get_size()
            box_rect = draw.rect(
                display_surface,
                color,
                (position_x, position_y, text_size_width + 10, text_size_height + 10),
            )

            box_rect_x, box_rect_y = box_rect.topleft
        else:
            self.text_surface = self.font.render(text, True, color)
