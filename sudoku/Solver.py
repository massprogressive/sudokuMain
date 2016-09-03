from .functions import *
from .global_variables import *


class Solver:
    """
    Board is a class allows you set specified board, get
    information and manipulate board.
    """
    def __init__(self, board=None):
        """
        Initializes board with passed initial or creates one
        filled with zeros.
        :param board: initial board
        """
        self.numbers = NUMBERS
        self.block_height = BLOCK_HEIGHT
        self.block_width = BLOCK_WIDTH
        self.num_blocks = NUM_BLOCKS
        self.board = board or self.make_board()

    def make_board(self):
        """
        Creates board filled zeros.
        """
        return [[0] * self.num_blocks for y in range(self.num_blocks)]

    def get_move(self):
        """
        Returns the first possible position to move
        :return: row and column
        """
        for row in range(self.num_blocks):
            for col in range(self.num_blocks):
                if self.board[row][col] == 0:
                    return row, col

    def get_numbers(self, row, col):
        """
        Generate the list on numbers not in block and not in line.
        :param row: board row
        :param col: board column
        :return: list of numbers
        """
        block_nums = block_numbers(self.board, row, col)
        line_nums = delete_zeros(self.board[row])
        numbers = [number for number in range(1, 10) if number not in line_nums + block_nums]
        return numbers

    def check_position(self, row, col):
        """
        Checks specified position on board.
        :param row: board row
        :param col: board column
        :return: True if all conditions satisfied, otherwise - False
        """
        horizontal = duplicates(self.board[row])
        vertical = duplicates([self.board[_row][col] for _row in range(self.num_blocks)])
        block = duplicates(block_numbers(self.board, row, col))
        return horizontal and vertical and block

    def check_all(self):
        """
        Checks whole board
        :return: True if board is solved, otherwise - False
        """
        for row in self.board:
            if not duplicates(delete_zeros(row)):
                return False
        for column in zip(*self.board):
            if not duplicates(column):
                return False
        return True

    def __str__(self):
        """
        String representation of the board
        """
        string = ''
        for row in range(self.num_blocks):
            if row == 3 or row == 6:
                string += ('*' * 11 + '\n')
            for col in range(self.num_blocks):
                if col == 3 or col == 6:
                    string += '|'
                string += str(self.board[row][col])
            string += '\n'
        return string

    def make_move(self):
        if self.get_move() is None:
            if self.check_all():
                print(self)
                return self
        else:
            row, col = self.get_move()
            numbers = self.get_numbers(row, col)
            for number in numbers:
                self.board[row][col] = number
                if self.check_position(row, col):
                    self.make_move()
            self.board[row][col] = 0
