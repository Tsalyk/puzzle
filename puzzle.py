board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
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
    False
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
    colours_lst = [[] for i in range(5)]

    for ind, element in enumerate(board):
        for subind, subel in enumerate(element):
            if subel != "*":
                if subind >= 4 and ind <= 4:
                    colours_lst[0].append(subel)
                elif subind >= 3 and ind <= 5:
                    colours_lst[1].append(subel)
                elif subind >= 2 and ind <= 6:
                    colours_lst[2].append(subel)
                elif subind >= 1 and ind <= 7:
                    colours_lst[3].append(subel)
                elif subind >= 0 and ind <= 8:
                    colours_lst[4].append(subel)

    colours_lst = [list(filter(lambda el: el != " ", lst))
                   for lst in colours_lst]

    for element in colours_lst:
        if len(set(element)) != len(element):
            return False

    return True


def validate_board(board: list) -> bool:
    """
    Return True if board is ready for the game.

    >>> validate_board(board)
    False
    """
    return check_rows(board) and check_columns(board) and check_bloc(board)