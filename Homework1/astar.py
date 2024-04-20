from tiles import TilesNode
from queue import PriorityQueue
from typing import List


def heuristic(node: TilesNode) -> int:
    """
    Evaluate the heuristic value of the current node.
    This implementation simply counts the number of misplaced tiles.

    Returns
    -------
    heuristic_value : int
        The heuristic value of the current node.
    """
    goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    h_value = 0

    """Comparing the goal to the current state and counting the number of misplaced tiles"""

    # using manhattan distance 
    for i in range(len(node.state)):
        for j in range(len(node.state[i])):
            cur_tile = node.state[i][j]

            if cur_tile != 0:  # Ignoring the empty space
                goal_row, goal_col = divmod(cur_tile - 1, len(node.state))  
                #calculates the manhattan distance by |row1 - goalRow| + |col2 - goalCol|
                h_value += abs(i - goal_row) + abs(j - goal_col) 
    return h_value
                          

def AStar(root: TilesNode, heuristic: callable) -> List[TilesNode]:
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((0, counter, root))
    explored = set()
    g_score = {root: 0}
    f_score = {root: heuristic(root)}

    while not unexplored.empty():
        _, _, cur_node = unexplored.get()

        if cur_node.is_goal():
            new_path = []
            while cur_node:
                new_path.append(cur_node)
                cur_node = cur_node.parent
            return new_path[::-1] 
        
        explored.add(cur_node)

        for child_node in cur_node.get_children():
            if child_node in explored:
                continue

            temp_g_score = g_score[cur_node] + 1

            if child_node not in g_score or temp_g_score < g_score[child_node]:
                child_node.parent = cur_node
                g_score[child_node] = temp_g_score
                f_score[child_node] = temp_g_score + heuristic(child_node)
                counter += 1
                unexplored.put((f_score[child_node], counter, child_node))

    return [] 
