from model import Model
from model import Player
import view as v
import controller as cont

def create_game(options = 'terminal'):

    m = create_bare_game()

    # Initial positions
    pos = create_initial_positions()
    m.set_placement(pos)

    # Create view
    view = create_view(options)
    m.set_view(view)

    # Create controller
    controller = create_controller(options)
    m.set_controller(controller)

    # Create players
    p1 = Player(view, controller, '1', lambda x: x > 0)
    p2 = Player(view, controller, '2', lambda x: x < 0)
    m.set_players([p1, p2])
    return m

def create_controller(options = 'terminal'):
    return cont.Terminal()

def create_view(options = 'terminal'):

    return v.Terminal()

def create_bare_game():

    m = Model()

    return m

def create_initial_positions():
    '''
    Could be moved into Game class
    '''

    start_position_a = [
        (6, 5),
        (8, 3),
        (13, 5),
        (24, 2)
    ]

    start_position_b = [(25-i, -val) for (i,val) in start_position_a]

    return start_position_a + start_position_b
