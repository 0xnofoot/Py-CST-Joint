def get_round_bricks(brick, x_size, y_size):
    x = brick[0]
    y = brick[1]
    round_bricks = list()
    round_bricks.append((x - 1, y - 1))
    round_bricks.append((x - 1, y))
    round_bricks.append((x - 1, y + 1))
    round_bricks.append((x, y - 1))
    round_bricks.append((x, y + 1))
    round_bricks.append((x + 1, y - 1))
    round_bricks.append((x + 1, y))
    round_bricks.append((x + 1, y + 1))

    def limit_filter(brick):
        if 0 <= brick[0] < x_size and 0 <= brick[1] < y_size:
            return True
        return False

    round_bricks = list(filter(lambda b: limit_filter(b), round_bricks))

    return round_bricks
