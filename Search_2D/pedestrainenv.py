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
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        # Buildings
        for i in range(2, 10):
            for j in range(4, 15):
                obs.add((i, j))
        for i in range(2, 10):
            for j in range(20, 31):
                obs.add((i, j))
        for i in range(15, 23):
            for j in range(4, 15):
                obs.add((i, j))
        for i in range(15, 23):
            for j in range(20, 31):
                obs.add((i, j))
        for i in range(28, 36):
            for j in range(4, 15):
                obs.add((i, j))
        for i in range(28, 36):
            for j in range(20, 31):
                obs.add((i, j))
        for i in range(41, 49):
            for j in range(4, 15):
                obs.add((i, j))
        for i in range(41, 49):
            for j in range(20, 31):
                obs.add((i, j))

        # Roads
        for i in range(12):
            obs.add((i, 15))
        for i in range(12, 28):
            obs.add((i, 10))
        for i in range(28, 44):
            obs.add((i, 15))
        for i in range(12, 28):
            obs.add((i, 20))

        # Trees
        for i in range(3, 48, 5):
            for j in range(3, 49, 8):
                obs.add((i, j))

        return obs
