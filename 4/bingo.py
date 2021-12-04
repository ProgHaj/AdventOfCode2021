import numpy as np
from dataclasses import dataclass


@dataclass
class BingoSet:
    numbers: set
    val: int = 0


class BingoBoard:
    def __init__(self, board: np.ndarray):
        self.board = board
        self.numbers = set(board.flatten())
        self.drawn = set()
        self.win = len(board)

        # diag1 = board.diagonal()
        # diag2 = np.fliplr(board).diagonal()
        # bingosets = [BingoSet(set(diag1)), BingoSet(set(diag2))]
        bingosets = []

        for row in board:
            bingosets.append(BingoSet(set(row)))

        for col in board.transpose():
            bingosets.append(BingoSet(set(col)))

        self.bingosets = bingosets

    def check_win(self):
        return any(bingoset.val >= self.win for bingoset in self.bingosets)

    def add_number(self, number):
        self.drawn.add(number)
        for bingoset in self.bingosets:
            bingoset.val += 1 if number in bingoset.numbers else 0

    def calc_score(self, win_number):
        return sum(self.numbers - self.numbers.intersection(self.drawn)) * win_number


def setup_bingo(fn):
    with open(fn, "r") as f:
        numbers_drawn = f.readline().strip().split(",")
        rest = f.read()

    numbers_drawn = [int(drawn) for drawn in numbers_drawn]
    boards = rest.split("\n\n")

    board_list = []
    for board_raw in boards:
        board = []
        rows = board_raw.split("\n")
        for row in rows:
            row = row.split()
            row = [int(numb) for numb in row]
            if row:
                board.append(row)

        bingo_board = BingoBoard(np.array(board))
        board_list.append(bingo_board)

    return numbers_drawn, board_list


def play_bingo(fn):
    numbers_drawn, board_list = setup_bingo(fn)

    for number in numbers_drawn:
        for board in board_list:
            board.add_number(number)
            if board.check_win():
                print(f"Score: {board.calc_score(number)}, winning number: {number}")
                return

    print("NO ONE WON")


def play_bingo_p2(fn):
    numbers_drawn, board_list = setup_bingo(fn)

    needed_wins = len(board_list)
    current_wins = 0
    board_list = [[board, 0] for board in board_list]

    for number in numbers_drawn:
        for i, (board, has_win) in enumerate(board_list):
            board.add_number(number)
            if not has_win and board.check_win():
                current_wins += 1
                board_list[i][1] = 1

            if current_wins == needed_wins:
                print(f"Score: {board.calc_score(number)}, winning number: {number}")
                return

    print("NO ONE WON")
