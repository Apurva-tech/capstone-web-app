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

        for i in range(10, 30):
            obs.add((i, 25))
        for i in range(10, 30):
            obs.add((i, 20))

        for i in range(0, 18):
            obs.add((10, i))
        for i in range(0, 18):
            obs.add((15, i))
        for i in range(0, 18):
            obs.add((20, i))
        for i in range(0, 18):
            obs.add((25, i))
        for i in range(0, 18):
            obs.add((30, i))

        for i in range(12, 30):
            obs.add((32, i))
        for i in range(12, 30):
            obs.add((35, i))
        for i in range(12, 30):
            obs.add((37, i))

        for i in range(35, 45):
            obs.add((i, 10))
        for i in range(35, 45):
            obs.add((i, 5))
        return obs
