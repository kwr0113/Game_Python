# pc랑 주사위 게임
pl_pos = 6


def board():
    print('*' * (pl_pos - 1) + 'P' + '*' * (30 - pl_pos))


board()
