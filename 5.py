def calculate_initial_angle(hour, minute):
    # Hour hand moves 30 degrees per hour + 0.5 degrees per minute
    hour_angle = (hour % 12) * 30 + (minute * 0.5)
    # Minute hand moves 6 degrees per minute
    minute_angle = minute * 6
    # Calculate the absolute angle between hour and minute hands
    angle = abs(hour_angle - minute_angle)
    # Return the smaller of the two possible angles (interior or exterior)
    return min(angle, 360 - angle)

def calculate_cost(hour, minute, target_angle, A, B, X, Y):
    # Calculate the initial angle
    initial_angle = calculate_initial_angle(hour, minute)
    
    # The difference we need to cover to reach the target angle
    angle_diff = abs(target_angle - initial_angle)
    
    # Cost for moving hour hand clockwise and minute hand counterclockwise
    cost_1 = angle_diff * A * X + angle_diff * B * Y
    
    # Cost for moving hour hand counterclockwise and minute hand clockwise
    cost_2 = angle_diff * B * X + angle_diff * A * Y
    
    # Return the minimum cost of the two options
    return min(cost_1, cost_2)

def solve_clock_angle_problem(initial_time, Q, costs, queries):
    # Parse the initial time (hours:minutes format)
    hour, minute = map(int, initial_time.split(':'))
    
    # Extract cost values (A, B, X, Y)
    A, B, X, Y = costs
    
    total_cost = 0
    
    # Process each query
    for target_angle in queries:
        total_cost += calculate_cost(hour, minute, target_angle, A, B, X, Y)
    
    # Return the total minimum cost
    return total_cost

# Read the input
initial_time = input()  # e.g., "2:35"
Q = int(input())  # Number of queries

# Extract the costs from the next line
costs = list(map(int, input().split()))  # A, B, X, Y (all in a single line)

# Read each query as a single integer (ensuring correct input format)
queries = [int(input()) for _ in range(Q)]  # List of angles for each query

# Solve the problem
result = solve_clock_angle_problem(initial_time, Q, costs, queries)

# Output the result
print(result)
