import numpy as np
import random as r

def create_lines(total: int, min: float, max: float) -> np.array:
    lines_set = []
    for _ in range(total):
        line = []
        for __ in range(4):
            line.append(r.uniform(min, max))
        line = np.array(line)
        lines_set.append(line)
    lines_set = np.array(lines_set)

    return lines_set


def rectangular_filter(target: np.array, x1: float, y1: float, x2: float, y2: float) -> np.array:
    # I love sets
    satisfied_lines = []
    v = np.array([x1, y1, x2, y2])
    for u in target:
        if v[0] < u[0] < v[2] and v[0] < u[2] < v[2] \
            and v[1] < u[1] < v[3] and v[1] < u[3] < v[3]:
            satisfied_lines.append(u)
    satisfied_lines = np.array(satisfied_lines)
    
    return satisfied_lines



if __name__ == "__main__":
    lines = create_lines(total=20, min=3, max=9)
    print(lines)
    print(lines.shape)
    
    filtered_lines = rectangular_filter(target=lines, x1=3, y1=3, x2=8, y2=8)
    print(filtered_lines)
    print(filtered_lines.shape)

  