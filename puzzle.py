board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3      **",
 "  8  2***",
 "  2  ****"
 ]


def check_rows(board: list) -> bool:
    """
    Return True if all numbers in lines are unique.

    >>> check_rows(board)
    True
    """
    digit_dict = {}
    counter = 0

    for element in board:
        for subel in element:
            if subel.isdigit():
                if counter not in digit_dict:
                    digit_dict[counter] = [subel]
                else:
                    digit_dict[counter].append(subel)
        counter += 1
    for value in digit_dict.values():
        if not len(value) == len(set(value)):
            return False
    return True


def check_columns(board: list) -> bool:
    """
    Return True if all numbers in columns are unique.

    >>> check_columns(board)
    True
    """
    column_lst = [[] for i in range(len(board))]

    for element in board:
        for ind, subel in enumerate(element):
            column_lst[ind].append(subel)
    column_lst = [list(filter(lambda x: x.isdigit(), lst))
                  for lst in column_lst]
    for element in column_lst:
        if len(element) != len(set(element)):
            return False
    return True


def check_bloc(board: list) -> bool:
    """
    Return True if all numbers in certain bloc of colours are unique.

    >>> check_bloc(board)
    True
    """
    pass


def validate_board(board: list) -> bool:
    """
    Return True if board is ready for the game.

    >>> validate_board(board)
    False
    """
    return check_rows and check_columns and check_bloc