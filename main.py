from schedule import get_todays_games
from boxscore import get_box_score
def main():
    print(get_todays_games())
    get_box_score("0022600273")



if __name__ == "__main__":
    main()