class Configuration:
    # Common
    #         Low-Resolution: 640x480, 800x600
    # Medium-Resolution: 1024x768, 1280x720 (720p)
    # High-Resolution: 1920x1080 (1080p), 2560x1440 (1440p)
    _global_config = None

    def __new__(cls):
        if cls._global_config is None:
            cls._global_config = super().__new__(cls)
        return cls._global_config

    def __init__(self):
        self._global_config = {
            "COLORS": {
                "Red": (255, 0, 0),
                "Green": (0, 255, 0),
                "Blue": (0, 0, 255),
                "White": (255, 255, 255),
                "Black": (0, 0, 0),
                "SkyBlue": (32, 228, 201),
            },
            "ENABLE_MOUSE_TRACK": False,
            "ENABLE_GRID": True,
            # Test
            "WINDOW_TITLE": "Zombie Defenders",
            "WIDTH": 800,
            "HEIGHT": 600,
            # Map
            "TILE_MAPS": (40, 20),
            "TILE_SIZE": 40,
            ## Map object
            "MAP_OBJECT": {
                "circle": 1,
                "rectangle": 2,
            },
        }

    def get_value(self, key):
        return self._global_config.get(key, None)

    def set_value(self, key, value):
        self._global_config[key] = value
