# pc랑 주사위 게임
pl_pos = 1
com_pos = 1


def board():
    print('*' * (pl_pos - 1) + 'P' + '*' * (30 - pl_pos))
    print('*' * (com_pos - 1) + 'C' + '*' * (30 - com_pos))


while True:
    board()
    input("Enter를 누르면 말이 움직입니다")
    pl_pos = pl_pos + 1
    com_pos = com_pos + 2