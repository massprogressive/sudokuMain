from newFunctions import *
from global_variables import *


class Board:
    """
    Board is a class allows you set specified board, get
    information and manipulate board.
    """
    def __init__(self, makeBoard=False, makeMoves=False):
        """
        Creates board class with class with board
        fulfilled zeros.
        """
        self.numbers = NUMBERS
        self.block_height = BLOCK_HEIGHT
        self.block_width = BLOCK_WIDTH
        self.num_blocks = NUM_BLOCKS
        self.board = None
        if makeBoard:
            self.make_board()

    def make_board(self):
        """
        Creates board fulfilled zeros.
        """
        self.board = [[0 for x in range(9)] for y in range(9)]

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
        Cheks specified position on board.
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
        for col in range(self.num_blocks):
            col_numbers = delete_zeros([self.board[_row][col] for _row in range(self.num_blocks)])
            if not duplicates(col_numbers):
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


def make_move(board_inst):
    if board_inst.get_move() is None:
        if board_inst.check_all():
            print('Solved board')
            print()
            print(board_inst)
            return board_inst
    else:
        row, col = board_inst.get_move()
        numbers = board_inst.get_numbers(row, col)
        for number in numbers:
            board_inst.board[row][col] = number
            if board_inst.check_position(row, col):
                make_move(board_inst)
        board_inst.board[row][col] = 0
