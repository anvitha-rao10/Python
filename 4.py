from collections import deque

def findMinimumMoves(board, start, end):
    n = len(board)
    m = len(board[0])
    visited = set()
    queue = deque([(start, 0)])  # (position, moves)
    visited.add(start)

    while queue:
        pos, moves = queue.popleft()
        x, y = pos

        # If we have reached the destination
        if pos == end:
            return moves

        # Get possible moves from the current position
        for next_pos in getPossibleMoves(board, pos, n, m):
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, moves + 1))

    return "Impossible"  # If destination cannot be reached

def getPossibleMoves(board, pos, n, m):
    x, y = pos
    moves = []

    # 1. If in the last row, we can move left and right
    if x == n - 1:
        if y > 0:  # Move left
            moves.append((x, y - 1))
        if y < m - 1:  # Move right
            moves.append((x, y + 1))
    
    # 2. Gravity: Slide down to the next stable cell
    if x < n - 1 and board[x + 1][y] == 1:  # If the next row has a lift
        # Slide down until we find a stable cell or the last row
        while x + 1 < n and board[x + 1][y] == 0:
            x += 1
        moves.append((x, y))  # Add new position after gravity

    # 3. Lifts: Use lifts to move upwards
    if board[x][y] == 1:  # Lift available at current cell
        for i in range(x - 1, -1, -1):  # Move upwards
            if board[i][y] == 1:  # Only move to cells with lifts
                moves.append((i, y))

    return moves

# Input handling
N, M = map(int, input().split())  # Board dimensions
board = [list(map(int, input().split())) for _ in range(N)]

start = tuple(map(int, input().split()))  # Start position (row, col)
end = tuple(map(int, input().split()))  # End position (row, col)

# Find the minimum moves
result = findMinimumMoves(board, start, end)
print(result)
