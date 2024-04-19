from copy import deepcopy


class TilesNode:
    """A class to represent a node in the Fifteen-Tile Puzzle.

    Parameters
    ----------
    state: list[list[int]]
        An array (list of list) of ints representing the initial state of the puzzle.
        This array should contain integers from 0 to 15 separated by spaces.
        The integer 0 represents the empty space in the puzzle.

    parent : Node, optional
        The parent node of the current node. The default is None.
    """

    def __init__(
        self,
        state,
        parent=None,
    ):
        self.state = state
        self.parent = parent

    def is_goal(self) -> bool:
        
        goal_state = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,0]]
        return self.state == goal_state

    def find_empty_space(self) -> tuple[int, int]:
        """Helper function to find the empty space in the current state.

        You don't need to use this function, but it may be helpful.

        Returns
        -------
        empty_row : int
            The row index of the empty space.

        empty_col : int
            The column index of the empty space.
        """
        for i, row in enumerate(self.state):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j

    def swap_tiles(self, row1, col1, row2, col2):
        """
        Helper function to swap two tiles in the current state.

        You don't need to use this function, but it may be helpful.

        """
        new_state = deepcopy(self.state)
        new_state[row1][col1], new_state[row2][col2] = (
            new_state[row2][col2],
            new_state[row1][col1],
        )
        return new_state

    def get_children(self) -> list["TilesNode"]:
        children = []
        empty_row, empty_col = self.find_empty_space()

        for down_row, down_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            new_row, new_col = empty_row + down_row, empty_col + down_col
            
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state[0]):
                new_state = self.swap_tiles(empty_row, empty_col, new_row, new_col)
                # Create a new TilesNode object from the new state
                child_node = TilesNode(new_state, parent=self)
                children.append(child_node)

        return children



    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def get_path(self) -> list["TilesNode"]:
        """
        Once a goal node is found, this function can be used to backtrack.

        Be sure to set .parent correctly when creating child nodes for this to work.

        You don't need to use this function, but it may be helpful.
        """
        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent
        return path[::-1]

    def __eq__(self, other):
        if isinstance(other, TilesNode):
            return self.state == other.state
        return False

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def is_solvable(self):
        """
        Check if the current state is solvable.
        In a solvable state, the number of inversions must be even.

        You don't need to use this function, but it may be helpful.

        From piazza
        """
        flat_state = [tile for row in self.state for tile in row]

        inversions = 0
        for i in range(0, len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] != 0 and flat_state[j] != 0 and flat_state[i] > flat_state[j]:
                    inversions += 1

        empty_row, _ = self.find_empty_space()

        # n is even
        if ((len(self.state)) % 2 == 0):
            return (inversions + empty_row) % 2 == 1
        else: # n is odd
            return (inversions) % 2 == 0
