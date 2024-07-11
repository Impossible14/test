def read_circle():
    a = open('circle.txt')
    x, y = map(int, a.readline().split())
    radius = int(a.readline().strip())
    return (x, y, radius)


def read_points():
    b = open('dot.txt')
    points = [tuple(map(int, line.split())) for line in b]
    return points


def func(circle, point):
    x0, y0, radius = circle
    x, y = point
    distance = (x - x0) ** 2 + (y - y0) ** 2
    radius = radius ** 2

    if distance < radius:
        return 1
    elif distance == radius:
        return 0
    else:
        return 2


def main():
    circle = read_circle()
    points = read_points()

    for point in points:
        position = func(circle, point)
        print(position)


if __name__ == "__main__":
    main()
