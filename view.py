class Terminal:
    def __init__(self):
        pass

    def display_board(self, board):
        '''
                    0
        vvvvvv vvvvvv

        vvvvvv vvvvvv
                   23
        '''
        print('#' * 20)
        print('Player 1')

        overpart = board[0:12]
        underpart = board[12:]

        rows1 = max(map(abs, overpart))
        rows2 = max(map(abs, underpart))

        print('|||||| ||||||')
        for r in range(rows1):
            for i in range(6,12)[::-1]:
                if overpart[i] > (r):
                    print('x', end='')
                elif overpart[i] < -(r):
                    print('o', end='')
                else:
                    print(' ', end='')

            print(' ', end='')
            for i in range(6)[::-1]:
                if overpart[i] > (r ):
                    print('x', end='')
                elif overpart[i] < -(r):
                    print('o', end='')
                else:
                    print(' ', end='')


            print('')


        print(' ' * 20)
        for r in range(rows2)[::-1]:
            for i in range(6):
                if underpart[i] > (r):
                    print('x', end='')
                elif underpart[i] < -(r):
                    print('o', end='')
                else:
                    print(' ', end='')

            print(' ', end='')
            for i in range(6,12):
                if underpart[i] > (r):
                    print('x', end='')
                elif underpart[i] < -(r):
                    print('o', end='')
                else:
                    print(' ', end='')

            print('')

        print('|||||| ||||||')
        print('Player 2')

    def display_dice_roll(self, dice1, dice2):

        print(dice1)
        print(dice2)
