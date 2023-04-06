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

        # Add rocky terrain around the edges of the map
        for i in range(x):
            obs.add((i, 0))
            obs.add((i, y-1))
        for i in range(y):
            obs.add((0, i))
            obs.add((x-1, i))

        # Add hills and valleys
        for i in range(5, x-5, 10):
            for j in range(5, y-5, 12):
                if i % 2 == 0:
                    obs.add((i, j))
                    obs.add((i, j+1))
                    obs.add((i+1, j))
                else:
                    obs.add((i+1, j+1))
                    obs.add((i+1, j))
                    obs.add((i, j+1))
            for j in range(6, y-6, 14):
                obs.add((i, j))
                obs.add((i, j+1))
                obs.add((i, j+2))
                obs.add((i+1, j+1))
                obs.add((i+2, j))

        # Add craters and boulders on the surface
        for i in range(3, x-3, 8):
            for j in range(3, y-3, 10):
                obs.add((i, j))
                obs.add((i+1, j+1))
                obs.add((i+2, j+2))
                obs.add((i+3, j+3))
                obs.add((i+4, j+4))
                obs.add((i+5, j+5))
                obs.add((i+6, j+6))
                obs.add((i+7, j+7))

        return obs
