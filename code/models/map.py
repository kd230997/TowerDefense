from pygame import (
    K_F2,
    KEYDOWN,
    draw,
    Vector2,
    mouse,
    MOUSEMOTION,
    MOUSEBUTTONDOWN,
)

from models.configuration import Configuration


class MapEditor:
    def __init__(self, map_grid, display_surface):
        self.display_surface = display_surface
        self.map_grid = map_grid
        self.rotate_angle = 0

        self.config = Configuration()

        # Toggle
        self.toggleDrawing = True
        self.toggleGrid = self.config.get_value("ENABLE_GRID")

    def handle_map_events(self, event):
        if event.type == MOUSEMOTION and self.config.get_value("ENABLE_MOUSE_TRACK"):
            self.mouse_tracking()
        elif event.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0] == True:
            self.cell_onclick()
        elif event.type == KEYDOWN:
            if event.key == K_F2:
                print("F2 pressed")
                self.toggleGrid = not self.toggleGrid
                self.config.set_value("ENABLE_GRID", self.toggleGrid)

    def draw_circle(self, grid_position: tuple):
        (col, row) = grid_position

        draw.circle(
            self.display_surface,
            self.config.get_value("COLORS")["Red"],
            (
                col * self.config.get_value("TILE_SIZE")
                + (self.config.get_value("TILE_SIZE") / 2),
                row * self.config.get_value("TILE_SIZE")
                + +(self.config.get_value("TILE_SIZE") / 2),
            ),
            self.config.get_value("TILE_SIZE") / 4,
        )

    def draw_triangle(self, grid_position: tuple):
        triangle_margin = self.config.get_value("TILE_SIZE") // 6
        (col, row) = grid_position
        # Polygon points
        polygon_points = [
            Vector2(
                col * self.config.get_value("TILE_SIZE")
                + (self.config.get_value("TILE_SIZE") / 2),
                row * self.config.get_value("TILE_SIZE") + triangle_margin,
            ),
            Vector2(
                (
                    col * self.config.get_value("TILE_SIZE")
                    + self.config.get_value("TILE_SIZE")
                )
                - triangle_margin,
                (
                    row * self.config.get_value("TILE_SIZE")
                    + self.config.get_value("TILE_SIZE")
                )
                - triangle_margin,
            ),
            Vector2(
                col * self.config.get_value("TILE_SIZE") + triangle_margin,
                (
                    row * self.config.get_value("TILE_SIZE")
                    + self.config.get_value("TILE_SIZE")
                )
                - triangle_margin,
            ),
        ]

        # Calculate the center of the polygon
        center_x = sum(p.x for p in polygon_points) / len(polygon_points)
        center_y = sum(p.y for p in polygon_points) / len(polygon_points)
        center = Vector2(center_x, center_y)

        # Translate points to origin, rotate, and translate back
        rotated_points = []
        for point in polygon_points:
            translated_point = point - center
            rotated_point = translated_point.rotate(self.rotate_angle)
            final_point = rotated_point + center
            rotated_points.append(final_point)

        # Draw the rotated polygon
        draw.polygon(
            self.display_surface, self.config.get_value("COLORS")["Red"], rotated_points
        )

    def drawing_grid(self):
        if self.config.get_value("ENABLE_GRID") == True:
            # Draw grid
            for line in range(
                1,
                int(self.config.get_value("WIDTH") / self.config.get_value("TILE_SIZE"))
                + 1,
            ):
                draw.line(
                    self.display_surface,
                    self.config.get_value("COLORS")["Black"],
                    (line * self.config.get_value("TILE_SIZE"), 0),
                    (
                        line * self.config.get_value("TILE_SIZE"),
                        self.config.get_value("HEIGHT"),
                    ),
                )

            for line in range(
                1,
                int(
                    self.config.get_value("HEIGHT") / self.config.get_value("TILE_SIZE")
                )
                + 1,
            ):
                draw.line(
                    self.display_surface,
                    self.config.get_value("COLORS")["Black"],
                    (0, line * self.config.get_value("TILE_SIZE")),
                    (
                        self.config.get_value("WIDTH"),
                        line * self.config.get_value("TILE_SIZE"),
                    ),
                )

    def draw_map(self):
        self.display_surface.fill(self.config.get_value("COLORS")["White"])

        # Rotation angle
        self.rotate_angle += 0.1
        self.drawing_grid()

        for colIndex, col in enumerate(self.map_grid):
            for rowIndex, row in enumerate(col):
                if (
                    self.map_grid[colIndex][rowIndex]
                    == self.config.get_value("MAP_OBJECT")["circle"]
                ):
                    self.draw_circle((colIndex, rowIndex))
                    continue

                if (
                    self.map_grid[colIndex][rowIndex]
                    == self.config.get_value("MAP_OBJECT")["rectangle"]
                ):
                    self.draw_triangle((colIndex, rowIndex))
                    continue

    def cell_onclick(self):
        mouse_x, mouse_y = mouse.get_pos()
        grid_x, grid_y = (
            mouse_x // self.config.get_value("TILE_SIZE"),
            mouse_y // self.config.get_value("TILE_SIZE"),
        )

        if self.map_grid[grid_x][grid_y] != 0:
            print("Already pointed!")
            return

        if self.toggleDrawing:
            self.map_grid[grid_x][grid_y] = self.config.get_value("MAP_OBJECT")[
                "circle"
            ]
        else:
            self.map_grid[grid_x][grid_y] = self.config.get_value("MAP_OBJECT")[
                "rectangle"
            ]

        self.toggleDrawing = not self.toggleDrawing

    def mouse_tracking(self):
        mouse_x, mouse_y = mouse.get_pos()
        print(
            f"Mouse: ({mouse_x // self.config.get_value("TILE_SIZE")}, {mouse_y // self.config.get_value("TILE_SIZE")}), coordinate ({mouse_x}, {mouse_y})"
        )
