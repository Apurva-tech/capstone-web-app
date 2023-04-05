class Env:
    def __init__(self):
        self.x_range = 51  # size of background
        self.y_range = 31
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
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        for i in range(10, 15):
            obs.add((i, 20))

        for i in range(23, 35):
            obs.add((i, 20))

        for i in range(5, 15):
            obs.add((i, 23))
        for i in range(5, 20):
            obs.add((i, 8))

        for i in range(25, 35):
            obs.add((i, 18))

        for i in range(39, 42):
            obs.add((i, 18))

        for i in range(5, 15):
            obs.add((i, 15))

        for i in range(0, 18):
            obs.add((20, i))

        for i in range(0, 20):
            obs.add((35, i))

        for i in range(23, 30):
            obs.add((16, i))

        for i in range(16):
            obs.add((40, i))

        return obs
