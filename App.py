from Program.CalorieCounter import CalorieCounter
from Program.RockPaperScissors import RockPaperScissors
from Program.RucksackOrganiser import RucksackOrganiser

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

def rucksack_organiser():
    rso = RucksackOrganiser()
    rso.read_data("Day3-RucksackOrganization/Data.txt")
    common_item_sum = rso.get_common_item_priority_sum()
    print("common item sum:")
    print(common_item_sum)

    common_group_item_sum = rso.get_group_item_priority_sum()
    print("group badges sum:")
    print(common_group_item_sum)

def main():
    #max_calories()
    #rock_paper_sciss()
    #rucksack_organiser()
    pass

if __name__=="__main__":
    main()