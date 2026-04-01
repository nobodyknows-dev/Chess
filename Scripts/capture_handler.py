def handler(turn, black_pos, white_pos):
    for x in black_pos:
        if x in white_pos:
            if turn:
                white_pos[white_pos.index(x)] = -1
            else:
                black_pos[black_pos.index(x)] = -1

    return black_pos, white_pos