N = int(input())

wires = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    wires.append((x1, y1, x2, y2))

animals_input = input().split()
animals = {}
for entry in animals_input:
    name, threshold = entry.split(':')
    animals[name] = int(threshold)

touched_animal = input().strip()

intersections = {}

def min_cells(x1, y1, x2, y2, xi, yi):
    if x1 == x2:
        return min(abs(y1 - yi), abs(y2 - yi))
    elif y1 == y2:
        return min(abs(x1 - xi), abs(x2 - xi))
    return 0

for i in range(N):
    for j in range(i+1, N):
        x1, y1, x2, y2 = wires[i]
        x3, y3, x4, y4 = wires[j]
        
        xi, yi = (min(x1, x2) + max(x3, x4)) // 2, (min(y1, y2) + max(y3, y4)) // 2
        
        if (xi, yi) not in intersections:
            intersections[(xi, yi)] = []

        min_distance = float('inf')
        for (x1, y1, x2, y2) in wires:
            distance = min_cells(x1, y1, x2, y2, xi, yi)
            min_distance = min(min_distance, distance)
        
        intersections[(xi, yi)].append(min_distance)

total_voltage = 0
for (xi, yi), distances in intersections.items():
    count = len(distances)
    min_cells_at_intersection = min(distances)
    total_voltage += count * min_cells_at_intersection

touched_animal_threshold = animals[touched_animal]
animal_died = "Yes" if total_voltage >= touched_animal_threshold else "No"

num_animals_dying = sum(1 for threshold in animals.values() if threshold < total_voltage)
probability_of_death = num_animals_dying / len(animals)

print(animal_died)
print(f"{probability_of_death:.2f}")
