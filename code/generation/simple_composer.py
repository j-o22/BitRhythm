# Simple algorithmic composer

import random

scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
melody = [random.choice(scale) for _ in range(16)]
print('Generated Melody:', melody)