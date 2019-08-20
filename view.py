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
        EMPTY = ' ' * 3
        P1_SIGN = ' x '
        P2_SIGN = ' o '
        SEP_VERT = ' | '
        SEP_HOR = ' v '

        print('#' * 20)
        print('Player 1')

        overpart = board[0:12]
        underpart = board[12:]

        rows1 = max(map(abs, overpart))
        rows2 = max(map(abs, underpart))


        format_spec = "{0: ^3}"
        # Indexing the positions
        print(
            ''.join(map(
                lambda x: format_spec.format(x),
                range(7,13)[::-1]
            )),
            SEP_VERT,
            ''.join(map(
                lambda x: format_spec.format(x),
                range(1,7)[::-1]
            )),
            sep = ''
        )
        print((SEP_HOR * 6) + SEP_VERT + (SEP_HOR * 6))
        for r in range(rows1):
            for i in range(6,12)[::-1]:
                if overpart[i] > (r):
                    print(P1_SIGN, end='')
                elif overpart[i] < -(r):
                    print(P2_SIGN, end='')
                else:
                    print(EMPTY, end='')

            print(SEP_VERT, end='')
            for i in range(6)[::-1]:
                if overpart[i] > (r ):
                    print(P1_SIGN, end='')
                elif overpart[i] < -(r):
                    print(P2_SIGN, end='')
                else:
                    print(EMPTY, end='')


            print('')


        print(' ' * 20)
        for r in range(rows2)[::-1]:
            for i in range(6):
                if underpart[i] > (r):
                    print(P1_SIGN, end='')
                elif underpart[i] < -(r):
                    print(P2_SIGN, end='')
                else:
                    print(EMPTY, end='')

            print(SEP_VERT, end='')
            for i in range(6,12):
                if underpart[i] > (r):
                    print(P1_SIGN, end='')
                elif underpart[i] < -(r):
                    print(P2_SIGN, end='')
                else:
                    print(EMPTY, end='')

            print('')

        print((SEP_HOR * 6) + SEP_VERT + (SEP_HOR * 6))
        print(
            ''.join(map(
                lambda x: format_spec.format(x),
                range(1+12,7+12)
            )),
            SEP_VERT,
            ''.join(map(
                lambda x: format_spec.format(x),
                range(7+12,13+12)
            )),
            sep = ''
        )
        print('Player 2')
        print('#' * 20)

    def display_dice_roll(self, dices, player):
        if len(dices) == 2:
            print(
                'Player ' + player +
                ' rolled ' + str(dices[0]) +
                ' and ' + str(dices[1])
            )
        else:
            print(
                'Player ' + player + ' rolled double ' + str(dices[0])
            )
