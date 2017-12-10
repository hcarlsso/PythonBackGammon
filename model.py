class Model:

    def __init__(self):

        self.players = []
        self.board = [0] * 24


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

    def __init__(self, view, controller):

        self.view = view
        self.controller = controller
