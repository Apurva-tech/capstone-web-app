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

        # SET 2: Agriculture Field (start = 2, 2 | goal = 48, 2)
        for i in range(27):  # bottom touching lower boundary
            obs.add((4, i))
            obs.add((5, i))
            obs.add((14, i))
            obs.add((15, i))
            obs.add((24, i))
            obs.add((25, i))
            obs.add((34, i))
            obs.add((35, i))
            obs.add((44, i))
            obs.add((45, i))

        for i in range(4, 30):  # top touching upper boundary
            obs.add((9, i))
            obs.add((10, i))
            obs.add((19, i))
            obs.add((20, i))
            obs.add((29, i))
            obs.add((30, i))
            obs.add((39, i))
            obs.add((40, i))

        return obs
