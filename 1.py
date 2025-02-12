def min_cost(s, cost):
    n = len(s)
    
    # Cost to convert to alternating pattern starting with '0' (Pattern 1: 010101...)
    cost_for_pattern1 = 0
    # Cost to convert to alternating pattern starting with '1' (Pattern 2: 101010...)
    cost_for_pattern2 = 0
    
    # Iterate through the string and calculate cost for both patterns
    for i in range(n):
        # Expected characters for the two patterns
        expected_char_for_pattern1 = '0' if i % 2 == 0 else '1'
        expected_char_for_pattern2 = '1' if i % 2 == 0 else '0'
        
        # If the character doesn't match the expected character in pattern 1
        if s[i] != expected_char_for_pattern1:
            cost_for_pattern1 += cost[i]
        
        # If the character doesn't match the expected character in pattern 2
        if s[i] != expected_char_for_pattern2:
            cost_for_pattern2 += cost[i]
    
    # Return the minimum cost to achieve either pattern
    return min(cost_for_pattern1, cost_for_pattern2)

# Input
s = input().strip()  # Binary string
cost = list(map(int, input().strip().split()))  # List of costs

# Output the result
print(min_cost(s, cost))
