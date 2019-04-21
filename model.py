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

    def __init__(self, view, controller, name, func):

        self.view = view
        self.controller = controller
        self.name = name
        self.func = func
allowable_actions
    def play(self, board):
        self.view.display_board(board)
        (dice1, dice2) = self.roll_dice()
        self.view.display_dice_roll(dice1, dice2, self.name)



        self.controller.select_move()

    def roll_dice(self):
        (dice1, dice2) = (randint(1,6), randint(1,6))
        return (dice1, dice2)

    def get_allowable_index(self, board):
        allowable_actions = []
        for (i, state) in enumerate(board):
            if self.func(state):
                allowable_actions.append(i+1)

        return allowable_actions
