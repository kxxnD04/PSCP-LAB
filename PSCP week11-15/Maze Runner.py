"""MAZE RUNNER
    >Read this<
    **This code was helped by chatgpt**
    So i suggest u to learn from others like Pubeth or Phumphuridon
    Thanks for read this message"""

def check_4direc(maze, current, visited, queue, path):
    """for 4 direc up,right,down and left"""
    directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]
    for dxx, dyy, direction in directions:
        xxx, yyy = current[0] + dxx, current[1] + dyy
        if 0 <= xxx < len(maze) and 0 <= yyy < len(maze[0])\
                and maze[xxx][yyy] != '*' and (xxx, yyy) not in visited:
            queue.append(((xxx, yyy), path + direction))
    return maze, current, visited, queue, path

def find_shortest_path(maze, start, y_positions):
    """calculate the shortest dis and path"""
    shortest_distance = float('inf')
    shortest_path = None
    for y_position in y_positions:
        queue = [(start, '')]
        visited = set()
        while queue:
            current, path = queue.pop(0)
            visited.add(current)
            if current == y_position:
                if len(path) < shortest_distance:
                    shortest_distance = len(path)
                    shortest_path = path
                break
            maze, current, visited, queue, path = check_4direc(
                maze, current, visited, queue, path)
    return shortest_path, shortest_distance

def maze_runner(maze):
    """main"""
    [start] = [(i, j) for i, row in enumerate(maze)
               for j, col in enumerate(row) if col == 'X']
    stop = [(i, j) for i, row in enumerate(maze)
            for j, col in enumerate(row) if col == 'Y']
    shortest_path, distance = find_shortest_path(maze, start, stop)
    print(shortest_path)
    print(distance)
    print('You will make it on time!' if distance*23 <=
          600 else "You won't make it on time.")

maze_runner([input() for _ in range(10)])
