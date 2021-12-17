import numpy as np


def read(filepath, map_fn):
    with open(filepath, 'r') as f:
        return list(map(map_fn, f.readlines()))


def day1(report):
    report_sums = []
    for i in range(len(report) - 2):
        report_sums.append(sum(report[i:i + 3]))

    n_increases = 0
    for i in range(1, len(report_sums)):
        if report_sums[i] > report_sums[i - 1]:
            n_increases += 1

    print(f'The number of times a depth measurement increases: {n_increases}')


def day2(course):
    depth = 0
    horizontal_pos = 0
    aim = 0

    for line in course:
        command, units = line.strip().split(' ')
        units = int(units)
        if command == 'forward':
            horizontal_pos += units
            depth += aim * units
        if command == 'down':
            aim += units
        if command == 'up':
            aim -= units

    print(f'Final => horizontal position: {horizontal_pos}, depth: {depth} (product: {horizontal_pos * depth})')


def day3part1(report):
    gamma_rate = ''
    epsilon_rate = ''
    for bit_idx in range(len(report[0].strip())):
        n_zeros = 0
        n_ones = 0

        for line in report:
            if line.strip()[bit_idx] == '0':
                n_zeros += 1
            else:
                n_ones += 1

        if n_zeros < n_ones:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(
        f'Gamma rate: {gamma_rate} = {int(gamma_rate, 2)}, epsilon rate: {epsilon_rate} = {int(epsilon_rate, 2)}, '
        f'power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')


def day3part2(report):
    def get_rating(report, bit_idx, criteria, line_len):
        if len(report) == 1:
            return int(report[0], 2)

        zero_bit = np.zeros(0, dtype=np.bool)

        for line in report:
            zero_bit = np.append(zero_bit, True) if line.strip()[bit_idx] == '0' else np.append(zero_bit, False)

        report = report[zero_bit] if criteria(zero_bit) else report[np.invert(zero_bit)]
        bit_idx = bit_idx + 1 if bit_idx < line_len - 1 else 0

        return get_rating(report, bit_idx, criteria, line_len)

    def oxygen_criteria(zero_bit):
        return np.sum(zero_bit) > np.sum(np.invert(zero_bit))

    def co2_criteria(zero_bit):
        return np.sum(zero_bit) <= np.sum(np.invert(zero_bit))

    report = np.array(report)
    line_len = len(report[0].strip())
    oxygen_generator_rating = get_rating(report, 0, oxygen_criteria, line_len)
    co2_scrubber_rating = get_rating(report, 0, co2_criteria, line_len)

    print(
        f'Oxygen generator rating: {oxygen_generator_rating}, CO2 Scrubber rating: {co2_scrubber_rating} => Life '
        f'support rating: {oxygen_generator_rating * co2_scrubber_rating}')


def day4part1(bingo):
    def parse_board(board):
        return np.array(list(map(lambda x: np.fromstring(x.strip(), dtype=int, sep=' '), board)))[..., None]

    boards = np.empty((5, 5, 0), dtype=int)
    for i in range(2, len(bingo) - 4, 6):
        boards = np.append(boards, parse_board(bingo[i:i + 5]), axis=-1)

    winning_board = -1
    last_number = -1

    for number in list(map(int, bingo[0].strip().split(','))):
        boards[boards == number] = -1

        if np.any(np.sum(boards, axis=0) == -5):
            winning_board = np.where(np.sum(boards, axis=0) == -5)[1][0]
            last_number = number
            break
        elif np.any(np.sum(boards, axis=1) == -5):
            winning_board = np.where(np.sum(boards, axis=1) == -5)[1][0]
            last_number = number
            break

    if winning_board > -1:
        board = boards[..., winning_board]
        score = np.sum(board[board != -1]) * last_number
        print(f'Winning board: {winning_board} Last number: {last_number} Unmarked sum: {np.sum(board[board != -1])} '
              f'Score: {score}')


def day4part2(bingo):
    def parse_board(board):
        return np.array(list(map(lambda x: np.fromstring(x.strip(), dtype=int, sep=' '), board)))[..., None]

    boards = np.empty((5, 5, 0), dtype=int)
    for i in range(2, len(bingo) - 4, 6):
        boards = np.append(boards, parse_board(bingo[i:i + 5]), axis=-1)

    last_winning_board = -1
    last_number = -1

    print(len(bingo[0].strip()))
    i = 0
    for number in list(map(int, bingo[0].strip().split(','))):
        boards[boards == number] = -1
        i += 1

        if np.any(np.sum(boards, axis=0) == -5):
            print(np.where(np.sum(boards, axis=0) == -5))
            last_winning_board = np.where(np.sum(boards, axis=0) == -5)[1]
            last_number = number
            if boards.shape[-1] == 1:
                break
            else:
                boards = np.delete(boards, last_winning_board, axis=-1)
        elif np.any(np.sum(boards, axis=1) == -5):
            print(np.where(np.sum(boards, axis=1) == -5))
            last_winning_board = np.where(np.sum(boards, axis=1) == -5)[1]
            last_number = number
            if boards.shape[-1] == 1:
                break
            else:
                boards = np.delete(boards, last_winning_board, axis=-1)

    if last_winning_board > -1:
        board = boards[..., last_winning_board]
        score = np.sum(board[board != -1]) * last_number
        print(
            f'Winning board: {last_winning_board} Last number: {last_number} Unmarked sum: '
            f'{np.sum(board[board != -1])} '
            f'Score: {score}')


if __name__ == '__main__':
    # day1(read('samples/day1', map_fn=lambda x: int(x)))
    # day1(read('puzzles/day1', map_fn=lambda x: int(x)))
    # day2(read('samples/day2', map_fn=lambda x: x))
    # day2(read('puzzles/day2', map_fn=lambda x: x))
    # day3(read('samples/day3', map_fn=lambda x: x))
    # day3part1(read('puzzles/day3', map_fn=lambda x: x))
    # day3part2(read('puzzles/day3', map_fn=lambda x: x))  # Oxygen: 825, Co2: 3375 => Life support rating: 2784375
    # day4part1(read('samples/day4', map_fn=lambda x: x))
    day4part1(read('puzzles/day4', map_fn=lambda x: x))  # Board: 41 Last num: 48 Unmarked sum: 932 Score: 44736
    day4part2(read('puzzles/day4', map_fn=lambda x: x))  # Board: 0 Last number: 7 Unmarked sum: 261 Score: 1827
