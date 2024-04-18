from tiles import TilesNode
from queue import PriorityQueue


def heuristic(node: TilesNode) -> int:
    """
    Evaluate the heuristic value of the current node.
    This implementation simply counts the number of misplaced tiles.

    Returns
    -------
    heuristic_value : int
        The heuristic value of the current node.
    """
    goal_state = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

    misplaced_tiles = sum(1 for i in range(len(node.state)) for j in range(len(node.state[i])) if node.state[i][j] != goal_state[i][j])

    return misplaced_tiles
                          


def AStar(root, heuristic: callable) -> TilesNode:
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((0, counter, root))
    explored = set()
    g_score = {root: 0}
    f_score = {root: heuristic(root)}

    while not unexplored.empty():
       _, _, current_node = unexplored.get()

       if current_node.is_goal():
           return current_node
       
       explored.add(current_node)

       for child_node in current_node.get_children():
           if child_node in explored:
               continue
           
           temp_g_score = g_score[current_node] + 1

           if child_node not in g_score or temp_g_score < g_score[child_node]:
               child_node.parent = current_node
               g_score[child_node] = temp_g_score
               f_score[child_node] = temp_g_score + heuristic(child_node)
               counter += 1
               unexplored.put((f_score[child_node], counter, child_node))

    return None  # return None if no path was found
