from model import Model

def create_bare_game():

    m = Model()

    return m

def create_initial_positions():

    start_position_a = [
        (6, 5),
        (8, 3),
        (13, 5),
        (24, 2)
    ]

    start_position_b = [(25-i, -val) for (i,val) in start_position_a]

    return start_position_a + start_position_b
