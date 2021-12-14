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


if __name__ == '__main__':
    day1(read('samples/day1', map_fn=lambda x: int(x)))
    day1(read('puzzles/day1', map_fn=lambda x: int(x)))
    day2(read('samples/day2', map_fn=lambda x: x))
    day2(read('puzzles/day2', map_fn=lambda x: x))
