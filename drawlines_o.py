import random as r

def create_lines(total: int, min: float, max: float) -> tuple:
    lines_set = []
    for _ in range(total):
        line = []
        for __ in range(4):
            line.append(r.uniform(min, max))
        line = tuple(line)
        lines_set.append(line)
    lines_set = tuple(lines_set)

    return lines_set


def rectangular_filter(target: tuple, x1: float, y1: float, x2: float, y2: float) -> tuple:
    # I love sets
    satisfied_lines = []
    v = tuple([x1, y1, x2, y2])
    for u in target:
        if v[0] < u[0] < v[2] and v[0] < u[2] < v[2] \
            and v[1] < u[1] < v[3] and v[1] < u[3] < v[3]:
            satisfied_lines.append(u)
    satisfied_lines = tuple(satisfied_lines)
    
    return satisfied_lines

def tester(sample_size: int):
    unfiltered = create_lines(total=sample_size, min=0, max=1000)
    filtered = rectangular_filter(target=unfiltered, x1=100, y1=100, x2=400, y2=400)

    return unfiltered, filtered

if __name__ == "__main__":
    lines = create_lines(total=20, min=3, max=9)
    print(lines)
    print(len(lines))
    
    filtered_lines = rectangular_filter(target=lines, x1=3, y1=3, x2=8, y2=8)
    print(filtered_lines)
    print(len(filtered_lines))