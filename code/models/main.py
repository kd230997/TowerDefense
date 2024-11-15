from pygame import event as GameEvents, display, time, init, QUIT
import numpy as np

from models.configuration import Configuration
from models.map import MapEditor
from models import constant
from models.menu import Menu


class Main:
    """
    My Main
    """

    def __init__(self):
        init()
        self.config = Configuration()
        self.game_state = constant.GAME_STATE.PAUSE

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
        display.set_caption(self.config.get_value("WINDOW_TITLE"))

        # Object
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

        # Menu
        self.menu = Menu(self.display_surface)

    def imports(self):
        pass

    def handle_layout_event(self, event):
        if self.game_state == constant.GAME_STATE.MAP_EDITOR:
            self.map.handle_events(event)
        elif self.game_state == constant.GAME_STATE.PAUSE:
            self.handle_event_action(self.menu.handle_events(event))

    def handle_event_action(self, event_action):
        # event_action will contain 2 value (action, id of object is interacted)
        if event_action is not None and event_action[0] is constant.ACTION.CLICKED and event_action[1] is constant.GAME_STATE.MAP_EDITOR:
            self.game_state = constant.GAME_STATE.MAP_EDITOR

    def event_loop(self) -> None:
        for event in GameEvents.get():
            if event.type == QUIT:
                self.running = False
            else:
                self.handle_layout_event(event)
                # if self.game_state == constant.GAME_STATE["PLAY"]:
                #     self.draw_play()
                #     break

    def run(self):
        dt = self.clock.tick() / 1000
        print("Start Game!")
        while self.running:
            if self.game_state == constant.GAME_STATE.QUIT:
                self.running = False
            elif self.game_state == constant.GAME_STATE.MAP_EDITOR:
                self.map.draw_map()
            elif self.game_state == constant.GAME_STATE.PAUSE:
                self.menu.draw_menu()
            elif self.game_state == constant.GAME_STATE.PLAY:
                self.draw_play()

            self.event_loop()
            display.update()

        quit()
