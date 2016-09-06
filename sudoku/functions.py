def block_idx(row, col):
    """
    Generate block index depends on row and column
    :param row: row index
    :param col: column index
    :return: block index
    """
    return int(row / 3) * 3 + int(col / 3)


def block_range(row, col):
    """
    Generate block start index and end index.
    :param row: row index
    :param col: column index
    """
    row_start, row_stop = int(row / 3) * 3, int(row / 3) * 3 + 3
    col_start, col_stop = int(col / 3) * 3, int(col / 3) * 3 + 3
    rows = list(range(row_start, row_stop))
    cols = list(range(col_start, col_stop))
    return rows, cols


def block_numbers(board, row, col):
    """
    Generate bock numbers depends on row and columns
    :param row: row index
    :param col: column index
    """
    rows, cols = block_range(row, col)
    numbers = []
    for row in rows:
        for col in cols:
            if board[row][col] != 0:
                numbers.append(board[row][col])
    return numbers


def duplicates(lst):
    """
    Function checks for duplicate in element.
    """
    for number in range(1, 10):
        if lst.count(number) > 1:
            return False
    return True


def delete_zeros(lst):
    """
    Remove 0 from list of integers.
    """
    _lst = []
    for element in lst:
        if element != 0:
            _lst.append(element)
    return _lst


def read_file(file_name):
    """
    Get board from file.
    """
    from re import findall as fa
    data = []
    # with open(file_name, 'r') as f:
    for line in f:
        row = fa('[0-9]', line)
        row = [int(digit) for digit in row]
        if len(row) == 9:
            data.append(row)
    if len(data) == 9:       
        return data
    return False

def run(cls, file_name):
    board = read_file(file_name)
    solver = cls(board)
    print()
    print('Initial board')
    print()
    print(solver)
    solved_board = solver.make_move()
    return solved_board
