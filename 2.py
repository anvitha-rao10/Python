import math

def rotate_point(point, angle):
    x, y = point
    rad = angle * math.pi / 180
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

def find_min_plank_size(points):
    min_area = float('inf')
    best_width, best_height = 0, 0

    for angle in range(0, 360, 45):
        rotated_points = [rotate_point(point, angle) for point in points]

        min_x, max_x = float('inf'), -float('inf')
        min_y, max_y = float('inf'), -float('inf')

        for x, y in rotated_points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

        width = max_x - min_x
        height = max_y - min_y
        area = width * height

        if area < min_area:
            min_area = area
            best_width, best_height = width, height

    return int(best_width) + 1, int(best_height) + 1

# Input
N = int(input())
points = []
for _ in range(N):
    x, y = map(float, input().split())
    points.append((x, y))

# Find the minimum plank size
width, height = find_min_plank_size(points)

# Print the result
print(width, height)