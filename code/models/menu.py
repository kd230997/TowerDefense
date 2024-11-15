from pygame import event as GameEvents, MOUSEBUTTONDOWN, QUIT, mouse
import sys

from models import constant
from models.draw_text import DrawText
from models.configuration import Configuration


class Menu:
    def __init__(self, display_surface) -> None:
        self.display_surface = display_surface
        self.config = Configuration()
        self.menu_content = []
        for index, menu_item in enumerate(constant.MENU_CONTENT):
            self.menu_content.append(
                DrawText(
                    self.display_surface,
                    menu_item,
                    (
                        self.config.get_value("WIDTH") // 2 - 100,
                        self.config.get_value(
                            "HEIGHT") // 2 + (index * 40) - 100,
                    ),
                    self.config.get_value("COLORS")["White"],
                    is_bordered=True,
                    id=menu_item
                )
            )

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0] == True:
            mouse_pos = mouse.get_pos()

            for item in self.menu_content:
                if item.rect.collidepoint(mouse_pos):
                    return (constant.ACTION.CLICKED, item.id)

    def draw_menu(self) -> None:
        self.display_surface.fill(self.config.get_value("COLORS")["SkyBlue"])
        for item in self.menu_content:
            self.display_surface.blit(item.text_surface, item.position)
