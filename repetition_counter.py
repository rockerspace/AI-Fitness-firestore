import numpy as np

def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180 else angle

class RepCounter:
    def __init__(self):
        self.count = 0
        self.direction = None  # 'down' or 'up'

    def update(self, angle):
        if angle < 90:
            if self.direction != 'down':
                self.direction = 'down'
        if angle > 160:
            if self.direction == 'down':
                self.direction = 'up'
                self.count += 1
        return self.count
