import factory as f



def main():

    game = f.create_game(options = 'terminal')
    game.play()

if __name__ == '__main__':
    main()
