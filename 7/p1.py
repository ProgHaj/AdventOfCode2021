import numpy as np
import json

inp = np.array(json.load(open("input", "r")))
val = round(np.mean(inp))
print(int(sum(abs(inp - val))))