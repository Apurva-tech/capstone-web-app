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

        # SET 3: Aircraft Stealth Mission (start = 10, 3 | goal = 35, 2)
        # full
        for i in range(30):
            obs.add((1, i))
            obs.add((2, i))
            obs.add((3, i))

        # upper
        for i in range(7, 30):
            obs.add((4, i))
        for i in range(10, 30):
            obs.add((5, i))
        for i in range(12, 30):
            obs.add((6, i))
        for i in range(16, 30):
            obs.add((7, i))
        for i in range(18, 30):
            obs.add((8, i))
        for i in range(24, 30):
            obs.add((35, i))
            obs.add((36, i))
        for i in range(25, 30):
            obs.add((9, i))
            obs.add((23, i))
            obs.add((34, i))
        for i in range(26, 30):
            obs.add((21, i))
            obs.add((22, i))
            obs.add((24, i))
            obs.add((25, i))
            obs.add((32, i))
            obs.add((33, i))
            obs.add((37, i))
        for i in range(27, 30):
            obs.add((10, i))
            obs.add((20, i))
            obs.add((26, i))
            obs.add((31, i))
            obs.add((38, i))
            obs.add((39, i))
        for i in range(28, 30):
            obs.add((11, i))
            obs.add((19, i))
            obs.add((27, i))
            obs.add((28, i))
            obs.add((29, i))
            obs.add((30, i))
            obs.add((40, i))
        for i in range(29, 30):
            obs.add((12, i))
            obs.add((13, i))
            obs.add((14, i))
            obs.add((18, i))
            obs.add((41, i))

        # middle
        for i in range(3, 27):
            obs.add((43, i))
            obs.add((44, i))
            obs.add((45, i))
        for i in range(4, 12):
            obs.add((34, i))
        for i in range(4, 13):
            obs.add((35, i))
            obs.add((36, i))
        for i in range(4, 22):
            obs.add((37, i))
        for i in range(4, 24):
            obs.add((38, i))
            obs.add((39, i))
        for i in range(4, 26):
            obs.add((40, i))
            obs.add((41, i))
            obs.add((42, i))
        for i in range(5, 14):
            obs.add((10, i))
            obs.add((11, i))
        for i in range(6, 9):
            obs.add((7, i))
            obs.add((8, i))
        for i in range(6, 10):
            obs.add((9, i))
        for i in range(8, 23):
            obs.add((46, i))
        for i in range(9, 23):
            obs.add((22, i))
            obs.add((23, i))
            obs.add((24, i))
        for i in range(9, 24):
            obs.add((20, i))
            obs.add((21, i))
        for i in range(10, 24):
            obs.add((25, i))
            obs.add((26, i))
        for i in range(10, 25):
            obs.add((18, i))
            obs.add((19, i))
        for i in range(11, 25):
            obs.add((27, i))
            obs.add((30, i))
        for i in range(11, 26):
            obs.add((28, i))
            obs.add((29, i))
        for i in range(12, 19):
            obs.add((47, i))
        for i in range(12, 24):
            obs.add((31, i))
        for i in range(14, 27):
            obs.add((16, i))
            obs.add((17, i))
        for i in range(15, 23):
            obs.add((32, i))
            obs.add((33, i))
        for i in range(16, 22):
            obs.add((34, i))
        for i in range(19, 27):
            obs.add((15, i))
        for i in range(20, 26):
            obs.add((13, i))
            obs.add((14, i))
        for i in range(21, 24):
            obs.add((11, i))
            obs.add((12, i))

        # lower
        for i in range(2):
            obs.add((7, i))
            obs.add((8, i))
            obs.add((9, i))
            obs.add((10, i))
            obs.add((11, i))
        for i in range(3):
            obs.add((5, i))
            obs.add((6, i))
        for i in range(4):
            obs.add((4, i))
        for i in range(6):
            obs.add((20, i))
            obs.add((21, i))
            obs.add((22, i))
        for i in range(7):
            obs.add((18, i))
            obs.add((19, i))
            obs.add((23, i))
            obs.add((24, i))
        for i in range(8):
            obs.add((17, i))
            obs.add((25, i))
            obs.add((26, i))
            obs.add((27, i))
        for i in range(9):
            obs.add((15, i))
            obs.add((16, i))
            obs.add((28, i))
            obs.add((29, i))
            obs.add((30, i))
            obs.add((31, i))
        for i in range(10):
            obs.add((32, i))
        for i in range(11):
            obs.add((33, i))
        for i in range(13):
            obs.add((14, i))
        for i in range(15):
            obs.add((12, i))
        for i in range(18):
            obs.add((13, i))

        return obs
