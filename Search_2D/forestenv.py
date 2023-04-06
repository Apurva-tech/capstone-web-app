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

        # Add trees around the edges of the forest
        for i in range(x):
            obs.add((i, 0))
            obs.add((i, y-1))
        for i in range(y):
            obs.add((0, i))
            obs.add((x-1, i))

        # Add trees in the middle of the forest
        for i in range(2, x-2, 5):
            for j in range(2, y-2, 6):
                obs.add((i, j))
                obs.add((i+1, j))
                obs.add((i, j+1))
                obs.add((i+1, j+1))

        return obs
