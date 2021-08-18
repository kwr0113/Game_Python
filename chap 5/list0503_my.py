# pc랑 주사위 게임
import random

pl_pos = 1
com_pos = 1


def board(pl, com):
    print('*' * (pl_pos - 1) + 'P' + '*' * (30 - pl_pos) + ' Goal', end='')
    if pl == 0:
        print()
    else:
        print(" " + str(pl))
    print('*' * (com_pos - 1) + 'C' + '*' * (30 - com_pos) + ' Goal', end='')
    if com == 0:
        print('\n')
    else:
        print(" " + str(com) + '\n')


board(0, 0)
print("주사위 게임, 스타트!")

while True:
    input("Enter를 누르면 여러분의 말이 움직입니다")
    p = random.randint(1, 6)
    pl_pos = pl_pos + p

    if pl_pos > 30:
        pl_pos = 30
    board(p, 0)
    if pl_pos == 30:
        print("여러분이 승리했습니다!")
        break

    input("Enter를 누르면 컴퓨터의 말이 움직입니다")
    c = random.randint(1, 6)
    com_pos = com_pos + c

    if com_pos > 30:
        com_pos = 30
    board(0, c)
    if com_pos == 30:
        print("컴퓨터가 승리했습니다!")
        break

