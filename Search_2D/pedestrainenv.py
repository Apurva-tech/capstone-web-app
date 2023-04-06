class Env:
    def __init__(self):
        self.x_range = 51  # size of background
        self.y_range = 51
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
            obs.add((x - 1, i))

        # SET 2: Pedestrian Tracking Terrain (start = 2, 2 | goal = 48, 2)

        # Vertical barriers
        for i in range(2, 28):
            obs.add((5, i))
            obs.add((15, i))
            obs.add((25, i))
            obs.add((35, i))
            obs.add((45, i))

        # Horizontal barriers
        for i in range(6, 44):
            obs.add((i, 9))
            obs.add((i, 19))
            obs.add((i, 29))
            obs.add((i, 39))

        # Obstacle clusters
        obs.add((10, 13))
        obs.add((11, 12))
        obs.add((12, 12))
        obs.add((13, 12))
        obs.add((14, 12))
        obs.add((15, 13))
        obs.add((16, 14))
        obs.add((16, 15))
        obs.add((16, 16))
        obs.add((15, 17))
        obs.add((14, 18))
        obs.add((13, 18))
        obs.add((12, 18))
        obs.add((11, 17))

        obs.add((34, 33))
        obs.add((33, 34))
        obs.add((32, 35))
        obs.add((31, 36))
        obs.add((30, 37))
        obs.add((29, 38))
        obs.add((29, 39))
        obs.add((29, 40))
        obs.add((30, 41))
        obs.add((31, 42))
        obs.add((32, 43))
        obs.add((33, 44))
        obs.add((34, 45))

        obs.add((22, 18))
        obs.add((22, 19))
        obs.add((23, 19))
        obs.add((24, 19))
        obs.add((24, 18))
        obs.add((23, 17))

        obs.add((28, 32))
        obs.add((27, 31))
        obs.add((26, 30))
        obs.add((25, 29))
        obs.add((24, 28))
        obs.add((23, 27))
        obs.add((22, 26))
        obs.add((21, 25))
        obs.add((20, 24))
        obs.add((19, 23))
        obs.add((18, 22))
        obs.add((17, 21))
        obs.add((16, 20))
        obs.add((15, 19))

        return obs


def obs_map(self):
    """
    Initialize obstacles' positions
    :return: map of obstacles
    """

    x = self.x_range
    y = self.y_range
    obs = set()

    for i in range(x):
        obs.add((i, 0))
    for i in range(x):
        obs.add((i, y - 1))

    for i in range(y):
        obs.add((0, i))
    for i in range(y):
        obs.add((x - 1, i))

    # SET 2: Complex Pedestrian Tracking Terrain (start = 2, 2 | goal = 48, 2)
    for i in range(7, 24):  # left side obstacle
        obs.add((i, 4))
        obs.add((i, 5))
        obs.add((i, 6))
        obs.add((i, 7))
        obs.add((i, 8))
        obs.add((i, 9))
        obs.add((i, 10))
        obs.add((i, 11))
        obs.add((i, 12))
        obs.add((i, 13))
        obs.add((i, 14))
        obs.add((i, 15))
        obs.add((i, 16))
        obs.add((i, 17))
        obs.add((i, 18))
        obs.add((i, 19))
        obs.add((i, 20))
        obs.add((i, 21))
        obs.add((i, 22))

    for i in range(27, 44):  # right side obstacle
        obs.add((i, 4))
        obs.add((i, 5))
        obs.add((i, 6))
        obs.add((i, 7))
        obs.add((i, 8))
        obs.add((i, 9))
        obs.add((i, 10))
        obs.add((i, 11))
        obs.add((i, 12))
        obs.add((i, 13))
        obs.add((i, 14))
        obs.add((i, 15))
        obs.add((i, 16))
        obs.add((i, 17))
        obs.add((i, 18))
        obs.add((i, 19))
        obs.add((i, 20))
        obs.add((i, 21))
        obs.add((i, 22))

    for i in range(7, 24):  # top obstacle
        obs.add((24, i))
        obs.add((25, i))
        obs.add((26, i))
        obs.add((27, i))
        obs.add((28, i))
        obs.add((29, i))
        obs.add((30, i))
        obs.add((31, i))

    for i in range(7, 24):  # bottom obstacle
        obs.add((18, i))
        obs.add((19, i))
        obs.add((20, i))
        obs.add((21, i))
        obs.add((22, i))
        obs.add((23, i))
        obs.add((24, i))
        obs.add((25, i))

    for i in range(28, 44):  # diagonal obstacle
        obs.add((i, i-24))

    return obs
