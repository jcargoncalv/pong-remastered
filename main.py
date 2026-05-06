from classes.game import Game

#Screen size tuple (width x height)
SCREEN_SIZE = (1280, 620)
#FPS rate
FPS = 60
WIN_SCORE = 10

def main():
    game = Game(SCREEN_SIZE, FPS, WIN_SCORE)
    game.run()



if __name__ == "__main__":
    main()