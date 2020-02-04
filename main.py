from src.func import play
from src.parser import parser



if __name__ == '__main__':
    country, year, sec = parser()
    play(country, year, sec)
    