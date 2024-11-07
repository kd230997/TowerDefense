from pygame import event as GameEvents, display, time, init, QUIT
import numpy as np

from models.configuration import Configuration
from models.map import MapEditor
from models.constant import CONSTANTS
from models.draw_text import DrawText


class Main:
    """
    My Main
    """

    def __init__(self):
        init()
        self.config = Configuration()
        self.game_state = CONSTANTS.GAME_STATE["PAUSE"]

        # Init
        self.center = (
            self.config.get_value("WIDTH") // 2,
            self.config.get_value("HEIGHT") // 2,
        )
        self.resolution = (
            self.config.get_value("WIDTH"),
            self.config.get_value("HEIGHT"),
        )
        self.running = True
        self.clock = time.Clock()
        self.display_surface = display.set_mode(self.resolution)
        self.menu_content = []
        for index, menu_item in enumerate(CONSTANTS.MENU_CONTENT):
            self.menu_content.append(
                DrawText(
                    self.display_surface,
                    menu_item,
                    (
                        self.config.get_value("WIDTH") // 2 - 100,
                        self.config.get_value("HEIGHT") // 2 + (index * 40) - 100,
                    ),
                    self.config.get_value("COLORS")["White"],
                    is_bordered=True,
                )
            )

        display.set_caption(self.config.get_value("WINDOW_TITLE"))

        # Object
        self.circles = []
        self.triangles = []
        self.map = MapEditor(
            np.zeros(
                (
                    self.config.get_value("WIDTH")
                    // self.config.get_value("TILE_SIZE"),
                    self.config.get_value("HEIGHT")
                    // self.config.get_value("TILE_SIZE"),
                )
            ),
            self.display_surface,
        )

    def draw_menu(self) -> None:
        self.display_surface.fill(self.config.get_value("COLORS")["SkyBlue"])
        for item in self.menu_content:
            self.display_surface.blit(item.text_surface, item.position)

    def draw_play(self) -> None:
        pass

    def imports(self):
        pass

    def event_loop(self) -> None:
        for event in GameEvents.get():
            if event.type == QUIT:
                self.running = False
                break

            if self.game_state == CONSTANTS.GAME_STATE["MAP_EDITOR"]:
                self.map.handle_map_events(event)

    def run(self):
        dt = self.clock.tick() / 1000
        print("Start Game!")
        while self.running:
            self.event_loop()
            if self.game_state == CONSTANTS.GAME_STATE["QUIT"]:
                self.running = False
            elif self.game_state == CONSTANTS.GAME_STATE["MAP_EDITOR"]:
                self.map.draw_map()
            elif self.game_state == CONSTANTS.GAME_STATE["PAUSE"]:
                self.draw_menu()
            elif self.game_state == CONSTANTS.GAME_STATE["PLAY"]:
                self.draw_play()

            display.update()

        quit()
