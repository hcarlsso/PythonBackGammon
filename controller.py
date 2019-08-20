class Terminal:
    def __init__(self):
        pass

    def select_index(self, indeces):
        '''
        Select an index where a marker is to move.
        '''
        condition = True
        option_string = ''.join(map(lambda x: '['+ str(x) +']', indeces))
        while condition:
            index = input('Select index: ' + option_string)
            if index in indeces:
                condition = False
        return index

    def select_dice(self, dices):
        '''
        Select a dice.
        '''
        condition = True
        option_string = ''.join(map(lambda x: '['+ str(x) +']', dices))
        while condition:
            try:
                index = input('Select dice to use: ' + option_string)
                dices_selected = list(filter(lambda x: x.value == index, dices))
                dice = dices_selected[0]
                if dice in dices:
                    condition = False
            except:
                pass
        return dice
