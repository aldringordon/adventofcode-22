from Program.CalorieCounter import CalorieCounter
from Program.RockPaperScissors import RockPaperScissors

def max_calories():
    cc = CalorieCounter()
    cc.read_and_convert("Day1-CalorieCounting/Data.txt")
    print(cc.get_max_val())
    cc.remove_max()
    print(cc.get_max_val())
    cc.remove_max()
    print(cc.get_max_val())

def rock_paper_sciss():
    rps = RockPaperScissors()

    print("Reading RPS Data")
    rps.read_data("Day2-RockPaperScissors/Data.txt")

    print("Calculating Score")
    score = rps.calc_score()

    print("Score: ")
    print(score)

def main():
    #max_calories()
    rock_paper_sciss()

if __name__=="__main__":
    main()