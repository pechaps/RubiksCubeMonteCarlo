

class RubiksCube:
    """
    Represents a 2x2 Rubik's Cube.
    The cube is initially on the solved state.
    Method performs the possible movement on the initial state.
    """
    def __init__(self):
        self.state = [
            [["g", "g"], ["g", "g"]],
            [["r", "r"], ["r", "r"]],
            [["b", "b"], ["b", "b"]],
            [["o", "o"], ["o", "o"]],
            [["w", "w"], ["w", "w"]],
            [["y", "y"], ["y", "y"]],
        ]

    def move_right(self):
        (
            self.state[0][0][1],
            self.state[0][1][1],
            self.state[5][0][1],
            self.state[5][1][1],
            self.state[2][0][0],
            self.state[2][1][0],
            self.state[4][1][1],
            self.state[4][0][1],
            self.state[1][0][0],
            self.state[1][1][0],
            self.state[1][1][1],
            self.state[1][0][1],
        ) = (
            self.state[5][0][1],
            self.state[5][1][1],
            self.state[2][1][0],
            self.state[2][0][0],
            self.state[4][1][1],
            self.state[4][0][1],
            self.state[0][1][1],
            self.state[0][0][1],
            self.state[1][1][0],
            self.state[1][1][1],
            self.state[1][0][1],
            self.state[1][0][0],
        )

    def move_right_inverse(self):
        for _ in range(3):
            self.move_right()

    def move_up(self):
        (
            self.state[0][0][0],
            self.state[0][0][1],
            self.state[1][0][0],
            self.state[1][0][1],
            self.state[2][0][0],
            self.state[2][0][1],
            self.state[3][0][0],
            self.state[3][0][1],
            self.state[4][0][0],
            self.state[4][1][0],
            self.state[4][1][1],
            self.state[4][0][1],
        ) = (
            self.state[1][0][0],
            self.state[1][0][1],
            self.state[2][0][0],
            self.state[2][0][1],
            self.state[3][0][0],
            self.state[3][0][1],
            self.state[0][0][0],
            self.state[0][0][1],
            self.state[4][1][0],
            self.state[4][1][1],
            self.state[4][0][1],
            self.state[4][0][0],
        )

    def move_up_inverse(self):
        for _ in range(3):
            self.move_up()


    def move_front(self):
        (
            self.state[1][0][0],
            self.state[1][1][0],
            self.state[4][1][1],
            self.state[4][1][0],
            self.state[3][0][1],
            self.state[3][1][1],
            self.state[5][0][0],
            self.state[5][0][1],
            self.state[0][0][0],
            self.state[0][1][0],
            self.state[0][1][1],
            self.state[0][0][1],
        ) = (
            self.state[4][1][0],
            self.state[4][1][1],
            self.state[3][0][1],
            self.state[3][1][1],
            self.state[5][0][0],
            self.state[5][0][1],
            self.state[1][1][0],
            self.state[1][0][0],
            self.state[0][1][0],
            self.state[0][1][1],
            self.state[0][0][1],
            self.state[0][0][0],
        )

    def move_front_inverse(self):
        for _ in range(3):
            self.move_front()

    @staticmethod
    def is_cube_resolved(state: list) -> bool:
        for face in state:
            if (face[0] != face[1]) | (face[0][0] != face[0][1]) | (face[1][0] != face[1][1]) :
                return False
        return True

