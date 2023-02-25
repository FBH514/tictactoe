class Player:

    def __init__(self, mark: str) -> None:
        """
        Constructor for the Player object
        :param mark: str
        :return None
        """
        if mark.lower() not in ["x", "o"]:
            raise ValueError("Mark can only be X or O.")
        self._mark: str = mark
        self._turn = False

    def __repr__(self) -> str:
        """
        Returns a string definition of Player attributes
        :return: str
        """
        return str(vars(self))

    @property
    def mark(self) -> str:
        """
        Returns Player's mark
        :return:
        """
        return self._mark

    @property
    def turn(self) -> bool:
        """
        Getter for the turn property
        :return: bool
        """
        return self._turn

    @turn.setter
    def turn(self, value: bool) -> None:
        """
        Setter for the turn property
        :param value: bool
        :return: None
        """
        self._turn = value

    @staticmethod
    def user_input(prompt: str) -> int:
        """
        Gets the user input
        :param prompt: str
        :return: int
        """
        while True:
            try:
                user = int(input(f"{prompt}:\t"))
                if user not in range(1, 10):
                    print(f"Invalid Input. Please choose between {range(1, 10)}")
                    continue
                return user
            except ValueError:
                print(f"Invalid Input. Please choose between {range(1, 10)}")


class Board:

    def __init__(self) -> None:
        """
        Constructor for the Board object
        :return None
        """
        self._board: list = self.make_board()
        self._active: int = 0

    def __repr__(self) -> str:
        """
        Returns a string representation of the Board object
        :return: str
        """
        board: str = ''
        for count, item in enumerate(self.board):
            board += f"{item}\n"
            if count < 2:
                board += "————|—————|————\n"

        return f"Current Board:\n" \
               f"{board}"

    @property
    def board(self) -> list:
        """
        Getter for the board property
        :return: list
        """
        return self._board

    @staticmethod
    def make_board() -> list:
        """
        Defines the starting board for Tic Tac Toe
        :return: list
        """
        board = []
        for row in range(3):
            board.append([' ' for _ in range(3)])
        return board

    @property
    def active(self) -> int:
        """
        Returns the number of active cases
        :return: int
        """
        return self._active

    def insert(self, mark: str, case: int) -> None:
        """
        Inserts the mark into the board
        :param mark: str
        :param case: int
        :return: None
        """
        if case in [1, 2, 3]:
            self.board[0][case - 1] = mark
        elif case in [4, 5, 6]:
            self.board[1][case - 4] = mark
        elif case in [7, 8, 9]:
            self.board[2][case - 7] = mark
        else:
            raise ValueError(f"Invalid case, must be between {'—'.join(str(item + 1) for item in range(9))}")
        self._active += 1


class Game:

    def __init__(self) -> None:
        """
        Constructor for the Game object
        :return None
        """
        self._board = Board()
        self._board.make_board()
        self._player1 = Player("x")
        self._player2 = Player("o")
        self._player1 = True

    def __repr__(self) -> str:
        """
        Returns a string representation of the Game object
        :return:
        """
        return str(vars(self))

    @staticmethod
    def check_win(board: list, mark: str) -> bool:
        """
        Checks if Player won.
        :param board: list
        :param mark: mark
        :return: bool
        """
        for _ in range(3):
            if board[_][0] is mark and \
                    board[_][1] is mark and \
                    board[_][2] is mark:
                return True
            elif board[0][_] is mark \
                    and board[1][_] is mark \
                    and board[2][_] is mark:
                return True
        if board[0][0] is mark \
                and board[1][1] is mark \
                and board[2][2] is mark:
            return True
        elif board[2][0] is mark \
                and board[1][1] is mark \
                and board[0][2] is mark:
            return True
        return False

    def run(self) -> None:
        """
        Runs the game
        :return: None
        """
        prompt = "Pick a case."
        while self._board.active < 10:
            print(self._board)
            if self._player1:
                self._board.insert("x", Player.user_input(prompt))
                self._player1 = False
                self._player2 = True
                if self.check_win(self._board.board, "x"):
                    print("Player 1 with mark X wins!")
                    break
            else:
                self._board.insert("o", Player.user_input(prompt))
                self._player1 = True
                self._player2 = False
                if self.check_win(self._board.board, "o"):
                    print("Player 2 with mark O wins!")
                    break


if __name__ == '__main__':
    Game().run()