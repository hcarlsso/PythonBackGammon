import unittest as ut
import factory as f

class TestGame(ut.TestCase):

    def test_placement(self):

        m = f.create_bare_game()
        pos = f.create_initial_positions()

        m.set_placement(pos)
        self.assertDictEqual(
            dict(m.get_placement()),
            dict(pos)
        )

if __name__ == '__main__':
    ut.main()
