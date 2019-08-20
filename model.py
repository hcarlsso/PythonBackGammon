from itertools import cycle
from random import randint

class Model:

    def __init__(self):

        self.players = []
        self.board = [0] * 24

        self.view = None
        self.controller = None

    def set_players(self, players):
        self.players = players

    def set_view(self, view):
        self.view = view

    def set_controller(self, controller):
        self.controller = controller

    def play(self):
        '''
        Infinite loop
        '''
        for player in cycle(self.players):
            self.view.display_board(self.board)
            player.play(self.board)

    def get_placement(self):
        #positions
        placement = []
        for i, val in enumerate(self.board):
            if val != 0:
                placement.append((i+1, val))
        return placement

    def set_placement(self, placement):
        self.board = [0] * 24
        for (i, val) in placement:
            self.board[i-1] = val

class Player:

    def __init__(self, view, controller, name, func, move_func):

        self.view = view
        self.controller = controller
        self.name = name
        self.func = func
        self.move_func = move_func

    def play(self, board):


        dices = self.roll_dices()
        self.view.display_dice_roll(dices, self.name)

        self.play_dice(board, dices)


    def roll_dices(self):

        dice1 = Dice()
        dice2 = Dice()

        dice1.roll()
        dice2.roll()

        dices = [dice1, dice2]
        # Check double roll
        if dice1.value == dice2.value:
            dice3 = Dice(dice1.value)
            dice4 = Dice(dice1.value)
            dices.extend([dice3, dice4])

        return dices

    def get_allowable_index(self, board):
        '''
        Player index
        '''
        allowable_actions = []
        for (i, state) in enumerate(board):
            if self.func(state):
                allowable_actions.append(i+1)

        return allowable_actions

    def play_dice(self, board, dices):

        allowable_actions = self.get_allowable_index(board)
        index = self.controller.select_index(allowable_actions)

        dice = self.controller.select_dice(dices)

        self.move_marker(board, index, dice.value)

    def move_marker(self, board, index, steps):

        board[index] = self.move_func()


class Dice:
    def __init__(self, value=None):
        self.value = value

    def roll(self):
        self.value = randint(1, 6)

    def __str__(self):
        return str(self.value)
