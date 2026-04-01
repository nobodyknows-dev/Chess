def pawn_move(color, pos, black_pos, white_pos):
    moves = []
    promotion = False
    x, y = pos % 8, pos // 8

    if color == "wh":
        # Move forward
        if pos - 8 not in black_pos and pos - 8 not in white_pos:
            if y == 6 and pos - 16 not in black_pos and pos - 16 not in white_pos:
                moves.append(pos - 16)
                moves.append(pos - 8)
            else:
                moves.append(pos - 8)

        # Capture
        if pos - 9 in black_pos and x != 0:
            moves.append((pos - 9))
        if pos - 7 in black_pos and x != 7:
            moves.append((pos - 7))

        # Promotion
        if y == 1:
            promotion = True

    if color == "bl":
        # Move forward
        if pos + 8 not in black_pos and pos + 8 not in white_pos:
            if y == 1 and pos + 16 not in black_pos and pos + 16 not in white_pos:
                moves.append(pos + 16)
                moves.append(pos + 8)
            else:
                moves.append(pos + 8)

        # Capture
        if pos + 9 in white_pos and x != 7:
            moves.append((pos + 9))
        if pos + 7 in white_pos and x != 0:
            moves.append((pos + 7))

        # Promotion
        if y == 7:
            promotion = True
            
    return moves, promotion