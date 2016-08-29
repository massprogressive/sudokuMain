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
    _lst = []
    for element in lst:
        if element != 0:
            _lst.append(element)
    return _lst


def last_digit_in_column(lines):
    possible_moves = []
    for line in lines:
        if len(set(delete_zeros(line))) == 8:
            number = list(range(1, 10))
            for element in delete_zeros((list(line))):
                if element in number:
                    number.pop(number.index(element))
            if len(number) == 1:
                number = number[0]
                y = line.index(0)
                x = lines.index(line)
                block = int(x / 3) + int(y / 3) * 3
                possible_moves.append((number, block, y % 3, x % 3))
    return possible_moves


def last_digit_in_row(lines):
    possible_moves = []
    for line in lines:
        if len(delete_zeros(list(line))) == 8:
            number = list(range(1, 10))
            for element in delete_zeros(list(line)):
                if element in number:
                    number.pop(number.index(element))
            if len(number) == 1:
                number = number[0]
                y = lines.index(line)
                x = line.index(0)
                block = int(lines.index(line) / 3) * 3 + int(line.index(0) / 3)
                possible_moves.append((number, block, y % 3, x % 3))
    return possible_moves


def ninth_test(inst):
    from_horizontal = last_digit_in_row(inst.horizontal)
    from_vertical = last_digit_in_column(inst.vertical)
    for move in from_horizontal + from_vertical:
        inst.set_number(move[0], move[1], move[2], move[3])
    inst.horizontal_lines()
    inst.vertical_lines()
    return inst

